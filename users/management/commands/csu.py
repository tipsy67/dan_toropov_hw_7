from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        newsu = User(email="dtoropov@yandex.ru", is_staff=True, is_superuser=True)
        newsu.set_password("Negoro123")

        newsu.save()
