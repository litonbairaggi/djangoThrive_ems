from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from ems.models import Employee, Designation, Team, Attendance



def dashboard(request):
    total_employee = Employee.objects.count()
    total_team = Team.objects.count()
    total_attendance = Attendance.objects.count()
    total_designation = Designation.objects.count()
    attend = Attendance.objects.all().order_by('-id')
    context = {
        'employee': total_employee,
        'team': total_team,
        'attendance': total_attendance,
        'designation': total_designation,
        'attend': attend
    }
    return render(request, 'home.html', context)