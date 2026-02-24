#Render the response based on the data provided by views 
from django.shortcuts import render

from .models import Topic

# Create your views here.
"""A view function takes in information from a request, prepares the data needed to generate a page, 
and then sends the data back to the browser. """

def index(request):
    """The home page for learning log"""
    return render(request, 'learning_logs/index.html')


def topics(request):
    """Show all topics"""
    topics = Topic.objects.order_by("date_added")
    context = {"topics": topics}
    return render(request, 'learning_logs/topics.html', context)