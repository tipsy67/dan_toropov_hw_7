from django.urls import path
from rest_framework.routers import DefaultRouter

from lws import views
from lws.apps import LwsConfig
from lws.views import CourseViewSet
from users.views import PaymentGetLinkAPIView, PaymentGetStatusAPIView

app_name = LwsConfig.name

router = DefaultRouter()
router.register(r"course", CourseViewSet, basename="Course")

urlpatterns = [
    path(
        "course/<int:pk>/subscribe/",
        views.SubscribeSetAPIView.as_view(),
        name="subscribe",
    ),
    path(
        "course/<int:pk>/pay/",
        PaymentGetLinkAPIView.as_view(),
        name="course_pay",
    ),
    path(
        "course/<int:pk>/paystatus/",
        PaymentGetStatusAPIView.as_view(),
        name="course_paystatus",
    ),
    path(
        "lesson/<int:pk>/pay/",
        PaymentGetLinkAPIView.as_view(),
        name="lesson_pay",
    ),
    path(
        "lesson/<int:pk>/paystatus/",
        PaymentGetStatusAPIView.as_view(),
        name="lesson_paystatus",
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
