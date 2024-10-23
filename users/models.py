from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

NULLABLE = {'null':True, 'blank':True}

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')
    avatar = models.ImageField(upload_to='users/', **NULLABLE, verbose_name='аватар')
    phone = models.CharField(max_length=30, **NULLABLE, verbose_name='телефон')
    town = models.CharField(max_length=50, **NULLABLE, verbose_name='город')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
