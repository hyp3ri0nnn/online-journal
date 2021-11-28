from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    about = models.TextField(max_length=500)
    date_created = models.DateTimeField(auto_now = False, auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True, auto_now_add=False)
    image = models.ImageField()

    def __str__(self):
        return self.name
