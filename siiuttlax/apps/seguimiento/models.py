# models.py
from django.db import models

class Career(models.Model):
    level = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=50)
    status = models.IntegerField()
    year_plan = models.IntegerField()

    def __str__(self):
        return self.name
