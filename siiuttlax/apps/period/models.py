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