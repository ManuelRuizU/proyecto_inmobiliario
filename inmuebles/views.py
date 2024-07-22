# views.py

from django.shortcuts import render, redirect
from .services import handle_login, handle_register, handle_edit_profile, handle_logout

def contenido(request, tipo):
    if tipo == 'index':
        return render(request, 'index.html', {})
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
    else:
        return render(request, 'error.html', {})

