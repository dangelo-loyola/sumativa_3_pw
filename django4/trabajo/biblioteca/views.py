from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Cliente
from datetime import datetime
from django.contrib import messages
from django.shortcuts import render, redirect
from rest_framework import generics
from .models import Item
from .serializer import ItemSerializer



def iniciar_sesion(request):
    if request.method == 'POST':
        username = request.POST['username']
        contraseña = request.POST['contraseña']  # Cambio aquí
        cliente = authenticate(request, username=username, contraseña=contraseña)
        if Cliente is not None:
            login(request, Cliente)
            messages.success(request, '¡Inicio de sesión exitoso!')
            return redirect('index')  # Cambia 'index' por la URL a la que quieras redirigir después del inicio de sesión
        else:
            messages.error(request, 'Nombre de usuario o contraseña incorrectos.')
    return render(request, 'inicio_de_sesion.html')

# Vistas basadas en clases

# Vistas basadas en funciones
def index(request):
    return render(request, "index.html")

def accion(request):
    return render(request, 'accion.html')

def aventura(request):
    return render(request, 'aventura.html')

def categoria(request):
    return render(request, 'categoria.html')

def comentarios_de_clientes(request):
    return render(request, 'comentarios_de_clientes.html')

def contacto(request):
    return render(request, 'contacto.html')

def estrategia(request):
    return render(request, 'estrategia.html')

def inicio_de_sesion(request):
    return render(request, 'inicio_de_sesion.html')

def olvide_contraseña(request):
    return render(request, 'olvide_contraseña.html')

def quienes_somos(request):
    return render(request, 'quienes_somos.html')

def rol(request):
    return render(request, 'rol.html')

def terror(request):
    return render(request, 'terror.html')


def registro_usuario(request):
    if request.method == 'POST':
        # Obtener los datos del formulario
        email = request.POST.get('email')
        nombre_usuario = request.POST.get('nombre_usuario')
        nombre_completo = request.POST.get('nombre_completo')
        fecha_nacimiento_str = request.POST.get('fechaNacimiento')  # Obtener fecha en formato texto
        fecha_nacimiento = datetime.strptime(fecha_nacimiento_str, '%Y-%m-%d').date()  # Convertir a formato de fecha de Python
        direccion = request.POST.get('direccion')
        contraseña = request.POST.get('contraseña')

        # Crear una instancia del modelo Cliente con los datos del formulario
        cliente = Cliente.objects.create(
            email=email,
            nombre_usuario=nombre_usuario,
            nombre_completo=nombre_completo,
            fecha_nacimiento=fecha_nacimiento,
            direccion=direccion,
            contraseña=contraseña
        )

        # Guardar el cliente en la base de datos
        cliente.set_password(contraseña)
        cliente.save()

    # Renderizar el formulario si el método de la solicitud es GET
    return render(request, 'registro_usuario.html')


class ItemListCreate(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    