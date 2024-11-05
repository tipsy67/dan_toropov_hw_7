from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework import status
from lws.models import Course, Lesson
from users.models import User


class LessonTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="dtoropov@yandex.ru")
        self.course = Course.objects.create(name="Alchemy")
        self.lesson = Lesson.objects.create(
            name="Getting gold", owner=self.user, course=self.course
        )
        self.client.force_authenticate(user=self.user)
        self.etalon_data = [
            {
                "id": self.lesson.pk,
                "name": "Getting gold",
                "description": None,
                "preview": None,
                "video_url": None,
                "course": self.course.pk,
                "owner": self.user.pk,
            }
        ]

    def test_lesson_list(self):
        url = reverse("lws:lesson_list")
        response = self.client.get(url)
        response_data = response.json().get("results")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response_data, self.etalon_data)

    def test_lesson_view(self):
        url = reverse("lws:lesson_view", args=(self.lesson.pk,))
        response = self.client.get(url)
        response_data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response_data, self.etalon_data[0])

    def test_lesson_update(self):
        url = reverse("lws:lesson_update", args=(self.lesson.pk,))
        data = {"name": "Getting immortality pill"}
        response = self.client.patch(url, data)
        response_data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response_data.get("name"), "Getting immortality pill")

    def test_lesson_create(self):
        url = reverse("lws:lesson_create")
        data = {"name": "Getting immortality pill"}
        response = self.client.post(url, data)
        response_data = response.json()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(Lesson.objects.all().count(), 2)

    def test_lesson_destroy(self):
        url = reverse("lws:lesson_delete", args=(self.lesson.pk,))
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        self.assertEqual(Lesson.objects.all().count(), 0)

    def test_course_subscribe(self):
        url = reverse("lws:subscribe", args=(self.course.pk,))
        response = self.client.post(url)
        self.assertEqual(
            self.course.subscriptions.all().exists(), True
        )
        response = self.client.post(url)
        self.assertEqual(
            self.course.subscriptions.all().first().is_active, False
        )
        response = self.client.post(url)
        self.assertEqual(
            self.course.subscriptions.all().first().is_active, True
        )
