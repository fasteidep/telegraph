from django import forms
from .models import *

class NameForm(forms.Form):
    # choices : None
    
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.choices = [(i.name,i.name ) for i in Okrug.objects.all()]
    
    selector = forms.ChoiceField()
    dd = forms.EmailField()
    
    
class AddOkrug(forms.Form):
    name = forms.CharField(max_length=100)