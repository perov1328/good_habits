from django.db import models
from django.contrib.auth.models import AbstractUser

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    """
    Модель для пользователя
    """
    username = None

    email = models.EmailField(unique=True, verbose_name='Email')

    phone = models.CharField(max_length=35, verbose_name='Номер телефона', **NULLABLE)
    city = models.CharField(max_length=100, verbose_name='Город', **NULLABLE)
    tg_name = models.CharField(max_length=100, verbose_name='Ник в телеграме')
    tg_id = models.IntegerField(unique=True, verbose_name='ID телеграме', default=None, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
