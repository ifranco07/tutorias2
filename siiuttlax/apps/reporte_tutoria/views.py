from django.contrib.auth.decorators import login_required
from datetime import date, datetime
from django.shortcuts import render, redirect
from django.contrib import messages
from apps.career.models import Career
from apps.period.models import Semester
from apps.group.models import Group
from apps.academy.models import Professor, Student
from .models import ReporteTutoria, CanalizacionAlumno
from django.http import HttpResponseForbidden

def reporte_tutoria(request):
    # Obtener la fecha actual
    fecha_actual = datetime.now()

    # Calcular el mes y año del reporte
    mes_reporte = fecha_actual.month - 1 if fecha_actual.month > 1 else 12
    año_reporte = fecha_actual.year if fecha_actual.month > 1 else fecha_actual.year - 1

    # Verificar si estamos en los primeros 5 días del mes siguiente
    if not (1 <= fecha_actual.day <= 25):
        return HttpResponseForbidden("No puedes acceder a este módulo fuera del período permitido.")

    # Si la fecha es válida, continuar con el proceso del reporte
    if request.method == 'POST':
        fecha_tutoria = request.POST.get('fecha')
        carrera_id = request.POST.get('carrera')
        semestre_id = request.POST.get('semestre')
        grupo_id = request.POST.get('grupo')
        nombre_actividad = request.POST.get('nombre_actividad')
        objetivo_actividad = request.POST.get('objetivo_actividad')
        descripcion_actividad = request.POST.get('descripcion_actividad')
        evidencia_fotografica = request.FILES.get('evidencia_fotografica')
        evidencia_lista_asistencia = request.FILES.get('evidencia_lista_asistencia')
        evidencia_audio = request.FILES.get('evidencia_audio')
      

        if not (fecha_tutoria and nombre_actividad and objetivo_actividad and descripcion_actividad and evidencia_fotografica and evidencia_lista_asistencia):
            messages.error(request, 'Por favor, complete todos los campos requeridos.')
            return redirect('reporte_tutoria:reporte_tutorias')

       
        reporte = ReporteTutoria(
            fecha_tutoria = fecha_tutoria,
            carrera_id = carrera_id,
            semestre_id = semestre_id,
            grupo_id = grupo_id,
            nombre_actividad = nombre_actividad,
            objetivo_actividad = objetivo_actividad,
            descripcion_actividad = descripcion_actividad,
            evidencia_fotografica = evidencia_fotografica,
            evidencia_lista_asistencia = evidencia_lista_asistencia,
            evidencia_audio = evidencia_audio,
            tutor = request.user.professor    
        )
        reporte.save()

        # Redirigir a una página de éxito o a donde necesites después de guardar
        return redirect('reporte_tutoria:success') 

    else:
        tutor = request.user.professor  
        group = tutor.group_set.first()  # Obtener el primer grupo del tutor
        carrera = group.career
        semestre = group.semester

        context = {
            'reporte': { 
                'carreras': Career.objects.all(), 
                'semestres': Semester.objects.all(),  
                'grupos': Group.objects.all(),
            },
            'default_carrera': carrera.id,
            'default_semestre': semestre.id,
            'default_grupo': group.id,
        }
        return render(request, 'reporte_tutorias/reporte_tutoria.html', context)
    
def success_view(request):
    return render(request, 'reporte_tutorias/success.html')

@login_required
def mis_reportes(request):
    reportes = ReporteTutoria.objects.filter(tutor=request.user.professor).order_by('-fecha_tutoria', 'nombre_actividad')
    return render(request, 'reporte_tutorias/mis_reportes.html', {'reportes': reportes})


def canalizacion_alumno(request):
    if request.method == 'POST':
        carrera_id = request.POST.get('carrera')
        semestre_id = request.POST.get('semestre')
        grupo_id = request.POST.get('grupo')
       

        canalizacion = CanalizacionAlumno(
                carrera_id = carrera_id,
                semestre_id = semestre_id,
                grupo_id = grupo_id,
                tutor = request.user.professor    
        )
        canalizacion.save()

    else:
        tutor = request.user.professor  
        group = tutor.group_set.first()  # Obtener el primer grupo del tutor
        carrera = group.career
        semestre = group.semester

        context = {
            'canalizacion': { 
                'carreras': Career.objects.all(), 
                'semestres': Semester.objects.all(),  
                'grupos': Group.objects.all(),
            },
            'default_carrera': carrera.id,
            'default_semestre': semestre.id,
            'default_grupo': group.id,
        }
        return render(request, 'reporte_tutorias/canalizacion_alumno.html', context)