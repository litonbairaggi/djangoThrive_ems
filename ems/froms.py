from django import forms
from django.db.models.base import Model
from django.forms import fields, widgets

from . models import Team, Designation

class TeamForm(forms.ModelForm):  
    class Meta:  
        model = Team  
        fields = "__all__" 
         
        widgets={
            'team_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Team Name'}),
        }

class DesignationForm(forms.ModelForm):
    class Meta:
        model = Designation
        fields = ['id', 'designation_name']

        widgets = {
            'designation_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Designation Name'}),
        }