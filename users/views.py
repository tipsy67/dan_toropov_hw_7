from rest_framework import generics

from users.models import User
from users.serializer import UserSerializer


class UsersRetrieveAPIView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
