import uuid

from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=144)
    username = models.CharField(max_length=150)
    pid = models.CharField(max_length=50, default=uuid.uuid4())

    def __str__(self):
        return f"{self.user}"
