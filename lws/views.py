from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated

from lws.models import Course, Lesson
from lws.permissions import IsModerator, IsOwner
from lws.serializer import CourseSerializer, LessonSerializer


# Course------------------------
class CourseViewSet(viewsets.ModelViewSet):
    # queryset = Course.objects.all()
    serializer_class = CourseSerializer

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
