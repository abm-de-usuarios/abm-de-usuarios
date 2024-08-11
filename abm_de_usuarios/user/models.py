from django.db import models
from group.models import Group
from role.models import Role
class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=150, blank=False)
    last_name = models.CharField(max_length=150, blank=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    roles = models.ManyToManyField(Role, related_name='users')
    groups = models.ManyToManyField(Group, related_name='users')

    def __str__(self):
        return self.username
