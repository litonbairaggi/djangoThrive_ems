from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import View

from . models import Employee, Team, Designation, Employee, Attendance, Payroll
from . froms import TeamForm, DesignationForm, EmployeeForm, AttendanceForm, PayrollForm

from django.contrib.auth.decorators import login_required


from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
)
# Create your views here.

# @login_required(login_url='login')
class TeamCreateView(CreateView):
    model = Team 
    form_class = TeamForm 
    template_name = 'ems/create_team.html'
    def form_invalid(self, form):
        form.instance.user = self.request.user
        return super().form_invalid(form)
    def get_success_url(self):
        return reverse_lazy('ems:show_team')

# @login_required(login_url='login')
class TeamListView(ListView):
    model = Team 
    template_name = 'ems/show_team.html'
    context_object_name = 'teams'


# @login_required(login_url='login')
class TeamEditView(UpdateView):
    model = Team 
    form_class = TeamForm
    template_name = 'ems/edit_team.html'
    def get_success_url(self):
        id = self.object.id
        return reverse_lazy('ems:show_team')

@login_required(login_url='/session/login')
def destroy(request, id):
    teams = Team.objects.get(id=id)
    teams.delete()
    return redirect("/ems/show_team")



# Designation CRUD
# @login_required(login_url='login')
class DesignationCreateView(CreateView):
    model = Designation 
    form_class = DesignationForm 
    template_name = 'ems/create_designation.html'
    def form_invalid(self, form):
        form.instance.user = self.request.user
        return super().form_invalid(form)
    def get_success_url(self):
        return reverse_lazy('ems:show_designation')


# @login_required(login_url='login')
class DesignationListView(ListView):
    model = Designation 
    template_name = 'ems/show_designation.html'
    context_object_name = 'designations'


# @login_required(login_url='login')
class DesignationEditView(UpdateView):
    model = Designation 
    form_class = DesignationForm
    template_name = 'ems/edit_designation.html'
    def get_success_url(self):
        return reverse_lazy('ems:show_designation')


# @login_required(login_url='login')
def destroyDesignation(request, id):
    designations = Designation.objects.get(id=id)
    designations.delete()
    return redirect("/ems/show_designation")




# Employee CRUD
# @login_required(login_url='login')
class EmployeeCreateView(CreateView):
    model = Employee 
    form_class = EmployeeForm 
    template_name = 'ems/create_employee.html'
    def form_invalid(self, form):
        form.instance.user = self.request.user
        return super().form_invalid(form)
    def get_success_url(self):
        return reverse_lazy('ems:show_employee')

# @login_required(login_url='login')
class EmployeeListView(ListView):
    model = Employee 
    template_name = 'ems/show_employee.html'
    context_object_name = 'employees'

# @login_required(login_url='login')
class EmployeeEditView(UpdateView):
    model = Employee 
    form_class = EmployeeForm
    template_name = 'ems/edit_employee.html'
    def get_success_url(self):
        return reverse_lazy('ems:show_employee')

# @login_required(login_url='login')
def destroyEmployee(request, id):
    employees = Employee.objects.get(id=id)
    employees.delete()
    return redirect("/ems/show_employee")

# Attendance CRUD
# @login_required(login_url='login')
class AttendanceCreateView(CreateView):
    model = Attendance 
    form_class = AttendanceForm 
    template_name = 'ems/create_attendance.html'
    def form_invalid(self, form):
        form.instance.user = self.request.user
        return super().form_invalid(form)
    def get_success_url(self):
        return reverse_lazy('ems:create_attendance')

# @login_required(login_url='login')
class AttendanceListView(ListView):
    model = Attendance 
    template_name = 'ems/show_attendance.html'
    context_object_name = 'attendances'


# Payroll CRUD
# @login_required(login_url='login')
class PayrollCreateView(CreateView):
    model = Payroll 
    form_class = PayrollForm 
    template_name = 'ems/create_payroll.html'
    def form_invalid(self, form):
        form.instance.user = self.request.user
        return super().form_invalid(form)
    def get_success_url(self):
        return reverse_lazy('ems:create_payroll')

# @login_required(login_url='login')
class PayrollListView(ListView):
    model = Payroll 
    template_name = 'ems/show_payroll.html'
    context_object_name = 'payrolls'
    # print({context_object_name})

# @login_required(login_url='login')
class PayrollEditView(UpdateView):
    model = Payroll 
    form_class = PayrollForm
    template_name = 'ems/edit_payroll.html'
    def get_success_url(self):
        return reverse_lazy('ems:show_payroll')

# @login_required(login_url='login')
def destroyPayroll(request, id):
    payrolls = Payroll.objects.get(id=id)
    payrolls.delete()
    return redirect("/ems/show_payroll")

