from django.shortcuts import render, redirect
from django.contrib import messages

from . models import Employee, Team, Designation, Employee, Attendance, Payroll
from . froms import TeamForm, DesignationForm, EmployeeForm, AttendanceForm, PayrollForm
# Create your views here.


# Team crud
def createTeam(request):
    if request.method == "POST":
        form = TeamForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect(('/ems/show_team'))
            except:
                pass

    else:
        form = TeamForm()   
    context = {
        'form': form
    }    
    return render(request, 'ems/create_team.html', context)    

def showTeam(request):
    teams = Team.objects.all()
    context = {
        'teams': teams
    } 
    return render(request, 'ems/show_team.html', context)

def editTeam(request, id):
    teams = Team.objects.get(id=id)
    context = {
        'teams': teams
    }
    return render(request,'ems/edit_team.html', context)

def updateTeam(request, id):
    teams = Team.objects.get(id=id)
    form = TeamForm(request.POST, instance=teams)
    if form.is_valid():
        form.save()
        return redirect("/ems/show_team/")
    context = {
        'teams': teams
    }    
    return render(request, 'ems/edit_team.html', context) 

def destroy(request, id):
    teams = Team.objects.get(id=id)
    teams.delete()
    return redirect("/ems/show_team")

# Designation crud
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

def showDesignation(request):
    designations = Designation.objects.all()
    context = {
        'designations': designations
    }
    return render(request, 'ems/show_designation.html', context)

def editDesignation(request, id):
    designations = Designation.objects.get(id=id)
    context = {
        'designations': designations
    }
    return render(request,'ems/edit_designation.html', context)

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

def destroyDesignation(request, id):
    designations = Designation.objects.get(id=id)
    designations.delete()
    return redirect("/ems/show_designation")

# Employee curd  

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

def showEmployee(request):
    employees = Employee.objects.all()
    context = {
        'employees': employees
    }
    return render(request, 'ems/show_employee.html', context)

def editEmployee(request, id):
    employees = Employee.objects.get(id=id)
    context ={
        'employees': employees
    }
    return render(request, 'ems/edit_employee.html', context)


def updateEmployee(request, id):
    employees = Employee.objects.get(id=id)
    form = EmployeeForm(request.POST, instance=employees)
    if form.is_valid():
        form.save()
        return redirect("/ems/show_employee/")
    context = {
        'employees': employees
    }    
    return render(request, 'ems/edit_employee.html', context) 

def destroyEmployee(request, id):
    employees = Employee.objects.get(id=id)
    employees.delete()
    return redirect("/ems/show_employee")


# attendance CURD
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

def showAttendance(request):
    attendances = Attendance.objects.all()
    context = {
        'attendances': attendances
    }
    return render(request, 'ems/show_attendance.html', context)

# Payroll curd 


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

def showPayroll(request):
    payrolls = Payroll.objects.all()
    context = {
        'payrolls': payrolls
    }
    return render(request, 'ems/show_payroll.html', context)

def editPayroll(request, id):
    payrolls = Payroll.objects.get(id=id)
    context ={
        'payrolls': payrolls
    }
    return render(request, 'ems/edit_payroll.html', context)


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

def destroyPayroll(request, id):
    payrolls = Payroll.objects.get(id=id)
    payrolls.delete()
    return redirect("/ems/show_payroll")