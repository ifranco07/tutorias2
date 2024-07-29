from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from apps.period.models import Period
from apps.group.models import Group
from apps.academy.models import Professor

def index(request):
    periodos = Period.objects.all()
    print(periodos)
    return render(request, 'cumplimiento/consultas.html', {'periodos': periodos})

def consultas_por_periodo(request, periodo_id):
    periodo = get_object_or_404(Period, id=periodo_id)
    grupos = Group.objects.filter(period=periodo)
    grupos_data = []
    for grupo in grupos:
        grupo_data = {
            'Cuatrimestre': grupo.semester.semester_name,
            'Grupo': grupo.group,
            'Periodo': str(grupo.period),
            'Tutor': grupo.tutor.full_name if grupo.tutor else 'No asignado'
        }
        grupos_data.append(grupo_data)
    periods = Period.objects.all()
    return render(request, 'cumplimiento/consultas.html', {'grupos': grupos_data, 'periodo': periodo, 'periods': periods})

def Tutor(request):
    tutors = Professor.object.all()
    return render(request, 'consultas.html', {'tutors': tutors})

# def consultas_por_periodo(request, periodo_id):
#     periodo = get_object_or_404(Period, id=periodo_id)
#     grupos = Group.objects.filter(period=periodo)
#     grupos_data = [{'Cuatrimestre': grupo.semester.semester_name, 'Grupo': grupo.group, 'Periodo': str(grupo.period)} for grupo in grupos]
#     return render(request, 'cumplimiento/consultas.html', {'grupos': grupos_data, 'periodo': periodo})