# Generated by Django 5.0.6 on 2024-07-11 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('justify', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='email',
            field=models.EmailField(default='default@gmail.com', max_length=254),
            preserve_default=False,
        ),
    ]
