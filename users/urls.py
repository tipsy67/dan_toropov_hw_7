
from users.apps import UsersConfig
from django.urls import path

from users.views import UsersRetrieveAPIView, PaymentListAPIView

app_name = UsersConfig.name

urlpatterns=[
    path ("<int:pk>/", UsersRetrieveAPIView.as_view(), name="user_view"),
    path ("payment/",PaymentListAPIView.as_view(), name="payment_list")
]