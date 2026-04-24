from django.shortcuts import render
from .models import Curso

def cursos_view(request):
    # O uso do select_related e prefetch_related resolve o problema de N+1 queries
    cursos = Curso.objects.select_related('professor').prefetch_related('alunos').all()
    return render(request, 'escola_online/cursos.html', {'cursos': cursos})