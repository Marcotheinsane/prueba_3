
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('cursos/', views.listar_cursos, name='listar_cursos'),
    path('cursos/crear/', views.crear_curso, name='crear_curso'),
    path('cursos/editar/<int:codigo>/', views.editar_curso, name='editar_curso'),
    path('cursos/eliminar/<int:codigo>/', views.eliminar_curso, name='eliminar_curso'),
]
