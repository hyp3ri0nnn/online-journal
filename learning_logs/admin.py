from django.contrib import admin
from django.contrib.auth.models import User

# Register your models here.
from .models import Entry, Topic


admin.site.register(Topic)
admin.site.register(Entry)
