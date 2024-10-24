from django.contrib import admin

from lws.models import Course, Lesson


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    pass


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    pass
