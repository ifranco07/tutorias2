from django.urls import path
from . import views

app_name = "reporte_tutoria"
urlpatterns = [
    path('', views.reporte_tutoria, name='reporte_tutorias'),
    path('success/', views.success_view, name='success'),
    path('mis_reportes/', views.mis_reportes, name='mis_reportes'),
    path('canalizacion_alumno', views.canalizacion_alumno, name='canalizacion_alumno'),
    path('canalizacion_exitosa/', views.canalizacion_exitosa, name='canalizacion_exitosa')
]
