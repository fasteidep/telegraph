from django import forms
from .models import *

class NameForm(forms.Form):

    selector = forms.ChoiceField()
    dd = forms.EmailField()
    
    
class AddOkrug(forms.Form):
    name = forms.CharField(max_length=100)
    

class ContactForm(forms.Form):
    name = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)
