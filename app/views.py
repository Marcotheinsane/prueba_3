from django.shortcuts import redirect, render, get_object_or_404
from .models import Curso, Matriculas, Sucursal, Alumnos
# Create your views here.


def home(request):
    return render(request, 'home.html')

#crud de cursos
def listar_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'curso/listar_cursos.html', {'cursos': cursos})

def crear_curso(request):
    if request.method == 'POST':
        codigo = request.POST.get('codigo')
        nombre = request.POST.get('nombre')
        valor = request.POST.get('valor')
        curso = Curso(codigo=codigo, nombre=nombre, valor=valor)
        curso.save()
        return redirect('listar_cursos')
    return render(request, 'curso/crear_curso.html')

def editar_curso(request, codigo):
    curso = Curso.objects.get(codigo=codigo)
    if request.method == 'POST':
        curso.nombre = request.POST.get('nombre')
        curso.valor = request.POST.get('valor')
        curso.save()
        return redirect('listar_cursos')
    return render(request, 'curso/editar_curso.html', {'curso': curso})

def eliminar_curso(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    if request.method == 'POST':
        curso.delete()
        return redirect('listar_cursos')
    return render(request, 'curso/eliminar_curso.html', {'curso': curso}) 
def listar_sucursal(request):
    sucursales = Sucursal.objects.all()
    return render(request, 'sucursal/listar_sucursales.html', {'sucursales': sucursales})

def crear_sucursal(request):
    if request.method == 'POST':
        codigo = request.POST.get('codigo')
        nombre = request.POST.get('nombre')
        ciudad = request.POST.get('ciudad')
        sucursal = Sucursal(codigo=codigo, nombre=nombre, ciudad=ciudad)
        sucursal.save()
        return redirect('listar_sucursales')
    return render(request, 'sucursal/crear_sucursal.html')

def editar_sucursal(request, codigo):
    sucursal = Sucursal.objects.get(codigo=codigo)
    if request.method == 'POST':
        sucursal.nombre = request.POST.get('nombre')
        sucursal.ciudad = request.POST.get('ciudad')
        sucursal.save()
        return redirect('listar_sucursales')
    return render(request, 'sucursal/editar_sucursal.html', {'sucursal': sucursal})

def eliminar_sucursal(request, pk):
    sucursal = get_object_or_404(Sucursal, pk=pk)
    if request.method == 'POST':
        sucursal.delete()
        return redirect('listar_sucursales')
    return render(request, 'sucursal/eliminar_sucursal.html', {'sucursal': sucursal}) 
#crud de alumnos

def listar_alumnos(request):
    alumnos = Alumnos.objects.all()
    return render(request, 'alumno/listar_alumnos.html', {'alumnos': alumnos})
def crear_alumno(request):
    if request.method == 'POST':
        rut = request.POST.get('rut')
        nombre = request.POST.get('nombre')
        apellido_paterno = request.POST.get('apellido_paterno')
        direccion = request.POST.get('direccion')
        email = request.POST.get('email')
        fono = request.POST.get('fono')
        alumno = Alumnos(rut=rut, nombre=nombre, apellido_paterno=apellido_paterno, direccion=direccion, email=email, fono=fono)
        alumno.save()
        return redirect('listar_alumnos')
    return render(request, 'alumno/crear_alumno.html')  
def editar_alumno(request, rut):
    alumno = Alumnos.objects.get(rut=rut)
    if request.method == 'POST':
        alumno.nombre = request.POST.get('nombre')
        alumno.apellido_paterno = request.POST.get('apellido_paterno')
        alumno.direccion = request.POST.get('direccion')
        alumno.email = request.POST.get('email')
        alumno.fono = request.POST.get('fono')
        alumno.save()
        return redirect('listar_alumnos')
    return render(request, 'alumno/editar_alumno.html', {'alumno': alumno})

def eliminar_alumno(request, rut):
    alumno = get_object_or_404(Alumnos, rut=rut)
    if request.method == 'POST':
        alumno.delete()
        return redirect('listar_alumnos')
    return render(request, 'alumno/eliminar_alumnos.html', {'alumno': alumno})
#crud de matriculas 
def listar_matriculas(request):
    matriculas = Matriculas.objects.all()
    return render(request, 'matricula/listar_matriculas.html', {'matriculas': matriculas})

def crear_matricula(request):
    if request.method == 'POST':
        codigo = request.POST.get('codigo')
        curso_codigo = request.POST.get('curso_codigo')
        alumno_rut = request.POST.get('alumno_rut')
        sucursal_codigo = request.POST.get('sucursal_codigo')
        fecha = request.POST.get('fecha')
        matricula = Matriculas(codigo=codigo, curso_codigo_id=curso_codigo, alumno_rut_id=alumno_rut, sucursal_codigo_id=sucursal_codigo, fecha=fecha)
        matricula.save()
        return redirect('listar_matriculas')
    cursos = Curso.objects.all()
    alumnos = Alumnos.objects.all()
    sucursales = Sucursal.objects.all()
    return render(request, 'matricula/crear_matricula.html', {'cursos': cursos, 'alumnos': alumnos, 'sucursales': sucursales})

def editar_matricula(request, codigo):
    matricula = Matriculas.objects.get(codigo=codigo)
    if request.method == 'POST':
        matricula.curso_codigo_id = request.POST.get('curso_codigo')
        matricula.alumno_rut_id = request.POST.get('alumno_rut')
        matricula.sucursal_codigo_id = request.POST.get('sucursal_codigo')
        matricula.fecha = request.POST.get('fecha')
        matricula.save()
        return redirect('listar_matriculas')
    cursos = Curso.objects.all()
    alumnos = Alumnos.objects.all()
    sucursales = Sucursal.objects.all()
    return render(request, 'matricula/editar_matricula.html', {'matricula': matricula, 'cursos': cursos, 'alumnos': alumnos, 'sucursales': sucursales})

def eliminar_matricula(request, pk):
    matricula = get_object_or_404(Matriculas, pk=pk)
    if request.method == 'POST':
        matricula.delete()
        return redirect('listar_matriculas')
    return render(request, 'matricula/eliminar_matricula.html', {'matricula': matricula}) 