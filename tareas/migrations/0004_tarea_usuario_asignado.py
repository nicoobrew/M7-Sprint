# Generated by Django 4.2.3 on 2023-09-05 22:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tareas', '0003_tarea_observaciones_alter_tarea_etiqueta'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarea',
            name='usuario_asignado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tareas_asignadas', to=settings.AUTH_USER_MODEL),
        ),
    ]
