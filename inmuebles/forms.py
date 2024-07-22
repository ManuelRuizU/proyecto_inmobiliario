# forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Propiedad, Direccion, Usuario
from django.contrib.auth.models import User

class PropiedadForm(forms.ModelForm):
    class Meta:
        model = Propiedad
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(PropiedadForm, self).__init__(*args, **kwargs)
        self.fields['direccion'].queryset = Direccion.objects.all()

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['rut', 'direccion', 'telefono', 'tipo_usuario']

class CustomUserCreationForm(UserCreationForm):
    tipo_usuario = forms.ChoiceField(choices=[('arrendatario', 'Arrendatario'), ('arrendador', 'Arrendador')])
    rut = forms.CharField(max_length=12)
    direccion = forms.CharField(max_length=255)
    telefono = forms.CharField(max_length=20)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'tipo_usuario', 'rut', 'direccion', 'telefono']

    def clean_rut(self):
        rut = self.cleaned_data.get('rut')
        if Usuario.objects.filter(rut=rut).exists():
            raise forms.ValidationError('Este RUT ya está registrado.')
        return rut


