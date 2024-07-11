from django.contrib.auth.models import User
from django.db import models


# Usuario
class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rut = models.CharField(max_length=12, unique=True)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    tipo_usuario = models.CharField(max_length=50, choices=[('arrendatario', 'Arrendatario'), ('arrendador', 'Arrendador')])

    def __str__(self):
        return self.user.username

# Direccion
class Direccion(models.Model):
    pais = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    comuna = models.CharField(max_length=100)
    calle = models.CharField(max_length=255)
    numero = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.calle} {self.numero}, {self.comuna}, {self.ciudad}, {self.region}, {self.pais}"

# Moneda de Pago
class TipoMoneda(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


# Propiedad
class Propiedad(models.Model):
    PROPIEDAD_CHOICES = (
        ('Casa', 'Casa'),
        ('Departamento', 'Departamento'),
        ('Parcela', 'Parcela'),
    )

    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    m2_construidos = models.DecimalField(max_digits=10, decimal_places=2)
    m2_terreno = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad_estacionamientos = models.IntegerField()
    cantidad_habitaciones = models.IntegerField()
    cantidad_banos = models.IntegerField()
    direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE)
    tipo_inmueble = models.CharField(max_length=50, choices=PROPIEDAD_CHOICES)
    precio_mensual = models.DecimalField(max_digits=10, decimal_places=1)
    tipo_moneda = models.ForeignKey(TipoMoneda, on_delete=models.CASCADE)
    arrendador = models.ForeignKey('Usuario', on_delete=models.CASCADE, related_name='propiedades')
    numero_departamento = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        if self.tipo_inmueble != 'Departamento':
            self.numero_departamento = None
        super().save(*args, **kwargs)



