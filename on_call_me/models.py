from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    role = models.CharField(max_length=20)


class OnCallPeriod(models.Model):
    team_member = models.ForeignKey(User, on_delete=models.CASCADE)
    week_ending = models.DateField('week ending')
    start_date = models.DateField('start date')
    end_date = models.DateField('end date')
    days = models.IntegerField(default=0)
