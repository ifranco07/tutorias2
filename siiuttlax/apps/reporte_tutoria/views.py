from datetime import date
from django.shortcuts import render
from siiuttlax.apps import career, group
from siiuttlax.apps.period.models import Semester

def reporte_tutoria(request):
    context = {
        'reporte': {
            'fecha': date.today(),  # Utiliza la fecha actual
            'carrera': career.carrera(),  # Asumiendo que esta función retorna la carrera
            'grado': Semester.grado(),  # Asumiendo que esta función retorna el grado
            'grupo': group.grupo(),  # Asumiendo que esta función retorna el grupo
        }
    }
    return render(request, 'reporte_tutoria.html', context)
