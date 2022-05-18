from django.contrib import admin
from .models import Profesor, Alumno, Usuario, Curso, Suscripcion, CursoProfesor, CursoAlumno

# Register your models here.
admin.site.register(Profesor)
admin.site.register(Alumno)
admin.site.register(Usuario)
admin.site.register(Curso)
admin.site.register(Suscripcion)
admin.site.register(CursoProfesor)
admin.site.register(CursoAlumno)
