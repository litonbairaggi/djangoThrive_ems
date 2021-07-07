from django import forms
from django.forms import widgets

from . models import Team

class TeamForm(forms.ModelForm):  
    class Meta:  
        model = Team  
        fields = "__all__" 
         
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Team Name'}),
        }