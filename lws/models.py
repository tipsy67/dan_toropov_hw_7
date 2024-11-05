from django.db import models

from users.models import NULLABLE


class Lesson(models.Model):
    name = models.CharField(max_length=50, verbose_name="имя")
    description = models.TextField(**NULLABLE, verbose_name="описание")
    preview = models.ImageField(**NULLABLE, verbose_name="превью")
    video_url = models.URLField(**NULLABLE, verbose_name="ссылка")
    course = models.ForeignKey(
        to="Course",
        on_delete=models.SET_NULL,
        **NULLABLE,
        related_name="lessons",
        verbose_name="уроки",
    )
    owner = models.ForeignKey(to="users.User", on_delete=models.SET_NULL, **NULLABLE)

    def __str__(self):
        return f"Lesson:{self.name}"

    class Meta:
        verbose_name = "урок"
        verbose_name_plural = "уроки"


class Course(models.Model):
    name = models.CharField(max_length=50, verbose_name="имя")
    description = models.TextField(**NULLABLE, verbose_name="описание")
    preview = models.ImageField(**NULLABLE, verbose_name="превью")
    owner = models.ForeignKey(to="users.User", on_delete=models.SET_NULL, **NULLABLE)
    video_url = models.URLField(**NULLABLE, verbose_name="ссылка")

    def __str__(self):
        return f"Course:{self.name}"

    class Meta:
        verbose_name = "курс"
        verbose_name_plural = "курсы"


class Subscribe(models.Model):
    course = models.ForeignKey(
        to="Course",
        related_name="subscriptions",
        on_delete=models.CASCADE,
        verbose_name="курс",
    )
    user = models.ForeignKey(
        to="users.User",
        related_name="subscriptions",
        on_delete=models.CASCADE,
        verbose_name="пользователь",
    )
    is_active = models.BooleanField(verbose_name="активность")

    class Meta:
        verbose_name = "подписка"
        verbose_name_plural = "подписки"
