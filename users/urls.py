from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from users.apps import UsersConfig
from users.views import (PaymentListAPIView, UserCreateAPIView,
                         UserDeleteAPIView, UsersRetrieveUpdateAPIView)

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
    path("create/", UserCreateAPIView.as_view(), name="user_create"),
    path("<int:pk>/", UsersRetrieveUpdateAPIView.as_view(), name="user_view"),
    path("<int:pk>/delete/", UserDeleteAPIView.as_view(), name="user_delete"),
    path("payment/", PaymentListAPIView.as_view(), name="payment_list"),
]
