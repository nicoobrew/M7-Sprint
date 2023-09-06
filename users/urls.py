from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = "users"

urlpatterns = [

    # Pagina de registro
    path('registro/', views.registrarse, name='registro'),
    # Página de login
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    # Página de logout
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('cerrar-sesion/', views.cerrar_sesion, name='salir')
]