# views.py
from django.shortcuts import render

def contenido(request, tipo):
    if tipo == 'index':
        return render(request, 'index.html', {})
    elif tipo == 'nosotros':
        return render(request, 'nosotros.html', {})
    elif tipo == 'contacto':
        return render(request, 'contacto.html', {})
    
    else:
        # Manejar casos no válidos (por ejemplo, mostrar un error 404)
        return render(request, 'error.html', {})

