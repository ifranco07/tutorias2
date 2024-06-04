from django.db import models

# Create your models here.
class Period(models.Model):
    MONTHS_PERIOD = [
        ('Enero - Abril', 'Enero - Abril'),
        ('Mayo - Agosto', 'Mayo - Agosto'),
        ('Septiembre - Diciembre', 'Septiembre - Diciembre')
    ]
    period = models.CharField(max_length=22, choices=MONTHS_PERIOD, verbose_name='Periodo')
    year = models.IntegerField(verbose_name='Año', default=2024)
    cycle = models.CharField(max_length=20, verbose_name='Ciclo', default='2024-2025')

    def __str__(self):
        return f'{ self.period } { self.year }'
    
    class Meta:
        verbose_name = 'Periodo'
        verbose_name_plural = 'Periodos'
        ordering = ['year']


class Semester(models.Model):
    semester = models.CharField(max_length=2, verbose_name="Cuatrimestre")
    semester_name = models.CharField(max_length=10, verbose_name="Cuatrimestre en Letra")
    short_name = models.CharField(max_length=5, verbose_name="Abreviatura")

    def __str__(self):
        return f"{ self.semester }"

    class Meta:
        verbose_name = 'Cuatrimestre'
        verbose_name_plural = 'Cuatrimestres'