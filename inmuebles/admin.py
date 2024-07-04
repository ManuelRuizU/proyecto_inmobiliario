# admin.py

# usuarios/admin.py

from django.contrib import admin
from .models import Usuario, Direccion, Propiedad, TipoMoneda

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('user', 'rut', 'direccion', 'telefono', 'tipo_usuario')
    search_fields = ('user__username', 'rut', 'tipo_usuario')

class DireccionAdmin(admin.ModelAdmin):
    list_display = ('pais', 'region', 'ciudad', 'comuna', 'calle', 'numero')
    search_fields = ('pais', 'region', 'ciudad', 'comuna', 'calle')

class PropiedadAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo_inmueble', 'precio_mensual', 'tipo_moneda', 'direccion', 'arrendador')
    search_fields = ('nombre', 'tipo_inmueble', 'direccion__comuna')
    list_filter = ('tipo_inmueble', 'direccion__comuna')

class TipoMonedaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Direccion, DireccionAdmin)
admin.site.register(Propiedad, PropiedadAdmin)
admin.site.register(TipoMoneda, TipoMonedaAdmin)


