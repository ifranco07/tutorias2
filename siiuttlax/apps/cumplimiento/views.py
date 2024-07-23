from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from apps.period.models import Period
from apps.group.models import Group

def index(request):
    periods = Period.objects.all()
    return render(request, 'index.html', {'periods': periods})

def consultas_por_periodo(request, periodo_id):
    periodo = get_object_or_404(Period, id=periodo_id)
    grupos = Group.objects.filter(period=periodo)
    grupos_data = [{'Cuatrimestre': grupo.semester.semester_name, 'Grupo': grupo.group, 'Periodo': str(grupo.period)} for grupo in grupos]
    return JsonResponse(grupos_data, safe=False)

# from email.headerregistry import Group
# from django.shortcuts import render, get_object_or_404
# from urllib import request
# from django.http import JsonResponse

# from apps import period


# # Create your views here.

# def index():
#     periods =  period.objects.all()
#     return render(request, 'index.html', {periods: periods})

# def consultas_por_periodo(request, periodo_id):
#     periodo = get_object_or_404(period, id=periodo_id)
#     grupo = Group.objects.filter(periods=periodo)
#     consultas_data = [{'Cuatrimestre': grupo.GROUPS, 'Grupo:': grupo.semester, 'Periodo': grupo.period} for grupo in grupo]
#     return JsonResponse(consultas_data, safe=False)
