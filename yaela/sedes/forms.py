from django import forms
from .models import Sede, Campo

class SedeForm(forms.ModelForm):
    class Meta:
        model = Sede
        fields = ['sede', 'direccion', 'idusuario', 'descripcion']

class CampoForm(forms.ModelForm):
    class Meta:
        model = Campo
        fields = ['campo', 'idsede', 'idtipocampo']
