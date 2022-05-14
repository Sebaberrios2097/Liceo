from django.shortcuts import render
from .models import Alumno, Profesor
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

def registrarMatricula(request):
    Rut_Alumno=request.POST['rutAlumno']
    Dv_Alumno=request.POST['dvAlumno']
    PnomAlumno=request.POST['PnomAlumno']
    SnomAlumno=request.POST['SnomAlumno']    
    AppAlumno=request.POST['appAlumno']
    ApmAlumno=request.POST['apmAlumno']
    nacAlumno=request.POST['nacAlumno']
    Email_Alumno=request.POST['correoAlumno']
    motivoAlumno=request.POST['motivoAlumno']
    nomApoderado=request.POST['nomApoderado']
    apApoderado=request.POST['apApoderado']
    correoApoderado=request.POST['correoApoderado']
    
    
    alumno=Alumno.objects.create(run_alumno=Rut_Alumno,dv_alumno=Dv_Alumno,prim_nom_alumno=PnomAlumno,seg_nom_alumno=SnomAlumno,
                                ap_pat_alumno=AppAlumno,ap_mat_alumno=ApmAlumno,fec_nac_alumno=nacAlumno,correo_alumno=Email_Alumno,
                                motivo_matricula=motivoAlumno,nombres_apoderado=nomApoderado,apellidos_apoderado=apApoderado,correo_apoderado=correoApoderado)
    return redirect('/')
