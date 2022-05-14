from django.shortcuts import render
from .models import Profesor
from django.shortcuts import render,redirect

# Create your views here.

def home(request):   
    return render(request, 'Cursos/index.html')

def inicios(request):   
    return render(request, 'Cursos/iniciosesion.html')

def registro(request):   
    return render(request, 'Cursos/registrar.html')

def matricula(request):   
    return render(request, 'Cursos/matricula.html')

def cursos(request):
    profesores = Profesor.objects.all()
    return render(request, "Cursos/cursos.html", {"profesores": profesores})