from django.db import models

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
#     bio = models.TextField(blank=True, null=True)
#     location = models.CharField(max_length=100, blank=True, null=True)
#     birth_date = models.DateField(blank=True, null=True)

#     def __str__(self):
#         return self.user.username
