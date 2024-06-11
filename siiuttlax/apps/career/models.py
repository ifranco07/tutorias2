from django.db import models

from apps.period.models import Semester
# Create your models here.
class Career(models.Model):
    LEVELS = [
        ('TSU', 'Técnico Superior Universitario'),
        ('Ing', 'Ingeniería'),
        ('Lic', 'Licenciatura'),
        ('M', 'Maestría'),
    ]
    level = models.CharField(
            verbose_name='Nivel',
            max_length=10,
            choices = LEVELS,    
        )
    name = models.CharField(
            verbose_name='Nombre',
            max_length=200,    
        )
    short_name = models.CharField(
            verbose_name='Abreviatura',
            max_length=20,    
        )
    status = models.BooleanField(verbose_name='Estado', default=True)
    year_plan = models.CharField(verbose_name='Plan de estudios', max_length=4, blank=True, null=True)
    
    def __str__(self):
        return self.short_name
    
    class Meta:
        verbose_name = 'carrera'
        verbose_name_plural = 'carreras'


class Subject(models.Model):
    name = models.CharField(verbose_name='Nombre', max_length=200)
    career = models.ForeignKey(Career, on_delete=models.CASCADE, verbose_name='Carrera')
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE, verbose_name='Cuatrimestre')
    teorical_hours = models.IntegerField(verbose_name='Horas teóricas', default=0)
    practical_hours = models.IntegerField(verbose_name='Horas prácticas', default=0)
    total_hours = models.IntegerField(verbose_name='Horas totales', default=0)
    semanal_hours = models.IntegerField(verbose_name='Horas semanales', default=0)
    file = models.CharField(verbose_name='Archivo', max_length=200, blank=True, null=True)
    #file = models.FileField(verbose_name='Archivo', upload_to='subjects') ## Definir donde se almacenan archivos AWS S3


    def __str__(self):
        return f"{ self.name } { self.career }"

    class Meta:
        verbose_name = 'materia'
        verbose_name_plural = 'materias'
        ordering = ['career', 'semester']