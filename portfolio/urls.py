from django.urls import path
from . import views

# O app_name é muito importante para usarmos o redirect('portfolio:projetos') nas views
app_name = 'portfolio'

urlpatterns = [
    # ==========================================
    # ROTAS DE LISTAGEM
    # ==========================================
    path('', views.home_view, name='home'),
    path('sobre/', views.sobre_view, name='sobre'), # <--- ROTA ADICIONADA AQUI
    path('interesses/', views.interesses_view, name='interesses'),
    path('makingof/', views.makingof_view, name='makingof'),
    path('competencias/', views.competencias_view, name='competencias'),
    path('formacoes/', views.formacoes_view, name='formacoes'),
    path('tecnologias/', views.tecnologias_view, name='tecnologias'),
    path('ucs/', views.ucs_view, name='ucs'),
    path('projetos/', views.projetos_view, name='projetos'),
    path('tfcs/', views.tfcs_view, name='tfcs'),

    # ==========================================
    # ROTAS DE CRUD: PROJETOS
    # ==========================================
    path('projetos/novo/', views.novo_projeto_view, name='novo_projeto'),
    path('projetos/editar/<int:projeto_id>/', views.editar_projeto_view, name='editar_projeto'),
    path('projetos/apagar/<int:projeto_id>/', views.apagar_projeto_view, name='apagar_projeto'),

    # ==========================================
    # ROTAS DE CRUD: TECNOLOGIAS
    # ==========================================
    path('tecnologias/nova/', views.nova_tecnologia_view, name='nova_tecnologia'),
    path('tecnologias/editar/<int:tecnologia_id>/', views.editar_tecnologia_view, name='editar_tecnologia'),
    path('tecnologias/apagar/<int:tecnologia_id>/', views.apagar_tecnologia_view, name='apagar_tecnologia'),

    # ==========================================
    # ROTAS DE CRUD: COMPETÊNCIAS
    # ==========================================
    path('competencias/nova/', views.nova_competencia_view, name='nova_competencia'),
    path('competencias/editar/<int:competencia_id>/', views.editar_competencia_view, name='editar_competencia'),
    path('competencias/apagar/<int:competencia_id>/', views.apagar_competencia_view, name='apagar_competencia'),

    # ==========================================
    # ROTAS DE CRUD: FORMAÇÕES
    # ==========================================
    path('formacoes/nova/', views.nova_formacao_view, name='nova_formacao'),
    path('formacoes/editar/<int:formacao_id>/', views.editar_formacao_view, name='editar_formacao'),
    path('formacoes/apagar/<int:formacao_id>/', views.apagar_formacao_view, name='apagar_formacao'),
]