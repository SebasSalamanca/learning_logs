#Render the response based on the data provided by views 
from django.shortcuts import render

# Create your views here.
"""A view function takes in information from a request, prepares the data needed to generate a page, 
and then sends the data back to the browser. """

def index(request):
    """The home page for learning log"""
    return render(request, 'learning_logs/index.html')


