from django.urls import reverse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.serializers import ValidationError
from rest_framework.views import APIView

from lws.models import Course, Lesson
from lws.permissions import IsModerator
from users.models import Payment, User
from users.serializer import PaymentSerializer, UserLightSerializer, UserSerializer
from users.src.stripe_utils import (
    create_link_for_pay,
    create_price_on_stripe,
    get_status_payment,
)


class UserCreateAPIView(generics.CreateAPIView):

    permission_classes = (AllowAny,)
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class UserDeleteAPIView(generics.DestroyAPIView):
    queryset = User.objects.all()

    def get_permissions(self):
        if not (self.request.user.is_superuser):
            self.permission_denied(
                self.request,
                {"detail": "You do not have permission to perform this action."},
            )

        return super().get_permissions()


class UsersRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()

    def get_permissions(self):
        if not self.request.method == "GET":
            if not (self.kwargs.get("pk") == self.request.user.id):
                self.permission_denied(
                    self.request,
                    {"detail": "You do not have permission to perform this action."},
                )

        return super().get_permissions()

    def get_serializer_class(self):
        user_pk = self.kwargs.get("pk")
        if user_pk is not None:
            if user_pk == self.request.user.id:
                return UserSerializer

        return UserLightSerializer


class PaymentListAPIView(generics.ListAPIView):

    serializer_class = PaymentSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = [
        "course",
        "lesson",
    ]
    ordering_fields = [
        "date_of_payment",
    ]
    permission_classes = (IsModerator,)

    def get_queryset(self):
        queryset = Payment.objects.all()
        payment_method = self.request.query_params.get("payment_method", None)
        if payment_method:
            queryset = queryset.filter(payment_method=payment_method)
        return queryset


class PaymentGetLinkAPIView(generics.CreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    def perform_create(self, serializer):
        payment = serializer.save(user=self.request.user, payment_method="CARD")
        pk = self.kwargs.get("pk")
        obj = None
        if self.request.stream.path == reverse("lws:course_pay", kwargs={"pk": pk}):
            obj = Course.objects.filter(pk=pk).first()
            payment.course = obj
        elif self.request.stream.path == reverse("lws:lesson_pay", kwargs={"pk": pk}):
            obj = Lesson.objects.filter(pk=pk).first()
            payment.lesson = obj
        if obj is None:
            raise ValidationError("Нет такого материала для обучения")
        payment.cost = obj.price
        price = create_price_on_stripe(obj)
        payment.payment_id, payment.payment_link = create_link_for_pay(price)
        payment.save()


class PaymentGetStatusAPIView(APIView):

    def get(self, *args, **kwargs):
        pk = kwargs.get("pk")
        if self.request.stream.path == reverse(
            "lws:course_paystatus", kwargs={"pk": pk}
        ):
            obj = Course.objects.filter(pk=pk).first()
            payment = Payment.objects.filter(
                user=self.request.user, course=obj, lesson=None
            ).first()
        elif self.request.stream.path == reverse(
            "lws:lesson_paystatus", kwargs={"pk": pk}
        ):
            obj = Lesson.objects.filter(pk=pk).first()
            payment = Payment.objects.filter(
                user=self.request.user, course=None, lesson=obj
            ).first()

        if payment is not None:
            status = get_status_payment(payment.payment_id)
        else:
            status = "payment not found"

        return Response({"status": status})
