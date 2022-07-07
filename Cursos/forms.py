from django import forms
from django.forms import ModelForm
from .models import Curso, Almuerzo

class CursoForm(ModelForm):
    class Meta:
        model = Curso
        fields = ['nro_curso', 'anno_curso', 'letra', 'cant_alumnos']

    nro_curso = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    anno_curso = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    letra = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    cant_alumnos = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}))

class AlmuerzoForm(ModelForm):
    class Meta:
        model = Almuerzo
        fields = ['id_almuerzo', 'nombre_almuerzo', 'descripcion_almuerzo', 'id_tipo_almuerzo']

    id_almuerzo = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    nombre_almuerzo = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    descripcion_almuerzo = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    id_tipo_almuerzo = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}))