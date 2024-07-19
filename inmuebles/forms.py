# forms.py

from django import forms
from .models import Propiedad, Direccion

class PropiedadForm(forms.ModelForm):
    class Meta:
        model = Propiedad
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(PropiedadForm, self).__init__(*args, **kwargs)
        self.fields['direccion'].queryset = Direccion.objects.all()
