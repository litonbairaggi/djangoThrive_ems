from django.shortcuts import render


from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http.response import HttpResponse
from django.views import View
from django.contrib import messages


# Create your views here.

from django.views.generic import (
    CreateView,
)

from .models import (
    Team
) 
from . froms import (
    TeamForm
)

class TeamCreateView(CreateView):
    model = Team
    form_class = TeamForm
    template_name = 'ems/create_team.html' 
    def form_invalid(self, form):
        form.instance.user = self.request.user   
        return super().form_invalid(form)
    def get_success_url(self):
        return reverse_lazy('store:create_supplier')
