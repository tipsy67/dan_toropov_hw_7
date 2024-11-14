from datetime import timedelta
from django.conf import settings
from django.core.mail import send_mail
from celery import shared_task
from django.utils import timezone

from lws.models import Subscribe, Course
from users.models import User


def deactivate_from_list_users(list_users):
    for user in list_users:
        user.is_active = False
        user.save()


@shared_task
def deactivate_old_users():
    list_users = User.objects.filter(
        is_active=True,
        last_login__isnull=True,
        date_joined__lt=timezone.now() - timedelta(days=30),
    )
    deactivate_from_list_users(list_users)
    list_users = User.objects.filter(
        is_active=True,
        last_login__lt=timezone.now() - timedelta(days=30),
    )
    deactivate_from_list_users(list_users)


@shared_task
def sendmail_for_subscribers(pk):
    obj = Course.objects.filter(pk=pk).first()
    obj_list = Subscribe.objects.filter(course=obj)
    email_list = [x.user.email for x in obj_list]
    send_mail(
        "Внимание",
        f"Уважаемый пользователь, обновились материалы на курсе {obj.name}",
        settings.EMAIL_HOST_USER,
        email_list,
    )
