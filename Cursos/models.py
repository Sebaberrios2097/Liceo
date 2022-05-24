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

    def obtenerNomProfesor(self):
        return "{} {}, {} {}".format(self.ap_pat_prof, self.ap_mat_prof, self.prim_nom_prof, self.seg_nom_prof)

    def __str__(self):
        return self.obtenerNomProfesor()

    class Meta:
        verbose_name="Profesor"
        verbose_name_plural="Profesores"
        db_table="Profesor"

class Alumno(models.Model):
    id_alumno = models.AutoField(primary_key=True, null=False)
    run_alumno = models.IntegerField(null=False)
    dv_alumno = models.CharField(max_length=1, null=False)
    prim_nom_alumno = models.CharField(max_length=15, null=False)
    seg_nom_alumno = models.CharField(max_length=15, null=False)
    ap_pat_alumno = models.CharField(max_length=15, null=False)
    ap_mat_alumno = models.CharField(max_length=15, null=False)
    fec_nac_alumno = models.DateField(null=False)
    correo_alumno = models.CharField(max_length=50, null=False)
    motivo_matricula = models.CharField(max_length=250, null=False)
    nombres_apoderado = models.CharField(max_length=25, null=False)
    apellidos_apoderado = models.CharField(max_length=25, null=False)
    correo_apoderado = models.CharField(max_length=30, null=False)
    ingresado = models.BooleanField(blank=True, null=True)
    imagen_alumno = models.ImageField(blank=True, upload_to = "media", default = 'Fotos/static/images/no-img.jpg')
    
    def obtenerNomAlumno(self):
        return "{} {}, {} {}".format(self.ap_pat_alumno, self.ap_mat_alumno, self.prim_nom_alumno, self.seg_nom_alumno)

    def __str__(self):
        return self.obtenerNomAlumno()

    class Meta:
        verbose_name="Alumno"
        verbose_name_plural="Alumnos"
        db_table="Alumno"

class Usuario(models.Model):
    idusuario = models.AutoField(primary_key=True, null=False, blank=False)
    nomusuario = models.CharField(max_length=20, null=False, blank=False)
    contrausuario = models.CharField(max_length=20, null=False, blank=False)
    profesor = models.BooleanField(null=False)
    id_alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE, null=True, blank=True)
    id_profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE, null=True, blank=True)

    def mostrarUsuario(self):
        return "{}".format(self.nomusuario)

    def __str__(self):
        return self.mostrarUsuario()

    class Meta:
        verbose_name= 'Usuario'
        verbose_name_plural = 'Usuarios'
        db_table = 'Usuario'

class Curso(models.Model):
    id_curso = models.AutoField(primary_key=True, null=False)
    nro_curso = models.IntegerField(null=False)
    anno_curso = models.IntegerField(null=False)
    letra = models.CharField(max_length=1, null=False)
    cant_alumnos = models.IntegerField(null=False)

    def MostrarCurso(self):
        return "{} {}, {}".format(self.nro_curso, self.letra, self.anno_curso)
    
    def __str__(self):
        return self.MostrarCurso()
    
    class Meta:
        verbose_name='Curso'
        verbose_name_plural='Cursos'
        db_table='Curso'


class CursoProfesor(models.Model):
    id_cursoprofesor = models.AutoField(primary_key=True, null=False)
    prof_jefe = models.BooleanField(null=True)
    id_profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    id_curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    def cursoxprofesor(self):
        return "{} {}".format(self.id_curso, self.id_profesor)
    
    def __str__(self):
        return self.cursoxprofesor()
    
    class Meta:
        verbose_name="Curso x Profesor"
        verbose_name_plural="Curso x Profesor"
        db_table="CursoProfesor"

class CursoAlumno(models.Model):
    id_cursoalumno = models.AutoField(primary_key=True, null=False)
    id_alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    id_curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    def strCursoAlumno(self):
        return "{}, {}".format(self.id_alumno, self.id_curso)

    def __str__(self):
        return self.strCursoAlumno()
    
    class Meta:
        verbose_name="Curso x Alumno"
        verbose_name_plural="Curso x Alumno"
        db_table="CursoAlumno"

class Suscripcion(models.Model):
    id_suscripcion = models.AutoField(primary_key=True, null=False)
    correo = models.CharField(max_length=50, null=False)

    def strSuscripcion(self):
        return "{}".format(self.correo)

    def __str__(self):
        return self.strSuscripcion()

    class Meta:
        verbose_name="Suscripción"
        verbose_name_plural="Suscripciones"
        db_table="Suscripcion"

class TipoAlmuerzo(models.Model):
    id_tipo_almuerzo = models.AutoField(primary_key=True, blank=False, null=False)
    nombre_tipo_almuerzo = models.CharField(max_length=100, null=False, blank=False)

    def strTipoAlmuerzo(self):
        return "{}".format(self.nombre_tipo_almuerzo)
    
    def __str__(self):
        return self.strTipoAlmuerzo()
    
    class Meta:
        verbose_name = "Tipo de Almuerzo"
        verbose_name_plural = "Tipos de almuerzo"
        db_table = "TipoAlmuerzo"

class Almuerzo(models.Model):
    id_almuerzo = models.AutoField(primary_key=True, blank=False, null=False)
    nombre_almuerzo = models.CharField(max_length=100, null=False, blank=False)
    descripcion_almuerzo = models.CharField(max_length=500, null=False, blank=False)
    id_tipo_almuerzo = models.ForeignKey(TipoAlmuerzo, on_delete=models.CASCADE)
    
    def strAlmuerzo(self):
        return "{}/Tipo: {}".format(self.nombre_almuerzo, self.id_tipo_almuerzo)

    def __str__(self):
        return self.strAlmuerzo()

    class Meta:
        verbose_name="Almuerzo"
        verbose_name_plural="Almuerzos"
        db_table="Almuerzo"