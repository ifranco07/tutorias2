# Generated by Django 5.0.7 on 2024-08-01 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reporte_tutoria', '0005_rename_evidencia_evidencia_audio_reportetutoria_evidencia_audio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportetutoria',
            name='evidencia_audio',
            field=models.FileField(blank=True, null=True, upload_to='evidencias/audio', verbose_name='Evidencia de audio'),
        ),
        migrations.AlterField(
            model_name='reportetutoria',
            name='evidencia_canalizacion_alumno',
            field=models.FileField(blank=True, null=True, upload_to='evidencias/pdf_canalizacion', verbose_name='Evidencia pdf_canalizacion'),
        ),
        migrations.AlterField(
            model_name='reportetutoria',
            name='evidencia_fotografica',
            field=models.FileField(blank=True, null=True, upload_to='evidencias/imagenes_videos', verbose_name='Evidencia fotografica'),
        ),
        migrations.AlterField(
            model_name='reportetutoria',
            name='evidencia_lista_asistencia',
            field=models.FileField(blank=True, null=True, upload_to='evidencias/pdf', verbose_name='Evidencia list_asistencia'),
        ),
    ]
