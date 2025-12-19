from django.shortcuts import redirect, render
from .models import Curso, Sucursal
# Create your views here.


def home(request):
    return render(request, 'home.html')

<<<<<<< Updated upstream


=======
>>>>>>> Stashed changes
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

def eliminar_curso(request, codigo):
    curso = Curso.objects.get(codigo=codigo)
    curso.delete()
    return redirect('listar_cursos')

<<<<<<< Updated upstream
=======
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

def eliminar_sucursal(request, codigo):
    sucursal = Sucursal.objects.get(codigo=codigo)
    sucursal.delete()
    return redirect('listar_sucursales')
>>>>>>> Stashed changes
