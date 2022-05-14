from django import views
from django.urls import URLPattern, path
from django.urls import path
from .views import home, inicios, registro, matricula, cursos
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
    path('cursos/', cursos,name="cursos1"),
]