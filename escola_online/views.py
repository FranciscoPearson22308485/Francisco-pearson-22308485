from django.shortcuts import render
from .models import Curso

def cursos_view(request):
    # AVISO: select_related e prefetch_related obrigatórios para a nota máxima!
    cursos = Curso.objects.select_related('professor').prefetch_related('alunos').all()
    return render(request, 'escola_online/cursos.html', {'cursos': cursos})