from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_artigos, name='lista_artigos'),
    path('<int:pk>/', views.detalhe_artigo, name='detalhe_artigo'),
    path('criar/', views.criar_artigo, name='criar_artigo'),
    path('<int:pk>/editar/', views.editar_artigo, name='editar_artigo'),
    path('<int:pk>/apagar/', views.apagar_artigo, name='apagar_artigo'),
    path('<int:pk>/like/', views.dar_like, name='dar_like'),
    path('<int:pk>/comentar/', views.adicionar_comentario, name='adicionar_comentario'),
]
