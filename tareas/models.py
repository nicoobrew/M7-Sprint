from django.db import models
from django.contrib.auth.models import User

class Etiqueta(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Prioridad(models.Model):

    NIVELES = (
        ('baja', 'Baja'),
        ('media', 'Media'),
        ('alta', 'Alta')
    )

    nivel_prioridad = models.CharField(max_length=10, choices=NIVELES)

    def __str__(self):
        return self.nivel_prioridad

class Tarea(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_vencimiento = models.DateField()
    
    ESTADOS = (
        ('pendiente', 'Pendiente'),
        ('en_progreso', 'En Progreso'),
        ('completada', 'Completada'),
    )
    estado = models.CharField(max_length=20, choices=ESTADOS)
    etiqueta = models.ForeignKey(Etiqueta, on_delete=models.CASCADE, null=True)
    observaciones = models.TextField(blank=True, null=True)
    usuario_asignado = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tareas_asignadas', null=True, blank=True)
    prioridad = models.ForeignKey(Prioridad, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.titulo
    

    

    