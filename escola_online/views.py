from django.shortcuts import render, get_object_or_404
from .models import Curso, Professor, Aluno

# 1. Listagem de Cursos (com otimização de performance)
def cursos_view(request):
    # O select_related carrega o professor (1 para 1)
    # O prefetch_related carrega a lista de alunos (Muitos para Muitos)
    cursos = Curso.objects.select_related('professor').prefetch_related('alunos').all()
    return render(request, 'escola_online/cursos.html', {'cursos': cursos})

# 2. Listagem de Alunos
def alunos_view(request):
    # Vamos buscar todos os alunos e os cursos onde estão inscritos
    alunos = Aluno.objects.prefetch_related('cursos').all()
    return render(request, 'escola_online/alunos.html', {'alunos': alunos})

# 3. Listagem de Professores
def professores_view(request):
    professores = Professor.objects.prefetch_related('cursos').all()
    return render(request, 'escola_online/professores.html', {'professores': professores})

# 4. Detalhe de um Curso específico
def curso_view(request, id):
    # get_object_or_404 dá erro 404 se o ID do curso não existir
    curso = get_object_or_404(Curso, id=id)
    return render(request, 'escola_online/curso.html', {'curso': curso})