from lws.urls import urlpatterns
from users.apps import UsersConfig
from django.urls import path

from users.views import UsersRetrieveAPIView

app_name = UsersConfig.name

urlpatterns=[
    path ("/<int:pk>", UsersRetrieveAPIView.as_view(), name="user_view")
]