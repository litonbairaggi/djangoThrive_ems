from django.shortcuts import render, redirect
from django.contrib import messages

from . models import Team
from . froms import TeamForm
# Create your views here.

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