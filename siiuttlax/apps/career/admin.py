from django.contrib import admin

from .models import Career, Subject

# Register your models here.
@admin.register(Career)
class CareerAdmin(admin.ModelAdmin):
    list_display = ['short_name', 'level', 'name']
    ordering = ['level', 'short_name']

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'career', 'semester', 'semanal_hours', 'total_hours']
    list_filter = ['career', 'semester']