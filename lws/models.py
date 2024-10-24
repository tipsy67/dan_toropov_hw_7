from django.db import models

from users.models import NULLABLE

class Lesson(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(**NULLABLE)


class Course(models.Model):
    name = models.CharField(max_length=50, verbose_name='')
    description = models.TextField(**NULLABLE)
    preview = models.ImageField(**NULLABLE)
    lessons = models.ManyToManyField(to='Lesson', related_name='courses')