from django.shortcuts import render, redirect
from django.contrib import messages

from . models import Team, Designation
from . froms import TeamForm, DesignationForm
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