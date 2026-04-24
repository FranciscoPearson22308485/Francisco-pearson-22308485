from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('tecnologias/', views.tecnologias_view, name='tecnologias'),
    path('ucs/', views.ucs_view, name='ucs'),
]