from django.contrib import admin

from . models import Team, Designation, Employee, Attendance, Payroll
# Register your models here.

admin.site.register(Team)
admin.site.register(Designation)
admin.site.register(Attendance)
admin.site.register(Payroll)

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'employee_name', 'employee_email', 'team', 'designation', 'employee_img', 'address']
