"""Defines the url patterns for accounts"""

#Include for modules that Django has predefined
from django.urls import path, include 

from . import views

app_name = 'accounts'
urlpatterns = [
    #include default auth urls. 
    path('', include('django.contrib.auth.urls')),
    #Registration page 
    path('register/', views.register, name = 'register'),
    path('confirmation_sent/', views.confirmation_sent, name='confirmation_sent'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
]
