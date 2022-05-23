from django import forms
from django.forms import ModelForm
from .models import Curso

class CursoForm(ModelForm):
    class Meta:
        model = Curso
        fields = ['nro_curso', 'anno_curso', 'letra', 'cant_alumnos']

    nro_curso = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    anno_curso = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    letra = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    cant_alumnos = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}))