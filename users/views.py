from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import RegistroUsuarioForm
from django.contrib.auth.models import Group



# def registrarse(request):
#     if request.method == 'POST':
#         form = RegistroUsuarioForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             # Iniciar sesión automáticamente después del registro
#             login(request, user)
#             return redirect('tareas/bienvenido.html')  # Redireccionar a la página de lista de tareas
#     else:
#         form = RegistroUsuarioForm()
#     return render(request, 'users/registro.html', {'form': form})

def registrarse(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()

            # Obtener el grupo de "Usuarios"
            user_group = Group.objects.get(name='usuario')
            user.groups.add(user_group)

            # Iniciar sesión automáticamente después del registro
            login(request, user)
            return redirect('tareas:bienvenido')  # Redireccionar a la página de lista de tareas
    else:
        form = RegistroUsuarioForm()
    return render(request, 'users/registro.html', {'form': form})

def iniciar_sesion(request):
    login(request)
    return redirect('tareas:bienvenido')

def cerrar_sesion(request):
    logout(request)
    return redirect('usuarios:salir')


