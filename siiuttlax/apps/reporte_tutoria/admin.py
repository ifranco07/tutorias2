from django.contrib import admin
from .models import ReporteTutoria, CanalizacionAlumno
# Register your models here.

class Reportes_Tutorias(admin.ModelAdmin):
    fields = ["fecha_tutoria",
              "carrera",
              "semestre",
              "grupo",
              "nombre_actividad",
              "objetivo_actividad",
              "descripcion_actividad",
              "evidencia_fotografica",
              "evidencia_lista_asistencia",
              "evidencia_audio",
              "tutor"
              ]
    list_display = ["fecha_tutoria", "tutor"]

admin.site.register(ReporteTutoria, Reportes_Tutorias)


class Canalizaciones_Alumnos(admin.ModelAdmin):
    fields = [
        "carrera",
        "semestre",
        "grupo",
        "student",
        "evidencia_canalizacion_alumno",
        "tutor"
    ]
    list_display = ["fecha_creacion", "student"]

admin.site.register(CanalizacionAlumno, Canalizaciones_Alumnos)