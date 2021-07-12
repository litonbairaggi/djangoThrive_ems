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
        return reverse_lazy('ems:update_team', kwargs={'pk':id})


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
        return reverse_lazy('ems:create_team')



class DesignationListView(ListView):
    model = Designation 
    template_name = 'ems/show_designation.html'
    context_object_name = 'designations'


class DesignationEditView(UpdateView):
    model = Designation 
    form_class = DesignationForm
    template_name = 'ems/edit_designation.html'
    def get_success_url(self):
        id = self.object.id
        return reverse_lazy('ems:update_team', kwargs={'pk':id})


def destroy(request, id):
    designations = Designation.objects.get(id=id)
    designations.delete()
    return redirect("/ems/show_team")















# Designation crud
@login_required(login_url='/ems/login/')
def createDesignation(request):
    if request.method == "POST":
        form = DesignationForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect(('/ems/show_designation'))
            except:
                pass

    else:
        form = DesignationForm()   
    context = {
        'form': form
    }    
    return render(request, 'ems/create_designation.html', context)    

@login_required(login_url='/ems/login/')
def showDesignation(request):
    designations = Designation.objects.all()
    context = {
        'designations': designations
    }
    return render(request, 'ems/show_designation.html', context)

@login_required(login_url='/ems/login/')
def editDesignation(request, id):
    designations = Designation.objects.get(id=id)
    context = {
        'designations': designations
    }
    return render(request,'ems/edit_designation.html', context)

@login_required(login_url='/ems/login/')
def updateDesignation(request, id):
    designations = Designation.objects.get(id=id)
    form = DesignationForm(request.POST, instance=designations)
    if form.is_valid():
        form.save()
        return redirect("/ems/show_designation/")
    context = {
        'designations': designations
    }    
    return render(request, 'ems/edit_designation.html', context) 

@login_required(login_url='/ems/login/')
def destroyDesignation(request, id):
    designations = Designation.objects.get(id=id)
    designations.delete()
    return redirect("/ems/show_designation")

# Employee curd  

@login_required(login_url='/ems/login/')
def createEmployee(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/ems/show_employee')
            except:
                pass
    else:
        form = EmployeeForm()
    context = {
        'form': form
    }            
    return render(request, 'ems/create_employee.html', context) 

@login_required(login_url='/ems/login/')
def showEmployee(request):
    employees = Employee.objects.all()
    context = {
        'employees': employees
    }
    return render(request, 'ems/show_employee.html', context)

@login_required(login_url='/ems/login/')
def editEmployee(request, id):
    employees = Employee.objects.get(id=id)
    context ={
        'employees': employees
    }
    return render(request, 'ems/edit_employee.html', context)

# @login_required(login_url='/ems/login/')
# def updateEmployee(request, id):
#     employees = Employee.objects.get(id=id)
#     form = EmployeeForm(request.POST, instance=employees)
#     if form.is_valid():
#         form.save()
#         return redirect("/ems/show_employee/")
#     context = {
#         'employees': employees
#     }    
#     return render(request, 'ems/edit_employee.html', context) 

@login_required(login_url='/ems/login/')
def updateEmployee(request, id):
    template = 'ems/edit_employee.html'
    employees = get_object_or_404(Employee, id=id)
    form = EmployeeForm(request.POST or None, instance=employees)
    if form.is_valid():
        form.save()
        return redirect('/ems/show_employee/')
    context = {"employees": employees}
    return render(request, template, context)    



@login_required(login_url='/ems/login/')
def destroyEmployee(request, id):
    employees = Employee.objects.get(id=id)
    employees.delete()
    return redirect("/ems/show_employee")


# attendance CURD
@login_required(login_url='/ems/login/')
def createAttendance(request):
    if request.method == "POST":
        form = AttendanceForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/ems/show_attendance')
            except:
                pass
    else:
        form = AttendanceForm()
    context = {
        'form': form
    }            
    return render(request, 'ems/create_attendance.html', context) 

@login_required(login_url='/ems/login/')
def showAttendance(request):
    attendances = Attendance.objects.all()
    context = {
        'attendances': attendances
    }
    return render(request, 'ems/show_attendance.html', context)

# Payroll curd 


@login_required(login_url='/ems/login/')
def createPayroll(request):
    if request.method == "POST":
        form = PayrollForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/ems/show_payroll')
            except:
                pass
    else:
        form = PayrollForm()
    context = {
        'form': form
    }            
    return render(request, 'ems/create_payroll.html', context) 

@login_required(login_url='/ems/login/')
def showPayroll(request):
    payrolls = Payroll.objects.all()
    context = {
        'payrolls': payrolls
    }
    return render(request, 'ems/show_payroll.html', context)

@login_required(login_url='/ems/login/')
def editPayroll(request, id):
    payrolls = Payroll.objects.get(id=id)
    context ={
        'payrolls': payrolls
    }
    return render(request, 'ems/edit_payroll.html', context)


@login_required(login_url='/ems/login/')
def updatePayroll(request, id):
    payrolls = Payroll.objects.get(id=id)
    form = EmployeeForm(request.POST, instance=payrolls)
    if form.is_valid():
        form.save()
        return redirect("/ems/show_payroll/")
    context = {
        'payrolls': payrolls
    }    
    return render(request, 'ems/edit_payroll.html', context) 

@login_required(login_url='/ems/login/')
def destroyPayroll(request, id):
    payrolls = Payroll.objects.get(id=id)
    payrolls.delete()
    return redirect("/ems/show_payroll")