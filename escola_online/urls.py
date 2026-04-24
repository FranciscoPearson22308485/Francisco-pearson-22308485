from django.urls import path
from . import views

app_name = 'escola_online'

urlpatterns = [
    path('cursos/', views.cursos_view, name='cursos'),
]