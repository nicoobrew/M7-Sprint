from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect, get_object_or_404
from .forms import TareaForm, FiltroTareasForm
from django.contrib.auth.decorators import login_required
from .models import Tarea, User, Prioridad

# Create your views here.
# def registrarse(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             # Loguear al usuario después del registro si lo deseas
#             login(request, user)
#             return redirect('tareas/bienvenido.html')  # Redireccionar a la página de lista de tareas
#     else:
#         form = UserCreationForm()
#     return render(request, 'users/login.html', {'form': form})

def index(request):
    return render(request, 'tareas/index.html')

def bienvenido(request):
    return render(request, 'tareas/bienvenido.html')

@login_required
# Vista para crear tarea y asignarla a algun usuario de la app
def crear_tarea(request):
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            tarea = form.save(commit=False)
            tarea.usuario = form.cleaned_data['usuario_asignado']
            tarea.save()
            return redirect('tareas:tareas-pendientes') 
    else:
        form = TareaForm()
    
    return render(request, 'tareas/crear_tareas.html', {'form': form})

@login_required
def ver_tarea(request, tarea_id):
    # Obtener la tarea específica por su ID o devolver un error 404 si no existe
    tarea = get_object_or_404(Tarea, pk=tarea_id)

    return render(request, 'tareas/ver_tarea.html', {'tarea': tarea})

@login_required
# Vista para editar una tarea existente
def editar_tarea(request, tarea_id):
    tarea = get_object_or_404(Tarea, id=tarea_id)

    if request.method == 'POST':
        form = TareaForm(request.POST, instance=tarea)
        if form.is_valid():
            form.save()
            return redirect('tareas:ver-tarea', tarea_id=tarea_id)  
    else:
        form = TareaForm(instance=tarea)

    return render(request, 'tareas/editar_tarea.html', {'form': form, 'tarea': tarea})

@login_required
# Vista para confirmar la eliminación de una tarea
def eliminar_tarea(request, tarea_id):
    tarea = get_object_or_404(Tarea, pk=tarea_id)

    if request.method == 'POST':
        # Si el usuario confirma la eliminación, redirige a la vista de eliminación
        tarea.delete()
        return redirect('tareas:tareas-pendientes')
    
    return render(request, 'tareas/eliminar_tarea.html', {'tarea': tarea})

@login_required
# Vista para marcar una tarea como completada
def completar_tarea(request, tarea_id):
    tarea = get_object_or_404(Tarea, pk=tarea_id)
    tarea.estado = 'completada'
    tarea.save()
    return redirect('tareas:tareas-pendientes')

@login_required
def tareas_pendientes(request):
    tareas = Tarea.objects.filter(usuario=request.user)

    # Procesar el formulario de filtro si se ha enviado
    if request.method == 'POST':
        form = FiltroTareasForm(request.POST)
        if form.is_valid():
            etiqueta = form.cleaned_data.get('etiqueta')
            estado = form.cleaned_data.get('estado')

            # Aplicar filtros si se han seleccionado
            if etiqueta:
                tareas = tareas.filter(etiqueta=etiqueta)
            if estado:
                tareas = tareas.filter(estado=estado)

    else:
        form = FiltroTareasForm()

    return render(request, 'tareas/lista_tareas.html', {'tareas': tareas, 'form': form})