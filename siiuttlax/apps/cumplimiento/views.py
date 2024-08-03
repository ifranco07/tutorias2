from django.shortcuts import render, get_object_or_404
from apps.period.models import Period
from apps.group.models import Group
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
    grupos_data = [
        {
            'Cuatrimestre': grupo.semester.semester_name,
            'Grupo': grupo.group,
            'Tutor': grupo.tutor.full_name if grupo.tutor else 'No asignado',
            'Periodo': str(grupo.period),
        }
        for grupo in grupos
    ]
    periods = Period.objects.all()
    return render(request, 'cumplimiento/consultas.html', {'grupos': grupos_data, 'current_period': period, 'periods': periods})
