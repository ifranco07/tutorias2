from django.db import models
from django.utils import timezone

class Tutor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    department = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    career = models.CharField(max_length=100)
    grade = models.CharField(max_length=10)
    group = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Activity(models.Model):
    name = models.CharField(max_length=100)
    objective = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.name

class TutoringSession(models.Model):
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return f"Tutoring session on {self.date} by {self.tutor}"
