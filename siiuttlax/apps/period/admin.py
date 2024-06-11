from django.contrib import admin

from .models import Period, Semester

# Register your models here.
@admin.register(Period)
class PeriodAdmin(admin.ModelAdmin):
    list_display = ['year', 'period', 'cycle', 'status']
    list_editable = ['status']

@admin.register(Semester)
class SemesterAdmin(admin.ModelAdmin):
    list_display = ['semester_name']