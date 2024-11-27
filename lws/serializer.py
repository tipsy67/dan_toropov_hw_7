from rest_framework import serializers

from lws.models import Course, Lesson
from lws.validators import URLCustomValidator


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = "__all__"
        validators = [URLCustomValidator(field="video_url")]


class CourseSerializer(serializers.ModelSerializer):

    current_user_is_subscriber = serializers.SerializerMethodField(read_only=True)
    number_of_lessons = serializers.SerializerMethodField(read_only=True)
    lessons = LessonSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = "__all__"
        validators = [URLCustomValidator(field="video_url")]

    def get_number_of_lessons(self, obj):
        return obj.lessons.all().count()

    def get_current_user_is_subscriber(self, obj):
        user = self.context["request"].user
        subscribe = obj.subscriptions.filter(user=user).first()
        if subscribe is None or not subscribe.is_active:
            return False
        return True
