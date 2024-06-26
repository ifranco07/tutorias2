from django.contrib import admin
from django.urls import path, include
from . import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.home.urls')),
    path('', include('apps.user_profile.urls')),
    path('', include('apps.academy.urls')),
    path('', include('apps.interview.urls')),
    path('', include('apps.group.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('reporte_tutoria/', views.reporte_tutoria, name='reporte_tutoria'),
]