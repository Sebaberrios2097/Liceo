from django.shortcuts import render
from .models import Alumno, CursoProfesor, Suscripcion, Curso, Almuerzo
from django.shortcuts import render,redirect
from .forms import CursoForm

# Create your views here.

def home(request):   
    cursos = Curso.objects.all()
    datos = {
        'cursos':cursos
    }
    return render(request, 'Cursos/index.html', datos)

def inicios(request):   
    return render(request, 'Cursos/iniciosesion.html')

def registro(request):   
    return render(request, 'Cursos/registrar.html')

def matricula(request):   
    return render(request, 'Cursos/matricula.html')

def Almuerzos(request):   
    return render(request, 'Cursos/Almuerzos.html')
    
def Login(request):   
    return render(request, 'Cursos/login.html')

def cursoxprofesor(request):
    cursoxprofesor = CursoProfesor.objects.all()
    return render(request, "Cursos/cursos.html", {"cursoxprofesor": cursoxprofesor})

def cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'Cursos/lista_cursos.html', {'cursos': cursos})

def listar_almuerzos(request):
    Almuerzos = Almuerzo.objects.all()
    return render(request, 'Cursos/Almuerzos.html', {'Almuerzo': Almuerzos})

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

def registrarSuscripcion(request):
    correo=request.POST['correo']

    suscripcion=Suscripcion.objects.create(correo=correo)
    return redirect('/')

def agregar_curso(request):
    curso = Curso.objects.all()
    datos = {
        'form':CursoForm(),
        'cursos': curso
    }

    if(request.method == 'POST'):
        formulario = CursoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = 'Se guardó correctamente'
            return redirect('cursos1')
    return render(request, 'Cursos/form_curso.html', datos)

def modificar_curso(request, id):
    curso = Curso.objects.get(id_curso = id)

    datos = {
        'form': CursoForm(instance = curso)
    }

    if request.method == 'POST':
        formulario = CursoForm(data = request.POST, instance = curso)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = 'Se modificó el curso'
            return redirect('cursos1')
        else:
            datos['mensaje'] = 'No se modificó el curso'
    return render(request,"Cursos/form_mod_curso.html", datos)

def eliminar_curso(request, id):
    curso = Curso.objects.get(id_curso = id)
    curso.delete()

    return redirect('cursos1')