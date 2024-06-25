from datetime import date
<<<<<<< HEAD
=======
from urllib import request
>>>>>>> 4da063739f084aff3c183a3609af567bf5669c56
from django.shortcuts import render
from siiuttlax.apps import career, group
from siiuttlax.apps.period.models import Semester

<<<<<<< HEAD
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
=======
from siiuttlax.apps import career, group
from siiuttlax.apps.period.models import Semester

def reporte_tutoria (request):context={
    'reporte':{
        date.fecha(''),
        career.carrera(''),
        Semester.grado(''),
        group.grupo(''),
    }
} 
render(request, 'reporte_tutoria.html', )
>>>>>>> 4da063739f084aff3c183a3609af567bf5669c56
