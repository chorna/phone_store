from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.utils import timezone


class CustomUserManager(UserManager):
    pass


class Employees(AbstractUser):
    # Campos adicionales que deseas agregar
    date_of_birth = models.DateField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)

    # Sobrecarga el UserManager
    objects = CustomUserManager()

    def __str__(self):
        return self.username
