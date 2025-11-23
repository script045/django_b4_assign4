from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = [
        ("admin", "Admin"),
        ("donor", "Donor"),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default="donor")

    # Fix reverse accessor clash
    groups = models.ManyToManyField(Group, related_name="custom_users", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="custom_user_permissions", blank=True)
    
    def __str__(self):
        return f"{self.username} ({self.role})"