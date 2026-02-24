"""Defines URL patterns for learning_logs"""

from django.urls import path #This library is useful to mapping urls with the views. 
from . import views

app_name = 'learning_logs'
urlpatterns = [
    #Home page
    path('', views.index, name = 'index'),
    #Page that shows all Topics
    path('topics/', views.topics, name = 'topics'),
    #Detail page for a single topic
    path('topics/<int:topic_id>/', views.topic, name = 'topic')
]
