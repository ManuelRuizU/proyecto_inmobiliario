"""
URL configuration for proyecto_inmobiliario project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# urls.py
from django.contrib import admin
from django.urls import path
from inmuebles import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('contacto/', views.contenido, {'tipo': 'contacto'}, name='contacto'),  # Ruta específica para el formulario de contacto
    path('<str:tipo>/', views.contenido, name='contenido'),  # Ruta genérica para otros tipos de contenido
    path('', views.contenido, {'tipo': 'index'}, name='index'),  # Ruta para la página de inicio
]


