from datetime import datetime
from django.db import models
from django.utils import timezone


class Person(models.Model):
    username = models.CharField(max_length=50, unique=True)
    code = models.IntegerField()
    u_id = models.CharField(max_length=255, blank=True)
    token_fcm = models.CharField(max_length=255, blank=True)
    avatar_name = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.username


class PersonMessage(models.Model):
    sender_username = models.CharField(max_length=50)
    receiver_username = models.CharField(max_length=50)
    sender_code = models.CharField(max_length=50)
    receiver_code = models.CharField(max_length=50)
    created_date = models.DateTimeField(default=timezone.now)
    message = models.TextField()
    image = models.ImageField(upload_to="media/images/%y/%m/%d/", blank=True)

    def __str__(self):
        return self.sender_username
