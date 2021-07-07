from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from .views import (
    createTeam,
    showTeam,
    editTeam,
    updateTeam,
    destroy,
)

urlpatterns = [
    path('create_team/', createTeam, name='create_team'),
    path('show_team/', showTeam, name='show_team'),
    path('edit_team/<int:id>/', editTeam, name='edit_team'),
    path('update_team/<int:id>/', updateTeam, name='update_team'),
    path('delete_team/<int:id>/', destroy, name='delete_team'),
    
]
