from django.urls import path
from rest_framework.routers import DefaultRouter


from lws import views
from lws.apps import LwsConfig
from lws.views import CourseViewSet

app_name = LwsConfig.name

router = DefaultRouter()
router.register(r"course", CourseViewSet, basename="Course")

urlpatterns = [
    path(
        "course/<int:pk>/subscribe/",
        views.SubscribeSetAPIView.as_view(),
        name="subscribe",
    ),
    path("lesson/", views.LessonListAPIView.as_view(), name="lesson_list"),
    path("lesson/<int:pk>/", views.LessonRetrieveAPIView.as_view(), name="lesson_view"),
    path(
        "lesson/<int:pk>/update/",
        views.LessonUpdateAPIView.as_view(),
        name="lesson_update",
    ),
    path(
        "lesson/<int:pk>/delete/",
        views.LessonDestroyAPIView.as_view(),
        name="lesson_delete",
    ),
    path("lesson/create/", views.LessonCreateAPIView.as_view(), name="lesson_create"),
] + router.urls
