# services.py

from django.db import IntegrityError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .forms import EditProfileForm, UserForm, CustomUserCreationForm
from .models import Usuario

def handle_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return True, None
        return False, form
    form = AuthenticationForm()
    return False, form

def handle_register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            try:
                user = form.save()
                Usuario.objects.create(
                    user=user,
                    rut=form.cleaned_data['rut'],
                    direccion=form.cleaned_data['direccion'],
                    telefono=form.cleaned_data['telefono'],
                    tipo_usuario=form.cleaned_data['tipo_usuario']
                )
                login(request, user)
                return True, None
            except IntegrityError:
                form.add_error('rut', 'Este RUT ya está registrado.')
                user.delete()  # Eliminar el usuario creado si ocurre un error
        return False, form
    form = CustomUserCreationForm()
    return False, form

def handle_edit_profile(request):
    user = request.user
    usuario = user.usuario  # Obtener el perfil del usuario
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=user)
        profile_form = EditProfileForm(request.POST, instance=usuario)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return True, None, None
        return False, user_form, profile_form
    user_form = UserForm(instance=user)
    profile_form = EditProfileForm(instance=usuario)
    return False, user_form, profile_form

def handle_logout(request):
    logout(request)

