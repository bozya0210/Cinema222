from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    name = models.CharField(max_length=100)
    role_choices = [
        ('admin', 'Администратор'),
        ('user', 'Пользователь')
    ]
    role = models.CharField(max_length=20, choices=role_choices)
    groups = models.ManyToManyField(Group, related_name='custom_user_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_permissions')

    def __str__(self):
        return self.name
