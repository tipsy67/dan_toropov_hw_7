from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from users.models import User, Payment
from users.serializer import UserSerializer, PaymentSerializer


class UsersRetrieveAPIView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


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

    def get_queryset(self):
        queryset = Payment.objects.all()
        payment_method = self.request.query_params.get("payment_method", None)
        if payment_method:
            queryset = queryset.filter(payment_method=payment_method)
        return queryset
