from django.urls import path
from . import views

app_name = 'escola_online'

urlpatterns = [
    path('cursos/', views.cursos_view, name='cursos'),
    path('professores/', views.professores_view, name='professores'),
    path('alunos/', views.alunos_view, name='alunos'),
    path('curso/<int:curso_id>/', views.curso_view, name='curso'),
]