from django.db import models

# Create your models here.


class Topic(models.Model):
    """A topic the user is learning about"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        """Return a string representation of the model"""
        return self.text
    

class Entry(models.Model):
    """This is the code that connects each entry to a specific topic"""
    """Something specific learning about a topic"""
    topic = models.ForeignKey(Topic, on_delete = models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self): ##How the admin user will represent a string. 
        """Return a simple string representing the entry"""
        return f"{self.text[:50]}..."