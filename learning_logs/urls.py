"""Defines URL patterns for learning_logs."""

from django.conf.urls import url
from django.urls import path

from learning_logs.models import Topic

from . import views

app_name = "learning_logs"
urlpatterns = [
    # Home Page
    path('', views.index, name="index"),
    # page that shows all topics.
    path('topics/', views.topics, name='topics'),
    # detail page for a single topic.
    path('topics/<int:topic_id>/', views.topic, name="topic"),
    # Page for adding a new topic.
    path('new_topic/', views.new_topic, name='new_topic'),
    # Page for adding new entry
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # Page for editing an entry. 
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]