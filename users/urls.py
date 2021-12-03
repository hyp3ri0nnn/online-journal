"""Defines URL pattern for users."""

from django.urls import path, include

from . import views

app_name = 'users'
urlpatterns = [
    # Include default auth urls.
    path('', include('django.contrib.auth.urls')),
    # Registration page
    path('register/', views.register, name='register'),
    path('profile/<int:user_id>/', views.user_profile, name='profile'),
    path('create/', views.create_profile, name="create_profile"),
]