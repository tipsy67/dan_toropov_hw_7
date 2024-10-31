from users.apps import UsersConfig
from django.urls import path

from users.views import UsersRetrieveAPIView, PaymentListAPIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.permissions import AllowAny

app_name = UsersConfig.name

urlpatterns = [
    path(
        "login/",
        TokenObtainPairView.as_view(permission_classes=(AllowAny,)),
        name="login",
    ),
    path(
        "token/refresh/",
        TokenRefreshView.as_view(permission_classes=(AllowAny,)),
        name="token_refresh",
    ),
    path("<int:pk>/", UsersRetrieveAPIView.as_view(), name="user_view"),
    path("payment/", PaymentListAPIView.as_view(), name="payment_list"),
]
