# views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .services import handle_login, handle_register, handle_edit_profile, handle_logout
from .services import (
    obtener_usuario, obtener_propiedades_arrendador, obtener_propiedades_favoritas,
    agregar_propiedad_logic, editar_propiedad_logic, eliminar_propiedad_logic
)
from .models import Propiedad, Usuario
from .forms import PropiedadForm
from .services import agregar_favorito, eliminar_favorito

def contenido(request, tipo):
    if tipo == 'index':
        propiedades = Propiedad.objects.all()
        return render(request, 'index.html', {'propiedades': propiedades})
    elif tipo == 'nosotros':
        return render(request, 'nosotros.html', {})
    elif tipo == 'contacto':
        return render(request, 'contacto.html', {})
    elif tipo == 'login':
        success, form = handle_login(request)
        if success:
            return redirect('profile')
        return render(request, 'registration/login.html', {'form': form})
    elif tipo == 'register':
        success, form = handle_register(request)
        if success:
            return redirect('profile')
        return render(request, 'registration/register.html', {'form': form})
    elif tipo == 'profile':
        if request.user.is_authenticated:
            return render(request, 'registration/profile.html')
        return redirect('login')
    elif tipo == 'edit_profile':
        if request.user.is_authenticated:
            success, user_form, profile_form = handle_edit_profile(request)
            if success:
                return redirect('profile')
            return render(request, 'registration/edit_profile.html', {'user_form': user_form, 'profile_form': profile_form})
        return redirect('login')
    elif tipo == 'logout':
        handle_logout(request)
        return redirect('login')
    elif tipo == 'propiedades_arrendador':
        return propiedades_arrendador(request)
    elif tipo == 'propiedades_favoritas':
        return propiedades_favoritas(request)
    elif tipo == 'agregar_propiedad':
        return agregar_propiedad(request)
    elif tipo == 'editar_propiedad':
        return editar_propiedad(request, request.GET.get('pk'))
    elif tipo == 'eliminar_propiedad':
        return eliminar_propiedad(request, request.GET.get('pk'))
    else:
        return render(request, 'error.html', {})



"""
def contenido(request, tipo):
    if tipo == 'index':
        propiedades = Propiedad.objects.all
        return render(request, 'index.html', {'propiedades': propiedades})
    elif tipo == 'nosotros':
        return render(request, 'nosotros.html', {})
    elif tipo == 'contacto':
        return render(request, 'contacto.html', {})
    elif tipo == 'login':
        success, form = handle_login(request)
        if success:
            return redirect('profile')
        return render(request, 'registration/login.html', {'form': form})
    elif tipo == 'register':
        success, form = handle_register(request)
        if success:
            return redirect('profile')
        return render(request, 'registration/register.html', {'form': form})
    elif tipo == 'profile':
        if request.user.is_authenticated:
            return render(request, 'registration/profile.html')
        return redirect('login')
    elif tipo == 'edit_profile':
        if request.user.is_authenticated:
            success, user_form, profile_form = handle_edit_profile(request)
            if success:
                return redirect('profile')
            return render(request, 'registration/edit_profile.html', {'user_form': user_form, 'profile_form': profile_form})
        return redirect('login')
    elif tipo == 'logout':
        handle_logout(request)
        return redirect('login')
    elif tipo == 'propiedades_arrendador':
        return propiedades_arrendador(request)
    elif tipo == 'propiedades_favoritas':
        return propiedades_favoritas(request)
    elif tipo == 'agregar_propiedad':
        return agregar_propiedad(request)
    elif tipo == 'editar_propiedad':
        return editar_propiedad(request, request.GET.get('pk'))
    elif tipo == 'eliminar_propiedad':
        return eliminar_propiedad(request, request.GET.get('pk'))
    else:
        return render(request, 'error.html', {})
"""

@login_required
def propiedades_arrendador(request):
    usuario = obtener_usuario(request)
    if usuario.tipo_usuario == 'arrendador':
        propiedades = obtener_propiedades_arrendador(usuario)
        return render(request, 'registration/propiedades_arrendador.html', {'propiedades': propiedades})
    return redirect('index')

@login_required
def propiedades_favoritas(request):
    usuario = obtener_usuario(request)
    if usuario.tipo_usuario == 'arrendatario':
        propiedades = obtener_propiedades_favoritas(usuario)
        return render(request, 'registration/propiedades_favoritas.html', {'propiedades': propiedades})
    return redirect('login')

@login_required
def agregar_propiedad(request):
    usuario = obtener_usuario(request)
    if usuario.tipo_usuario == 'arrendador':
        success, form = agregar_propiedad_logic(request, usuario)
        if success:
            return redirect('propiedades_arrendador')
        return render(request, 'registration/agregar_propiedad.html', {'form': form})
    return redirect('login')

@login_required
def editar_propiedad(request, pk):
    propiedad = get_object_or_404(Propiedad, pk=pk)
    if request.user == propiedad.arrendador.user:
        success, form = editar_propiedad_logic(request, propiedad)
        if success:
            return redirect('propiedades_arrendador')
        return render(request, 'registration/editar_propiedad.html', {'form': form})
    return redirect('login')

@login_required
def eliminar_propiedad(request, pk):
    propiedad = get_object_or_404(Propiedad, pk=pk)
    if request.user == propiedad.arrendador.user:
        if request.method == 'POST':
            eliminar_propiedad_logic(propiedad)
            return redirect('propiedades_arrendador')
        return render(request, 'registration/eliminar_propiedad.html', {'propiedad': propiedad})
    return redirect('login')


@login_required
def agregar_favorito_view(request, pk):
    usuario = obtener_usuario(request)
    propiedad = get_object_or_404(Propiedad, pk=pk)
    agregar_favorito(usuario, propiedad)
    return redirect('propiedades_favoritas')

@login_required
def eliminar_favorito_view(request, pk):
    usuario = obtener_usuario(request)
    propiedad = get_object_or_404(Propiedad, pk=pk)
    eliminar_favorito(usuario, propiedad)
    return redirect('propiedades_favoritas')

