from django.urls import path
from . import views

# O namespace ajuda a organizar os links no HTML
app_name = 'escola_online'

urlpatterns = [
    # Rota para a listagem de todos os cursos
    path('cursos/', views.cursos_view, name='cursos'),
    
    # Rota para a listagem de todos os professores
    path('professores/', views.professores_view, name='professores'),
    
    # Rota para a listagem de todos os alunos
    path('alunos/', views.alunos_view, name='alunos'),
    
    # Rota DINÂMICA: o <int:id> apanha o número do curso da barra de endereço
    path('curso/<int:id>/', views.curso_view, name='curso'),
    
    # A "Melhoria" da Ficha 7: rota vazia para abrir cursos diretamente
    path('', views.cursos_view),
]