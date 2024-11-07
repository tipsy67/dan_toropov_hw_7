from gc import get_objects
from drf_yasg.utils import swagger_auto_schema
from django.shortcuts import get_object_or_404
from rest_framework import generics, status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from lws.models import Course, Lesson, Subscribe
from lws.paginators import LWSPagination
from lws.permissions import IsModerator, IsOwner
from lws.serializer import CourseSerializer, LessonSerializer


# Course------------------------
class CourseViewSet(viewsets.ModelViewSet):
    # queryset = Course.objects.all()
    serializer_class = CourseSerializer
    pagination_class = LWSPagination

    def get_queryset(self):
        if self.request.user.is_moderator or self.request.user.is_superuser:
            return Course.objects.all()

        return Course.objects.filter(owner=self.request.user)

    def get_permissions(self):
        if self.action == "create":
            self.permission_classes = (~IsModerator, IsAuthenticated)
        elif self.action in ("retrieve", "update", "partial_update"):
            self.permission_classes = (IsOwner | IsModerator, IsAuthenticated)
        elif self.action == "destroy":
            self.permission_classes = (IsOwner, IsAuthenticated)

        return super().get_permissions()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


# Lesson________________________
class LessonListAPIView(generics.ListAPIView):
    # queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    pagination_class = LWSPagination

    def get_queryset(self):
        if self.request.user.is_moderator or self.request.user.is_superuser:
            return Lesson.objects.all()

        return Lesson.objects.filter(owner=self.request.user)


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (IsOwner | IsModerator, IsAuthenticated)


class LessonUpdateAPIView(generics.UpdateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (IsOwner | IsModerator, IsAuthenticated)


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = (~IsModerator, IsAuthenticated)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    permission_classes = (IsOwner, IsAuthenticated)


class SubscribeSetAPIView(APIView):

    @swagger_auto_schema(
        responses={200: '{"message":"подписка создана|выключена|включена"}'}
    )
    def post(self, *args, **kwargs):
        """Процедура создания подписки, либо ее активации/деактивации"""
        user = self.request.user
        course_pk = kwargs.get("pk")
        course = get_object_or_404(Course, pk=course_pk)
        subscribe_item = Subscribe.objects.filter(user=user, course=course).first()
        if subscribe_item is None:
            Subscribe.objects.create(user=user, course=course, is_active=True)
            message = "подписка создана"
        else:
            if subscribe_item.is_active:
                subscribe_item.is_active = False
                message = "подписка выключена"
            else:
                subscribe_item.is_active = True
                message = "подписка включена"
            subscribe_item.save()

        return Response({"message": message}, status.HTTP_200_OK)
