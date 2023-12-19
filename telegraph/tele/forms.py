from django import forms
from .models import *



class PostForm(forms.ModelForm):
    title = forms.CharField(max_length=128,widget=forms.TextInput(attrs = {"type":"text", "class":"form-control bg-dark", "maxlength":"128", "style":"border-color: rgb(60, 65, 68); background-color: rgb(44, 47, 49) !important; color: rgb(181, 175, 166);"}))
    body = forms.TextInput()
 
    class Meta:
        model = Article
        fields = ('title', 'body', )
 
      