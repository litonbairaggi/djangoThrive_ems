from django.contrib import admin

from . models import Team, Designation, Employee, Attendance
# Register your models here.

admin.site.register(Team)
admin.site.register(Designation)
admin.site.register(Employee)
admin.site.register(Attendance)
