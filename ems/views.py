from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import View

from . models import Employee, Team, Designation, Employee, Attendance, Payroll
from . froms import TeamForm, DesignationForm, EmployeeForm, AttendanceForm, PayrollForm, CreateUserForm

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user

from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,

)
# Create your views here.

@unauthenticated_user
def registerPage(request):
  
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for '+user)
            return redirect('ems/login/')
    context = {
        'form':form
    }
    return render(request, 'ems/register.html', context)

@unauthenticated_user
def loginPage(request):   
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/ems/show_employee/')
        else:
            messages.info(request, 'Username OR password is incorrect') 

    context = {}
    return render(request, 'ems/login.html', context)


def logoutUser(request):
	logout(request)
	return redirect('/ems/login/')


# Team views    

class TeamCreateView(CreateView):
    model = Team 
    form_class = TeamForm 
    template_name = 'ems/create_team.html'
    def form_invalid(self, form):
        form.instance.user = self.request.user
        return super().form_invalid(form)
    def get_success_url(self):
        return reverse_lazy('ems:create_team')


class TeamListView(ListView):
    model = Team 
    template_name = 'ems/show_team.html'
    context_object_name = 'teams'


class TeamEditView(UpdateView):
    model = Team 
    form_class = TeamForm
    template_name = 'ems/edit_team.html'
    def get_success_url(self):
        id = self.object.id
        return reverse_lazy('ems:show_team')


def destroy(request, id):
    teams = Team.objects.get(id=id)
    teams.delete()
    return redirect("/ems/show_team")



# Designation CRUD
class DesignationCreateView(CreateView):
    model = Designation 
    form_class = DesignationForm 
    template_name = 'ems/create_designation.html'
    def form_invalid(self, form):
        form.instance.user = self.request.user
        return super().form_invalid(form)
    def get_success_url(self):
        return reverse_lazy('ems:create_designation')



class DesignationListView(ListView):
    model = Designation 
    template_name = 'ems/show_designation.html'
    context_object_name = 'designations'


class DesignationEditView(UpdateView):
    model = Designation 
    form_class = DesignationForm
    template_name = 'ems/edit_designation.html'
    def get_success_url(self):
        return reverse_lazy('ems:show_designation')


def destroyDesignation(request, id):
    designations = Designation.objects.get(id=id)
    designations.delete()
    return redirect("/ems/show_designation")




# Employee CRUD
class EmployeeCreateView(CreateView):
    model = Employee 
    form_class = EmployeeForm 
    template_name = 'ems/create_employee.html'
    def form_invalid(self, form):
        form.instance.user = self.request.user
        return super().form_invalid(form)
    def get_success_url(self):
        return reverse_lazy('ems:create_employee')

class EmployeeListView(ListView):
    model = Employee 
    template_name = 'ems/show_employee.html'
    context_object_name = 'employees'

class EmployeeEditView(UpdateView):
    model = Employee 
    form_class = EmployeeForm
    template_name = 'ems/edit_employee.html'
    def get_success_url(self):
        return reverse_lazy('ems:show_employee')

def destroyEmployee(request, id):
    employees = Employee.objects.get(id=id)
    employees.delete()
    return redirect("/ems/show_employee")

# Attendance CRUD
class AttendanceCreateView(CreateView):
    model = Attendance 
    form_class = AttendanceForm 
    template_name = 'ems/create_attendance.html'
    def form_invalid(self, form):
        form.instance.user = self.request.user
        return super().form_invalid(form)
    def get_success_url(self):
        return reverse_lazy('ems:create_attendance')

class AttendanceListView(ListView):
    model = Attendance 
    template_name = 'ems/show_attendance.html'
    context_object_name = 'attendances'


# Payroll CRUD
class PayrollCreateView(CreateView):
    model = Payroll 
    form_class = PayrollForm 
    template_name = 'ems/create_payroll.html'
    def form_invalid(self, form):
        form.instance.user = self.request.user
        return super().form_invalid(form)
    def get_success_url(self):
        return reverse_lazy('ems:create_payroll')

class PayrollListView(ListView):
    model = Payroll 
    template_name = 'ems/show_payroll.html'
    context_object_name = 'payrolls'

class PayrollEditView(UpdateView):
    model = Payroll 
    form_class = PayrollForm
    template_name = 'ems/edit_payroll.html'
    def get_success_url(self):
        return reverse_lazy('ems:show_payroll')

@login_required(login_url='/ems/login/')
def destroyPayroll(request, id):
    payrolls = Payroll.objects.get(id=id)
    payrolls.delete()
    return redirect("/ems/show_payroll")

