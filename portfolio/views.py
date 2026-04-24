from django.shortcuts import render
from .models import Tecnologia

def home_view(request):
    return render(request, 'portfolio/home.html')

def tecnologias_view(request):
    tecnologias = Tecnologia.objects.all()
    return render(request, 'portfolio/tecnologias.html', {'tecnologias': tecnologias})