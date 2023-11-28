from django import forms
from .models import *


    

class ContactForm(forms.Form):
    name = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)


class PostForm(forms.ModelForm):
    title = forms.CharField(max_length=128)
    body = forms.TextInput()
 
    class Meta:
        model = Article
        fields = ('title', 'body', )
 
      