from django import views
from django.urls import URLPattern, path
from django.urls import path

from .views import eliminar_curso, home, inicios, registro, matricula, Almuerzos, cursoxprofesor, registrarMatricula, registrarSuscripcion, agregar_curso, modificar_curso, cursos, listar_almuerzos, Login
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from Cursos import views


urlpatterns = [
    path('', home,name="home"),
    path('inicio/', inicios,name="inicios1"),
    path('registro/', registro,name="registro1"),
    path('matricula/', matricula,name="matricula1"),
    path('Almuerzos/', Almuerzos,name="Almuerzos1"),
    path('cursoxprofesor/', cursoxprofesor,name="cursoxprofesor"),
    path('registrarMatricula/', registrarMatricula),
    path('registrarSuscripcion/', registrarSuscripcion),
    path('listar_almuerzos/', listar_almuerzos,name="listar_almuerzos"),
    path('agregar_curso/', agregar_curso, name='agregar_curso'),
    path('modificar_curso/<id>', modificar_curso, name='form_mod_curso'),
    path('eliminar_curso/<id>', eliminar_curso, name='eliminar_curso'),
    path('cursos/', cursos, name='cursos1'),
    path('login/', Login, name='login')


]