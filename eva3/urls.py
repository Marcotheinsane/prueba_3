
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('cursos/', views.listar_cursos, name='listar_cursos'),
    path('cursos/crear/', views.crear_curso, name='crear_curso'),
    path('cursos/editar/<int:codigo>/', views.editar_curso, name='editar_curso'),
    path('cursos/eliminar/<int:pk>/', views.eliminar_curso, name='eliminar_curso'),
    
    path('sucursales/', views.listar_sucursal, name='listar_sucursales'),
    path('sucursales/crear/', views.crear_sucursal, name='crear_sucursal'),
    path('sucursales/editar/<int:pk>/', views.editar_sucursal, name='editar_sucursal'),
    path('sucursales/eliminar/<int:pk>/', views.eliminar_sucursal, name='eliminar_sucursal'),

    path('alumnos/', views.listar_alumnos, name='listar_alumnos'),
    path('alumnos/crear/', views.crear_alumno, name='crear_alumno'),
    path('alumnos/editar/<str:rut>/', views.editar_alumno, name='editar_alumno'),
    path('alumnos/eliminar/<str:rut>/', views.eliminar_alumno, name='eliminar_alumno'), 


    path('matriculas/', views.listar_matriculas, name='listar_matriculas'),
    path('matriculas/crear/', views.crear_matricula, name='crear_matricula'),
    path('matriculas/editar/<int:id>/', views.editar_matricula, name='editar_matricula'),
    path('matriculas/eliminar/<int:pk>/', views.eliminar_matricula, name='eliminar_matricula'),
]
