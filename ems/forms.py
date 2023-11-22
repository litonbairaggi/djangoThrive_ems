from django import forms
from django.db import models
from django.db.models.base import Model
from django.forms import fields, widgets
from .models import Team, Designation, Employee, Attendance, Payroll


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

class EmployeeForm(forms.ModelForm):
    employee_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Name'}))
    employee_email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Valid Email'}))
    team = forms.ModelChoiceField(Team.objects.all(),required=True, empty_label='Select a team',widget=forms.Select(attrs={'class':'form-control'}))
    designation = forms.ModelChoiceField(Designation.objects.all(),required=True, empty_label='Select a designation',widget=forms.Select(attrs={'class':'form-control'}))
    employee_phone = forms.CharField(strip=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Mobile Number'}))
    gender = forms.ChoiceField(choices=Employee.GENDER, widget=forms.Select(attrs={'class':'form-control'}))
    address = forms.CharField(strip=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Address'}))
    # employee_img = forms.ImageField(widget=forms.FileInput(attrs={'class':'form-control'}))
    employee_img = forms.ImageField(label='Image',required=True,widget=forms.FileInput(attrs={'class':'form-control mt-2'}))
    # employee_img = forms.ImageField(label=('Employee img'),required=False, error_messages = {'invalid':("Image files only")})
    
    class Meta:
        model = Employee
        fields = ['id', 'employee_name', 'employee_email', 'team', 'designation', 'employee_phone', 'gender', 'address', 'salary', 'employee_img']
        widgets = {
            'salary':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Salary'}),
        }
        def __init__(self, *args, **kwargs):
            super(EmployeeForm, self).__init__(*args, **kwargs)
            self.fields['image'].required = False
        # labels={
        #     'employee_name':'Employee Name name',
        #     'employee_email':'Employee Email',
        #     'team':'Employee Team',
        #     'designation':'Employee Designation',
        #     'employee_phone':'Employee Phone',
        #     'gender':'Gender',
        #     'address':'Employee Address',
        #     'salary':'Salary',
        # }


class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['id', 'employee', 'attendance']
        widgets = {
            'employee':forms.Select(attrs={'class':'form-control'}),
            'attendance':forms.Select(attrs={'class':'form-control'}),
        }

class PayrollForm(forms.ModelForm):
    class Meta:
        model = Payroll
        fields = ['id', 'payroll_employee', 'bank_name', 'account_no']
        widgets = {
            'payroll_employee':forms.Select(attrs={'class':'form-control'}),
            'bank_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Bank Name'}),
            'account_no':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Account No'}),
        }