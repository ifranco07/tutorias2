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
    grupos_data = []

    num_actividades_esperadas = 4  # Asumiendo que se esperan 4 actividades

    for grupo in grupos:
        actividades = ReporteTutoria.objects.filter(grupo=grupo)
        actividades_nombres = [actividad.nombre_actividad for actividad in actividades] if actividades.exists() else []

        # Asegurar que siempre hay 4 actividades listadas, completar con 'No reportado'
        actividades_completas = actividades_nombres + ['No reportado'] * (num_actividades_esperadas - len(actividades_nombres))

        grupos_data.append({
            'Cuatrimestre': grupo.semester.semester_name,
            'Grupo': grupo.group,
            'Tutor': grupo.tutor.full_name if grupo.tutor else 'No asignado',
            'Periodo': str(grupo.period),
            'Actividades': actividades_completas
        })

    periods = Period.objects.all()
    return render(request, 'cumplimiento/consultas.html', {'grupos': grupos_data, 'current_period': period, 'periods': periods})
