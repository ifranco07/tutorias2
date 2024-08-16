from django.shortcuts import render, get_object_or_404
from apps.period.models import Period
from apps.group.models import Group
from apps.reporte_tutoria.models import ReporteTutoria
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    periods = Period.objects.all()
    current_period = periods.first()
    grupos = Group.objects.filter(period=current_period)
    grupos_data = [
        {
            'Cuatrimestre': grupo.semester.semester_name,
            'Grupo': grupo.group,
            'Tutor': grupo.tutor.full_name if grupo.tutor else 'No asignado',
            'Periodo': str(grupo.period),
        }
        for grupo in grupos
    ]
    return render(request, 'cumplimiento/consultas.html', {'periods': periods, 'current_period': current_period, 'grupos': grupos_data})

@login_required
def consultas_por_periodo(request, periodo_id):
    period = get_object_or_404(Period, id=periodo_id)
    grupos = Group.objects.filter(period=period)
    
    # Obtener el mes del parámetro GET, si existe
    mes = request.GET.get('mes', None)
    
    grupos_data = []
    num_actividades_esperadas = 4
    
    for grupo in grupos:
        # Filtrar reportes por mes y verificar si hay reportes para el grupo
        if mes:
            actividades = ReporteTutoria.objects.filter(grupo=grupo, fecha_tutoria__month=mes)
            if not actividades.exists():
                continue  # Si no hay reportes en el mes, pasar al siguiente grupo
        
        actividades = ReporteTutoria.objects.filter(grupo=grupo)
        actividades_data = []
        
        for actividad in actividades:
            actividades_data.append({
                'nombre_actividad': actividad.nombre_actividad,
                'evidencia_lista_asistencia': actividad.evidencia_lista_asistencia.url if actividad.evidencia_lista_asistencia else None,
                'evidencia_canalizacion_alumno': actividad.evidencia_canalizacion_alumno.url if actividad.evidencia_canalizacion_alumno else None
            })
        
        actividades_completas = actividades_data + [{'nombre_actividad': 'No reportado', 'evidencia_lista_asistencia': None, 'evidencia_canalizacion_alumno': None}] * (num_actividades_esperadas - len(actividades_data))
        
        grupos_data.append({
            'Cuatrimestre': grupo.semester.semester_name,
            'Grupo': grupo.group,
            'Tutor': grupo.tutor.full_name if grupo.tutor else 'No asignado',
            'Periodo': str(grupo.period),
            'Carrera': grupo.career.short_name if grupo.career else 'No asignada',
            'Actividades': actividades_completas
        })

    periods = Period.objects.all()
    return render(request, 'cumplimiento/consultas.html', {'grupos': grupos_data, 'current_period': period, 'periods': periods, 'selected_mes': mes})
