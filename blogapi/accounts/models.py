from django.contrib.auth.models import AbstractUser # type: ignore
from django.db import models # type: ignore


# Create your models here.
class CustomUser(AbstractUser):
    name=models.CharField(null=True, blank=True, max_length=100)