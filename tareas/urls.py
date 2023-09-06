from django.urls import path
from . import views 

app_name = 'tareas'

from django.contrib.auth import views as auth_views

urlpatterns = [
    # Página de bienvenida (puedes configurarla para redireccionar a la lista de tareas)
    path('bienvenido/', views.bienvenido, name='bienvenido'),
    path('tareas-pendientes/', views.tareas_pendientes, name='tareas-pendientes'),
    path('crear-tarea/', views.crear_tarea, name='crear-tarea'),
    path('ver-tarea/<int:tarea_id>', views.ver_tarea, name='ver-tarea'), # agregar al path 
    path('editar/<int:tarea_id>/', views.editar_tarea, name='editar-tarea'),
    path('eliminar/<int:tarea_id>/', views.eliminar_tarea, name='eliminar-tarea'),
    path('completar/<int:tarea_id>/', views.completar_tarea, name='completar-tarea'),
    path('', views.index, name='index'),
  
]