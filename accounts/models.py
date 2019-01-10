from django.db import models
from django.contrib.auth.models import User


class Account(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)
