from django import forms
from django.db import models
from django.db.models.base import Model
from django.forms import fields, widgets
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . models import Team, Designation, Employee, Attendance, Payroll


class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']  

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
    class Meta:
        model = Employee
        fields = ['id', 'employee_name', 'employee_email', 'team', 'designation', 'employee_phone', 'gender', 'address', 'salary']

        widgets = {
            'employee_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Name'}),
            'employee_email':forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email'}),
            'team':forms.Select(attrs={'class':'form-control'}),
            'designation':forms.Select(attrs={'class':'form-control'}),
            'employee_phone':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Phone'}),
            'gender':forms.Select(attrs={'class':'form-control'}),
            'address':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Address'}),
            'salary':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Salary'})
        }
        labels={
            'employee_name':'Employee Name name',
            'employee_email':'Employee Email',
            'team':'Employee Team',
            'designation':'Employee Designation',
            'employee_phone':'Employee Phone',
            'gender':'Gender',
            'address':'Employee Address',
            'salary':'Salary',
        }


class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['id', 'employee', 'created_entry', 'created_exit']
        widgets = {
            'employee':forms.Select(attrs={'class':'form-control'}),
            'created_entry':forms.DateTimeInput(attrs={'type': 'datetime-local', 'class':'form-control'}),
            'created_exit':forms.DateTimeInput(attrs={'type': 'datetime-local', 'class':'form-control'}),
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


      