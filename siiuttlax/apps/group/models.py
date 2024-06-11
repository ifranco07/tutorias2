from django.db import models
from django.db.models.signals import post_save

from apps.period.models import Period, Semester
from apps.career.models import Career, Subject
from apps.academy.models import Professor
from django.dispatch import receiver

# Create your models here.
class Group(models.Model):
    GROUPS = [('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('F', 'F'), ('G', 'G'), ('H', 'H')]

    semester = models.ForeignKey(
        Semester, 
        on_delete=models.CASCADE, 
        default=1, 
        verbose_name='Cuatrimestre')
    group = models.CharField(
        max_length=1, 
        choices=GROUPS, 
        default='A',
        verbose_name='Grupo')
    observations = models.CharField(
        max_length=50, 
        verbose_name='Observaciones', 
        null=True, blank=True)
    period = models.ForeignKey(
        Period, 
        on_delete=models.CASCADE,
        verbose_name='Periodo')
    career = models.ForeignKey(
        Career, 
        on_delete=models.CASCADE,
        verbose_name='Carrera')
    tutor = models.ForeignKey(
        Professor, 
        on_delete=models.CASCADE, 
        verbose_name='Tutor',
        null=True, blank=True)
    subjects = models.ManyToManyField(
        Subject,
        verbose_name='Materias',
        blank=True)
    ## Many to Many with DetailsGroup
    ## Many to Many with Students

    def set_subjects(self):
        subjects_by_career_and_semester = Subject.objects.filter(career=self.career, semester=self.semester)
        self.subjects.set(subjects_by_career_and_semester)

    def __str__(self):
        return f"{ self.semester } { self.group } { self.career }"
    
    class Meta:
        verbose_name = 'Grupo'
        verbose_name_plural = 'Grupos'
        ordering = ['group']

@receiver(post_save, sender=Group)
def set_subjects_signal(sender, instance, created, **kwargs):
    if created:
        instance.set_subjects()