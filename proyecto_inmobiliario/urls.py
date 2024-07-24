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
from inmuebles.views import contenido, propiedades_arrendador, propiedades_favoritas, agregar_propiedad, editar_propiedad, eliminar_propiedad

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contacto/', views.contenido, {'tipo': 'contacto'}, name='contacto'),  # Ruta específica para el formulario de contacto
    path('login/', views.contenido, {'tipo': 'login'}, name='login'),  # Ruta específica para el login
    path('register/', views.contenido, {'tipo': 'register'}, name='register'),  # Ruta específica para el registro
    path('profile/', views.contenido, {'tipo': 'profile'}, name='profile'),  # Ruta específica para el perfil
    path('edit_profile/', views.contenido, {'tipo': 'edit_profile'}, name='edit_profile'),  # Ruta específica para editar el perfil
    path('logout/', views.contenido, {'tipo': 'logout'}, name='logout'),  # Ruta específica para logout
    path('propiedades-arrendador/', propiedades_arrendador, name='propiedades_arrendador'),  # Ruta para listar propiedades de arrendador
    path('propiedades-favoritas/', propiedades_favoritas, name='propiedades_favoritas'),  # Ruta para listar propiedades favoritas de arrendatario
    path('agregar-propiedad/', agregar_propiedad, name='agregar_propiedad'),  # Ruta para agregar una propiedad
    path('editar-propiedad/<int:pk>/', editar_propiedad, name='editar_propiedad'),  # Ruta para editar una propiedad
    path('eliminar-propiedad/<int:pk>/', eliminar_propiedad, name='eliminar_propiedad'),  # Ruta para eliminar una propiedad
    path('<str:tipo>/', views.contenido, name='contenido'),  # Ruta genérica para otros tipos de contenido
    path('', views.contenido, {'tipo': 'index'}, name='index'),  # Ruta para la página de inicio
    path('agregar-favorito/<int:pk>/', views.agregar_favorito_view, name='agregar_favorito'), # Ruta para agregar una propiedad a fsvorito
    path('eliminar-favorito/<int:pk>/', views.eliminar_favorito_view, name='eliminar_favorito') # Ruta para eliminar una propiedad de favorito
]



