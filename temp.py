
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proyecto_inmobiliario.settings')
django.setup()

from inmuebles.models import Propiedad

def consulta_inmuebles_por_comunas():
    comunas = Propiedad.objects.values_list('direccion__comuna', flat=True).distinct()
    with open('inmuebles_por_comunas.txt', 'w') as file:
        for comuna in comunas:
            inmuebles = Propiedad.objects.filter(direccion__comuna=comuna).values('nombre', 'descripcion')
            file.write(f"Comuna: {comuna}\n")
            for inmueble in inmuebles:
                file.write(f" - Nombre: {inmueble['nombre']}, Descripción: {inmueble['descripcion']}\n")
            file.write("\n")

if __name__ == "__main__":
    consulta_inmuebles_por_comunas()


from inmuebles.models import Propiedad

def consulta_inmuebles_por_regiones():
    regiones = Propiedad.objects.values_list('direccion__region', flat=True).distinct()
    with open('inmuebles_por_regiones.txt', 'w') as file:
        for region in regiones:
            inmuebles = Propiedad.objects.filter(direccion__region=region).values('nombre', 'descripcion')
            file.write(f"Región: {region}\n")
            for inmueble in inmuebles:
                file.write(f" - Nombre: {inmueble['nombre']}, Descripción: {inmueble['descripcion']}\n")
            file.write("\n")

if __name__ == "__main__":
    consulta_inmuebles_por_regiones()