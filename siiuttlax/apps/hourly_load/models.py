from django.db import models

from apps.group.models import Group
# Create your models here.
class Concept(models.Model):
    concept = models.CharField(max_length=100, verbose_name='Concepto')
    description = models.CharField(max_length=150, verbose_name='Descripción')
    hours = models.IntegerField(verbose_name='Horas', default=0)
    status = models.BooleanField(verbose_name='Estado', default=True)

    def __str__(self):
        return self.concept
    
    class Meta:
        verbose_name = 'Concepto'
        verbose_name_plural = 'Conceptos'

class GroupDetails(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    concept = models.ForeignKey(Concept, on_delete=models.CASCADE)
    hours = models.IntegerField(verbose_name='Horas', default=0)
    #tutor = models.ForeignKey(Professor, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{ self.concept } { self.group }"

    class Meta:
        verbose_name = 'Detalle del grupo'
        verbose_name_plural = 'Detalles del grupo'