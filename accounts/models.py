from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

class UserType(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()

    def __str__(self):
        return self.name

class Language(models.Model):
    key = models.CharField(max_length=4)
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class CustomUser(AbstractUser):
    user_type = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None
        
        
    ) 
    preffered_language = models.ForeignKey(
        Language,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None
    )
