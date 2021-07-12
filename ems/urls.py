from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

# from . import views

from .views import (
    registerPage,
    loginPage,
    logoutUser,

    TeamCreateView,
    TeamListView,
    TeamEditView,
    
    destroy,

    createDesignation,
    showDesignation,
    editDesignation,
    updateDesignation,
    destroyDesignation,

    createEmployee,
    showEmployee,
    editEmployee,
    updateEmployee,
    destroyEmployee,

    createAttendance,
    showAttendance,

    createPayroll,
    showPayroll,
    editPayroll,
    updatePayroll,
    destroyPayroll,
)

app_name="ems"
urlpatterns = [

    path('register/', registerPage, name='register'),
	path('login/', loginPage, name='login'),  
	path('logout/', logoutUser, name="logout"),

    path('create_team/', TeamCreateView.as_view(), name='create_team'),
    path('show_team/', TeamListView.as_view(), name='show_team'),
    path('update_team/<int:pk>/', TeamEditView.as_view(), name='update_team'),

    path('delete_team/<int:id>/', destroy, name='delete_team'),



    path('create_designation/', createDesignation, name='create_designation'),
    path('show_designation/', showDesignation, name='show_designation'),
    path('edit_designation/<int:id>/', editDesignation, name='edit_designation'),
    path('update_designation/<int:id>/', updateDesignation, name='update_designation'),
    path('delete_designation/<int:id>/', destroyDesignation, name='delete_designation'),
    
    path('create_employee/', createEmployee, name='create_employee'),
    path('show_employee/', showEmployee, name='show_employee'),
    path('edit_employee/<int:id>/', editEmployee, name='edit_employee'),
    path('update_employee/<int:id>/', updateEmployee, name='update_employee'),
    path('delete_employee/<int:id>/', destroyEmployee, name='delete_employee'),

    path('create_attendance/', createAttendance, name='create_attendance'),
    path('show_attendance/', showAttendance, name='show_attendance'),

    path('create_payroll/', createPayroll, name='create_payroll'),
    path('show_payroll/', showPayroll, name='show_payroll'),
    path('edit_payroll/<int:id>/', editPayroll, name='edit_payroll'),
    path('update_payroll/<int:id>/', updatePayroll, name='update_payroll'),
    path('delete_payroll/<int:id>/', destroyPayroll, name='delete_payroll'),
    
]