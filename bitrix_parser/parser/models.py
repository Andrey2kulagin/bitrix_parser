from django.db import models

from datetime import datetime, timedelta

# Create your models here.
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    choices = (('Активна', 'Активна'),
               ('Не активна', 'Не активна'),)
    subscription = models.CharField(verbose_name="Статус подписки", max_length=50, choices=choices,
                                    default="Не активна", null=True)
    activation_date = models.DateField(verbose_name="Дата активации подписки", null=True)
    subscription_days = models.PositiveIntegerField(verbose_name="Длина подписки(дней)", null=True)
    end_of_subscription = models.DateField(verbose_name="Дата истечения подписки", null=True, blank=True)


