from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    def __str__(self):
        return f"{self.id} {self.username}"
    
# Provide unique related_name for groups and user_permissions
User._meta.get_field('groups').remote_field.related_name = 'cairocoinplus_user_groups'
User._meta.get_field('user_permissions').remote_field.related_name = 'cairocoinplus_user_permissions'