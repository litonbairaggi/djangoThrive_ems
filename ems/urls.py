from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from .views import (
    TeamCreateView
)

urlpatterns = [
    path('create_tem/', TeamCreateView.as_view(), name='create_tem'),
]