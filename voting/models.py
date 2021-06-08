from django.db import models
from django.contrib.auth.models import User


class Poll(models.Model):
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=1024, blank=True, null=True)
    active = models.BooleanField(default=True)
    expiretion_date = models.DateField()
    assigned_users = models.ManyToManyField(User, blank=True, null=True)


class Option(models.Model):
    title = models.CharField(max_length=128)
    count = models.IntegerField()
    is_correct = models.BooleanField(default=False, blank=True, null=True)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name='options')
