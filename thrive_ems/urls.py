from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from .views import dashboard

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dashboard, name='dashboard'),
    path('ems/', include('ems.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
