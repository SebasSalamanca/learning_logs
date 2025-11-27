from django.db import models

#A models tells django how to work with the data that will be stored in the app. 
class Topic(models.Model):
    """A topic the user is learning about"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string represetation of the model."""
        return self.text