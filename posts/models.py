"""Posts models."""

# Django
from django.db import models

# Create your models here.

class User(models.Model):

    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    is_admin = models.BooleanField(default=False)
    bio = models.TextField(blank=True)
    birthdate  = models.DateField(blank=True, null=True)

    # When an insntance is creted automatically will be create 
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        """Return email"""
        return self.email