from django.shortcuts import redirect, render
from .models import Curso
# Create your views here.


def home(request):
    return render(request, 'home.html')

<<<<<<< Updated upstream

=======
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
>>>>>>> Stashed changes
