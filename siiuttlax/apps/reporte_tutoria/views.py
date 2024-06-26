from datetime import date
from urllib import request
from django.shortcuts import render
from siiuttlax.apps import career, group
from siiuttlax.apps.period.models import Semester

def reporte_tutoria(request):
    context = {
        'reporte': {
            'fecha': date.today(),  
            'carrera': career.carrera(), 
            'grado': Semester.grado(),  
            'grupo': group.grupo(),
        }
    }
    return render(request, 'reporte_tutoria.html', context)
