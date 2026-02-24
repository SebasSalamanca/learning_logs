from django import forms

from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    """Meta class is an inner class you put inside your models or forms to provide 
    metadata, basically configuration options that describe the behavior of the model
    or form without being a database field itself. 
    Here are some extra instructions about how to handle this model."""
    class Meta:
        model = Topic
        #fields = ['text']
        fields = '__all__'
        labels = {'text': ''}

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text'] #Show the text item 
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}