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
    salary = models.FloatField(default=0)
    created_date = models.DateTimeField(default=now)

    # def __str__(self):
    #     return '{}{}'.format(self.employee_name, self.salary)

    def __str__(self):
        return self.employee_name 

    # def __float__(self):
    #     return 500.0
        

class Attendance(models.Model):
    ATTENDANCE=(
        ('Present ','present '),
        ('Absent','absent'),
    )
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, blank=False)
    attendance = models.CharField(max_length=100, choices=ATTENDANCE)
    created_date = models.DateTimeField(default=now) 

    def __str__(self):
        return self.employee.employee_name

class Payroll(models.Model):
    payroll_employee = models.ForeignKey(Employee, related_name='payroll_employee', on_delete=models.CASCADE, blank=False)
    bank_name = models.CharField(max_length=120, blank=False)
    account_no = models.CharField(max_length=32, blank=False)
    created_date = models.DateTimeField(default=now)

    

