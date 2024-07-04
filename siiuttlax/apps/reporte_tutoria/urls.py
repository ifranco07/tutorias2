from django.urls import path

from . import views

app_name="reporte"
urlpatterns = [
    
    path( "",views.reporte_tutoria,name="reporte_tutorias")
]
