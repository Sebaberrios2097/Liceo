from contextlib import nullcontext
from tokenize import blank_re
from turtle import st
from django.db import models

# Create your models here.
class Profesor(models.Model):
    id_profesor = models.AutoField(primary_key=True, null=False, blank=False)
    run_profesor = models.IntegerField(null=False, blank=False)
    dv_profesor = models.CharField(max_length=1, null=False, blank=False)
    prim_nom_prof = models.CharField(max_length=15, null=False, blank=False)
    seg_nom_prof = models.CharField(max_length=15, null=True, blank=False)
    ap_pat_prof = models.CharField(max_length=15, null=False, blank=False)
    ap_mat_prof = models.CharField(max_length=15, null=False, blank=False)
    fec_nac_prof = models.DateField(null=False)
    correo_profesor = models.CharField(max_length=50, null=False)
    imagen_profesor = models.ImageField(blank=True, upload_to = "media", default = 'Fotos/static/images/no-img.jpg')

    def __str__(self):
        return self.prim_nom_prof + ' ' + self.seg_nom_prof + ' ' + self.ap_pat_prof + ' ' + self.ap_mat_prof

class Alumno(models.Model):
    id_alumno = models.AutoField(primary_key=True, null=False)
    run_alumno = models.IntegerField(null=False)
    dv_alumno = models.CharField(max_length=1, null=False)
    prim_nom_alumno = models.CharField(max_length=15, null=False)
    seg_nom_alumno = models.CharField(max_length=15, null=False)
    ap_pat_alumno = models.CharField(max_length=15, null=False)
    ap_mat_alumno = models.CharField(max_length=15, null=False)
    fec_nac_alumno = models.DateField(null=False)
    correo_alumno = models.CharField(max_length=30, null=False)
    motivo_matricula = models.CharField(max_length=250, null=False)
    nombres_apoderado = models.CharField(max_length=25, null=False)
    apellidos_apoderado = models.CharField(max_length=25, null=False)
    correo_apoderado = models.CharField(max_length=30, null=False)
    ingresado = models.BooleanField(blank=True, null=True)
    imagen_alumno = models.ImageField(blank=True, upload_to = "media", default = 'Fotos/static/images/no-img.jpg')
    
    def __str__(self):
        return self.prim_nom_alumno + ' ' + self.seg_nom_alumno + ' ' + self.ap_pat_alumno + ' ' + self.ap_mat_alumno

class Usuario(models.Model):
    idusuario = models.AutoField(primary_key=True, null=False, blank=False)
    nomusuario = models.CharField(max_length=20, null=False, blank=False)
    contrausuario = models.CharField(max_length=20, null=False, blank=False)
    profesor = models.BooleanField(null=False)
    id_alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE, null=True, blank=True)
    id_profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nomusuario

class Curso(models.Model):
    id_curso = models.AutoField(primary_key=True, null=False)
    nro_curso = models.IntegerField(null=False)
    anno_curso = models.IntegerField(null=False)
    letra = models.CharField(max_length=1, null=False)
    cant_alumnos = models.IntegerField(null=False)

    def __str__(self):
        return str(self.nro_curso ) + str(self.letra ) + ' ' + str(self.anno_curso)

class CursoProfesor(models.Model):
    id_cursoprofesor = models.AutoField(primary_key=True, null=False)
    prof_jefe = models.BooleanField(null=True)
    id_profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    id_curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

class CursoAlumno(models.Model):
    id_cursoalumno = models.AutoField(primary_key=True, null=False)
    id_alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    id_curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

class Suscripcion(models.Model):
    id_suscripcion = models.AutoField(primary_key=True, null=False)
    correo = models.CharField(max_length=50, null=False)