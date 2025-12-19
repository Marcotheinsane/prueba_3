from django import forms
from .models import Curso, Alumnos, Sucursal, Matriculas

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['codigo', 'nombre', 'valor']
        widgets = {
            'codigo': forms.NumberInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'valor': forms.NumberInput(attrs={'class': 'form-control'}),
        }
        
class AlumnosForm(forms.ModelForm):
    class Meta:
        model = Alumnos
        fields = ['rut', 'nombre', 'apellido_paterno', 'apellido_materno', 'direccion', 'email', 'fono']
        widgets = {
            'rut': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido_paterno': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido_materno': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'fono': forms.TextInput(attrs={'class': 'form-control'}),
        }
    
class SucursalForm(forms.ModelForm):
    class Meta:
        model = Sucursal
        fields = ['codigo', 'nombre', 'ciudad']
        widgets = {
            'codigo': forms.NumberInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'ciudad': forms.TextInput(attrs={'class': 'form-control'}),
        }

class MatriculasForm(forms.ModelForm):
    class Meta:
        model = Matriculas
        fields = ['codigo', 'curso_codigo', 'alumno_rut', 'sucursal_codigo', 'fecha']
        widgets = {
            'codigo': forms.NumberInput(attrs={'class': 'form-control'}),
            'curso_codigo': forms.Select(attrs={'class': 'form-control'}),
            'alumno_rut': forms.Select(attrs={'class': 'form-control'}),
            'sucursal_codigo': forms.Select(attrs={'class': 'form-control'}),
            'fecha': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }