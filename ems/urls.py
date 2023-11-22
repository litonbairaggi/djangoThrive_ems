from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

# from . import views

from .views import (

    TeamCreateView,
    TeamListView,
    TeamEditView,
    destroy,

    DesignationCreateView,
    DesignationListView,
    DesignationEditView,
    destroyDesignation,

    EmployeeCreateView,
    EmployeeListView,
    EmployeeEditView,
    destroyEmployee,

    AttendanceCreateView,
    AttendanceListView,

    PayrollCreateView,
    PayrollListView,
    PayrollEditView,
    destroyPayroll,

)

app_name="ems"
urlpatterns = [

    path('create_team/', TeamCreateView.as_view(), name='create_team'),
    path('show_team/', TeamListView.as_view(), name='show_team'),
    path('update_team/<int:pk>/', TeamEditView.as_view(), name='update_team'),

    path('delete_team/<int:id>/', destroy, name='delete_team'),

    path('create_designation/', DesignationCreateView.as_view(), name='create_designation'),
    path('show_designation/', DesignationListView.as_view(), name='show_designation'),
    path('update_designation/<int:pk>/', DesignationEditView.as_view(), name='update_designation'),
    path('delete_designation/<int:id>/', destroyDesignation, name='delete_designation'),

    path('create_employee/', EmployeeCreateView.as_view(), name='create_employee'),
    path('show_employee/', EmployeeListView.as_view(), name='show_employee'),
    path('update_employee/<int:pk>/', EmployeeEditView.as_view(), name='update_employee'),
    path('delete_employee/<int:id>/', destroyEmployee, name='delete_employee'),

    path('create_attendance/', AttendanceCreateView.as_view(), name='create_attendance'),
    path('show_attendance/', AttendanceListView.as_view(), name='show_attendance'),

    path('create_payroll/', PayrollCreateView.as_view(), name='create_payroll'),
    path('show_payroll/', PayrollListView.as_view(), name='show_payroll'),
    path('update_payroll/<int:pk>/', PayrollEditView.as_view(), name='update_payroll'),
    path('delete_payroll/<int:id>/', destroyPayroll, name='delete_payroll'),
]