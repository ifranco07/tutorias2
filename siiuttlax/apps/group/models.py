from django.db import models

from apps.period.models import Period, Semester
from apps.career.models import Career
from apps.academy.models import Professor

# Create your models here.
class Group(models.Model):
    GROUPS = [('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('F', 'F'), ('G', 'G'), ('H', 'H')]
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE, default=1)
    group = models.CharField(max_length=1, choices=GROUPS, default='A')
    observations = models.CharField(max_length=50, verbose_name='Observaciones', null=True, blank=True)
    period = models.ForeignKey(Period, on_delete=models.CASCADE)
    career = models.ForeignKey(Career, on_delete=models.CASCADE)
    tutor = models.ForeignKey(Professor, on_delete=models.CASCADE, null=True, blank=True)
    ## Many to Many with DetailsGroup
    ## Many to Many with Students

    def __str__(self):
        return f"{ self.semester }º{ self.group } { self.career }"
    
    class Meta:
        verbose_name = 'Grupo'
        verbose_name_plural = 'Grupos'
        ordering = ['group']