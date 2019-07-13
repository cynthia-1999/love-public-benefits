from django.db import models

# Create your models here.
from django.db import models


class User(models.Model):
    user_id = models.CharField(max_length=25, unique=True)
    user_name = models.CharField(max_length=12, primary_key=True, unique=True)
    user_passwd = models.CharField(max_length=16)
    user_telenumb = models.CharField(max_length=11)

    def __str__(self):
        return self.user_name

2