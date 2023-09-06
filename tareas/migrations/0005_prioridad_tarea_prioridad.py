# Generated by Django 4.2.3 on 2023-09-05 23:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tareas', '0004_tarea_usuario_asignado'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prioridad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nivel_prioridad', models.CharField(choices=[('baja', 'Baja'), ('media', 'Media'), ('alta', 'Alta')], max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='tarea',
            name='prioridad',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tareas.prioridad'),
        ),
    ]
