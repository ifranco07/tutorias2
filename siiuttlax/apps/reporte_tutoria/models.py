from django.db import models
from apps.career.models import Career
from apps.period.models import Semester
from apps.group.models import Group
from apps.academy.models import Professor

class ReporteTutoria(models.Model):
    fecha_tutoria = models.DateField(verbose_name='Fecha de Tutoría')
    carrera = models.ForeignKey(Career, on_delete=models.CASCADE, verbose_name='Carrera')
    semestre = models.ForeignKey(Semester, on_delete=models.CASCADE, verbose_name='Semestre')
    grupo = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name='Grupo')
    nombre_actividad = models.CharField(max_length=255, verbose_name='Nombre de la Actividad')
    objetivo_actividad = models.TextField(verbose_name='Objetivo de la Actividad')
    descripcion_actividad = models.TextField(verbose_name='Descripción de la Actividad')
    evidencias = models.FileField(upload_to='evidencias/', verbose_name='Evidencias', blank=True, null=True)
    lista_asistencia = models.FileField(upload_to='lista_asistencia/', verbose_name='ListaAistencia', blank=True, null=True)
    tutor = models.ForeignKey(Professor, on_delete=models.CASCADE, verbose_name='Tutor')

    def __str__(self):
        return f'Reporte de Tutoría {self.fecha_tutoria} - {self.tutor}'

    class Meta:
        verbose_name = 'Reporte de Tutoría'
        verbose_name_plural = 'Reportes de Tutorías'
        ordering = ['-fecha_tutoria']
