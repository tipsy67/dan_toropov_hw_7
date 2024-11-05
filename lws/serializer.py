from rest_framework import serializers

from lws.models import Course, Lesson
from lws.validators import URLCustomValidator


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = "__all__"
        validators = [
            URLCustomValidator(field="video_url")
        ]


class CourseSerializer(serializers.ModelSerializer):

    number_of_lessons = serializers.SerializerMethodField()
    lessons = LessonSerializer(many=True)

    class Meta:
        model = Course
        fields = "__all__"
        validators = [
            URLCustomValidator(field="video_url")
        ]

    def get_number_of_lessons(self, obj):
        return obj.lessons.all().count()
