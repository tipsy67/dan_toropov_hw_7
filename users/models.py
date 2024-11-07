from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

NULLABLE = {"null": True, "blank": True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="почта")
    avatar = models.ImageField(upload_to="users/", **NULLABLE, verbose_name="аватар")
    phone = models.CharField(max_length=30, **NULLABLE, verbose_name="телефон")
    town = models.CharField(max_length=50, **NULLABLE, verbose_name="город")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"

    @property
    def is_moderator(self):
        if (
            self.has_perm("lws.view_course")
            and self.has_perm("lws.change_course")
            and not self.has_perm("lws.add_course")
            and not self.has_perm("lws.delete_course")
        ) or self.groups.filter(name="moders").exists():
            return True

        return False


class Payment(models.Model):
    PAYMENT_METHOD = {"CASH": "наличные", "CARD": "безналичные"}
    user = models.ForeignKey(
        to="User",
        on_delete=models.CASCADE,
        related_name="payments",
        verbose_name="пользователь",
        **NULLABLE
    )
    date_of_payment = models.DateTimeField(**NULLABLE, verbose_name="дата оплаты")
    course = models.ForeignKey(
        to="lws.Course",
        on_delete=models.SET_NULL,
        **NULLABLE,
        related_name="payments",
        verbose_name="курс"
    )
    lesson = models.ForeignKey(
        to="lws.Lesson",
        on_delete=models.SET_NULL,
        **NULLABLE,
        related_name="payments",
        verbose_name="урок"
    )
    cost = models.DecimalField(
        max_digits=10, decimal_places=2, default=0, verbose_name="сумма"
    )
    payment_method = models.CharField(max_length=4, choices=PAYMENT_METHOD, **NULLABLE)
    payment_id = models.CharField(max_length=255, **NULLABLE)
    payment_link = models.URLField(max_length=400, **NULLABLE)

    class Meta:
        verbose_name = "платеж"
        verbose_name_plural = "платежи"
