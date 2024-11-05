from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics
from rest_framework.permissions import AllowAny

from lws.permissions import IsModerator
from users.models import Payment, User
from users.serializer import PaymentSerializer, UserLightSerializer, UserSerializer


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
