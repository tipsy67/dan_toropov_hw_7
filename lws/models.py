from django.db import models

from users.models import NULLABLE


class Lesson(models.Model):
    name = models.CharField(max_length=50, verbose_name="имя")
    description = models.TextField(**NULLABLE, verbose_name="описание")
    preview = models.ImageField(**NULLABLE, verbose_name="превью")
    video_url = models.URLField(**NULLABLE, verbose_name="ссылка")

    def __str__(self):
        return f"Lesson:{self.name}"

    class Meta:
        verbose_name = "урок"
        verbose_name_plural = "уроки"


class Course(models.Model):
    name = models.CharField(max_length=50, verbose_name="имя")
    description = models.TextField(**NULLABLE, verbose_name="описание")
    preview = models.ImageField(**NULLABLE, verbose_name="превью")
    lessons = models.ManyToManyField(
        to="Lesson", blank=True, related_name="courses", verbose_name="уроки"
    )

    def __str__(self):
        return f"Course:{self.name}"

    class Meta:
        verbose_name = "урок"
        verbose_name_plural = "уроки"
