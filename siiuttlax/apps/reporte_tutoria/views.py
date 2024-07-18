from datetime import date
from django.shortcuts import render, redirect
from apps.career.models import Career
from apps.period.models import Semester
from apps.group.models import Group
from apps.academy.models import Professor
from .models import ReporteTutoria

def reporte_tutoria(request):
    if request.method == 'POST':
        fecha_tutoria = request.POST.get('fecha')
        carrera_id = request.POST.get('carrera')
        semestre_id = request.POST.get('semestre')
        grupo_id = request.POST.get('grupo')
        nombre_actividad = request.POST.get('nombre_actividad')
        objetivo_actividad = request.POST.get('objetivo_actividad')
        descripcion_actividad = request.POST.get('descripcion_actividad')
        evidencias = request.FILES.get('evidencias')
        lista_asistencia = request.FILES.get('lista_asistencia')

        reporte = ReporteTutoria(
            fecha_tutoria=fecha_tutoria,
            carrera_id=carrera_id,
            semestre_id=semestre_id,
            grupo_id=grupo_id,
            nombre_actividad=nombre_actividad,
            objetivo_actividad=objetivo_actividad,
            descripcion_actividad=descripcion_actividad,
            evidencias=evidencias,
            lista_asistencia=lista_asistencia,
            tutor=request.user.professor
        )
        reporte.save()

        # Redirigir a una página de éxito o a donde necesites después de guardar
        return redirect('success')  # Reemplazar 'success' con la URL a donde deseas redirigir

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
