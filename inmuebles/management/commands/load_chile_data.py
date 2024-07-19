
import json
from django.core.management.base import BaseCommand
from inmuebles.models import Direccion

class Command(BaseCommand):
    help = 'Load data from chile.json'

    def handle(self, *args, **options):
        with open('inmuebles/json/chile.json', encoding='utf-8') as file:
            data = json.load(file)

            for region in data['regions']:
                nombre_region = region['name']
                
                for comuna in region['comunas']:
                    nombre_comuna = comuna['name']
                    # Crear una dirección con calle y número en blanco
                    direccion, created = Direccion.objects.get_or_create(
                        pais='Chile',
                        region=nombre_region,
                        ciudad='',  # Ciudad en blanco
                        comuna=nombre_comuna,
                        calle='',  # Calle en blanco
                        numero=''  # Número en blanco
                    )
                    if created:
                        self.stdout.write(self.style.SUCCESS(f'Dirección para comuna "{nombre_comuna}" en región "{nombre_region}" creada.'))
                    else:
                        self.stdout.write(self.style.WARNING(f'Dirección para comuna "{nombre_comuna}" en región "{nombre_region}" ya existe.'))

