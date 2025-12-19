from django.db import models

class Curso(models.Model):
    codigo = models.IntegerField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=120)
    valor = models.IntegerField(max_length=10)
    
    def __str__(self):
        return self.nombre

class Alumnos(models.Model):
    rut = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido_paterno = models.CharField(max_length=80)
    apellido_paterno = models.CharField(max_length=80)
    direccion = models.CharField(max_length=120)
    email = models.EmailField(max_length=80)
    fono = models.CharField(max_length=12)
    
    def __str__(self):
        return self.nombre
    
class Sucursal(models.Model):
    codigo = models.IntegerField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=120)
    ciudad = models.CharField(max_length=80)
    
    def __str__(self):
        return self.nombre
    
class Matriculas(models.Model):
    codigo = models.IntegerField(max_length=10, primary_key=True)
    curso_codigo = models.ForeignKey(Curso, on_delete=models.CASCADE)
    alumno_rut = models.ForeignKey(Alumnos, on_delete=models.CASCADE)
    sucursal_codigo = models.ForeignKey(Sucursal, on_delete=models.CASCADE)
    fecha = models.DateField()
    