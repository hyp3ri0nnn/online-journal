from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.db.models.fields.files import ImageField
from django.forms.models import ModelForm
from django.http import request
from django.views.generic import ListView, DetailView
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=CASCADE)

# class Profile(models.Model):
#     username = models.TextField(max_length=50)
#     image = models.ImageField()
#     username = models.TextField(max_length=100)
#     about = models.TextField(max_length=500)
#     date_created = models.DateTimeField(auto_now = False, auto_now_add=True)
#     last_online = models.DateTimeField(auto_now=True, auto_now_add=False)
#     profile_id = models.OneToOneField(User, on_delete=CASCADE)

#     def __str__(self):
#         return self.username


# class Profile(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)

#     name = user.name
#     about = models.TextField(max_length=500)
#     date_created = models.DateTimeField(auto_now = False, auto_now_add=True)
#     last_login = models.DateTimeField(auto_now=True, auto_now_add=False)
#     image = models.ImageField()

#     def __str__(self):
#         return self.name


