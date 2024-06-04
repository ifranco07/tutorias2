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
    
    def __str__(self):
        return self.short_name
    
    class Meta:
        verbose_name = 'carrera'
        verbose_name_plural = 'carreras'


class Subject(models.Model):
    name = models.CharField(verbose_name='Nombre', max_length=200)
    career = models.ForeignKey(Career, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    teorical_hours = models.IntegerField(verbose_name='Horas teóricas')
    practical_hours = models.IntegerField(verbose_name='Horas prácticas')
    total_hours = models.IntegerField(verbose_name='Horas totales')
    file = models.FileField(verbose_name='Archivo', upload_to='subjects') ## Definir donde se almacenan archivos AWS S3


    def __str__(self):
        return self.short_name

    class Meta:
        verbose_name = 'materia'
        verbose_name_plural = 'materias'