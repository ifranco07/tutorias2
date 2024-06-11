from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Professor(User):
    title = models.CharField(max_length=50, verbose_name='Título')
    employee_number = models.IntegerField(verbose_name='Número de Empleado')

    @property
    def full_name(self):
        return f"{ self.first_name } { self.last_name }"
    
    def __str__(self):
        return f"{ self.title } - { self.full_name }"

    class Meta:
        verbose_name = 'Profesor'
        verbose_name_plural = 'Profesores'
        
        
class Student(User):
    enrollment = models.CharField(max_length=12, verbose_name='Matrícula')
    
    @property
    def full_name(self):
        return f"{ self.first_name } { self.last_name }"
    
    def __str__(self):
        return f"{ self.full_name } - { self.enrollment }"
    
    class Meta:
        verbose_name = 'Estudiante'
        verbose_name_plural = 'Estudiantes'


class Guest(models.Model):
    pass


class Principal(models.Model):
    pass