from django.contrib import admin
from django.db import models

from .models import Period

# Register your models here.
@admin.register(Period)
class PeriodAdmin(admin.ModelAdmin):
    list_display = ['period', 'year', 'cycle']