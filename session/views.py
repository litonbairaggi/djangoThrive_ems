from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib import messages
from . froms import SignUpForm

from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.template.loader import render_to_string


# Create your views here.


def loginPage(request):
    if request.method=="POST":
        form=AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                messages.error(request, 'Invalid User or password') 
        else:
            messages.error(request, 'Invalid User or password') 
    else:
        form=AuthenticationForm()
    context={
        'form': form
    }    
    return render(request, 'session/login.html', context)  



def logoutPage(request):
    logout(request)
    messages.success(request, 'Successfully Logged Out!')
    return redirect('/session/login/')            
                   

# django Registations form                   
def registrationPage(request):
    if request.method=="POST":
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('session:login')
    else:
        form=SignUpForm()
    return render(request, 'session/register.html', {'form': form})  



# Change Password
def change_password(request):
    if request.method=="POST":
        form=PasswordChangeForm(data=request.POST, user=request.user) 
        if form.is_valid():
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Password has successfully Changed')
            return redirect('dashboard')
    else:
        form = PasswordChangeForm(user=request.user)
    context = {
        'form':form
    }    
    return render(request, 'session/change_password.html', context) 

