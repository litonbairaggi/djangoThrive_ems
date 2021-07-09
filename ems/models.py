from django.db import models
from django.db.models.fields import CharField
from django.utils.timezone import now

# Create your models here.

class Team(models.Model):
    team_name = models.CharField(max_length=120, unique=True, blank=False)
    def __str__(self):
        return self.team_name

class Designation(models.Model):
    designation_name = models.CharField(max_length=120, unique=True, blank=False)
    created_date = models.DateTimeField(default=now)
    def __str__(self):
        return self.designation_name

class Employee(models.Model):
    GENDER=(
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )
    employee_name = models.CharField(max_length=120, unique=True, blank=False)
    employee_email = models.EmailField(max_length=64, unique=True, blank=False)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, blank=False)
    designation = models.ForeignKey(Designation, on_delete=models.CASCADE, blank=False)
    employee_phone = models.CharField(max_length=32, unique=True, blank=False)
    gender = models.CharField(max_length=100, choices=GENDER) 
    address = models.CharField(max_length=120, blank=True)
    salary = models.PositiveIntegerField(default=0)
    created_date = models.DateTimeField(default=now)

    def __str__(self):
        return self.employee_name

class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, blank=False)
    created_entry = models.DateTimeField(default=now)
    created_exit = models.DateTimeField(default=now)

    def __str__(self):
        return self.employee.employee_name

class Payroll(models.Model):
    payroll_employee = models.ForeignKey(Employee, on_delete=models.CASCADE, blank=False)
    bank_name = models.CharField(max_length=120, blank=False)
    account_no = models.CharField(max_length=32, blank=False)
    created_date = models.DateTimeField(default=now)
    def __str__(self):
        return self.payroll_employee.employee_name
