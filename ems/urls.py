from django.urls import path

from django.conf import settings
from django.conf.urls.static import static
from .views import (
    createTeam,
    showTeam,
    editTeam,
    updateTeam,
    destroy,

    createDesignation,
    showDesignation,
    editDesignation,
    updateDesignation,
    destroyDesignation,
)

urlpatterns = [
    path('create_team/', createTeam, name='create_team'),
    path('show_team/', showTeam, name='show_team'),
    path('edit_team/<int:id>/', editTeam, name='edit_team'),
    path('update_team/<int:id>/', updateTeam, name='update_team'),
    path('delete_team/<int:id>/', destroy, name='delete_team'),

    path('create_designation/', createDesignation, name='create_designation'),
    path('show_designation/', showDesignation, name='show_designation'),
    path('edit_designation/<int:id>/', editDesignation, name='edit_designation'),
    path('update_designation/<int:id>/', updateDesignation, name='update_designation'),
    path('delete_designation/<int:id>/', destroyDesignation, name='delete_designation'),
    
]
