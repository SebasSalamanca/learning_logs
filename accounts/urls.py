"""Defines the url patterns for accounts"""

#Include for modules that Django has predefined
from django.urls import path, include 

app_name = 'accounts'
urlpatterns = [
    #include default auth urls. 
    path('', include('django.contrib.auth.urls')),
]
