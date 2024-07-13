from datetime import date
from urllib import request
from django.shortcuts import render
from apps.career.models import Career
from apps.period.models import Semester
from apps.group.models import Group

def reporte_tutoria(request):
    context = {
        'reporte': { 
            'carreras': Career.objects.all(), 
            'semestres': Semester.objects.all(),  
            'grupos': Group.objects.all(),
        }
    }
    return render(request, 'reporte_tutorias/reporte_tutoria.html', context)
