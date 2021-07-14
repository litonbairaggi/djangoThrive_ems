from django.urls import path
from .views import loginPage, registrationPage, logoutPage, change_password 

app_name='session'
urlpatterns = [
    path('login/', loginPage, name='login'),
    path('registration/', registrationPage, name='registration'),
    path('logout/', logoutPage, name='logout'),
    path('password/', change_password, name='password'),
]