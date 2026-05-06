from django.contrib.auth.decorators import login_required
from collections import defaultdict
from django.shortcuts import render, redirect, get_object_or_404
from .models import Tecnologia, UnidadeCurricular, Projeto, TFC, Competencia, Formacao, Interesse, MakingOf
from .forms import ProjetoForm, TecnologiaForm, CompetenciaForm, FormacaoForm

# ==========================================
# VIEWS DE LISTAGEM (públicas)
# ==========================================

def home_view(request):
    return render(request, 'portfolio/home.html')

def interesses_view(request):
    interesses = Interesse.objects.all()
    return render(request, 'portfolio/interesses.html', {'interesses': interesses})

def makingof_view(request):
    entradas = MakingOf.objects.select_related('uc', 'projeto').all()
    return render(request, 'portfolio/makingof.html', {'entradas': entradas})

def competencias_view(request):
    competencias = Competencia.objects.prefetch_related('tecnologias', 'projetos').all()
    return render(request, 'portfolio/competencias.html', {'competencias': competencias})

def formacoes_view(request):
    formacoes = Formacao.objects.prefetch_related('tecnologias').all()
    return render(request, 'portfolio/formacoes.html', {'formacoes': formacoes})

def tecnologias_view(request):
    tecnologias = Tecnologia.objects.all()
    return render(request, 'portfolio/tecnologias.html', {'tecnologias': tecnologias})

def ucs_view(request):
    ucs = UnidadeCurricular.objects.select_related('licenciatura').prefetch_related('docentes').all()
    return render(request, 'portfolio/ucs.html', {'ucs': ucs})

def projetos_view(request):
    projetos = Projeto.objects.select_related('uc').prefetch_related('tecnologias').all()
    return render(request, 'portfolio/projetos.html', {'projetos': projetos})

def tfcs_view(request):
    tfcs = TFC.objects.prefetch_related('tecnologias').all()
    return render(request, 'portfolio/tfcs.html', {'tfcs': tfcs})

def sobre_view(request):
    """Página Sobre esta Aplicação - APENAS tecnologias usadas neste projeto"""
    
    # Lista das tecnologias que REALMENTE usei neste projeto Django
    nomes_usadas = ['Python', 'Django', 'HTML', 'CSS', 'SQLite', 'Git']
    
    tecnologias = Tecnologia.objects.filter(nome__in=nomes_usadas).select_related('tipo')
    
    tecnologias_por_tipo = defaultdict(list)
    for tech in tecnologias:
        nome_tipo = tech.tipo.nome if tech.tipo else "Outros"
        tecnologias_por_tipo[nome_tipo].append(tech)
    tecnologias_por_tipo = dict(sorted(tecnologias_por_tipo.items()))
    
    return render(request, 'portfolio/sobre.html', {
        'tecnologias_por_tipo': tecnologias_por_tipo,
    })

# ==========================================
# VIEWS DE CRUD: PROJETOS (protegidas)
# ==========================================

@login_required
def novo_projeto_view(request):
    if request.method == 'POST':
        form = ProjetoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('portfolio:projetos')
    else:
        form = ProjetoForm()
    return render(request, 'portfolio/novo_projeto.html', {'form': form})

@login_required
def editar_projeto_view(request, projeto_id):
    projeto = get_object_or_404(Projeto, id=projeto_id)
    if request.method == 'POST':
        form = ProjetoForm(request.POST, request.FILES, instance=projeto)
        if form.is_valid():
            form.save()
            return redirect('portfolio:projetos')
    else:
        form = ProjetoForm(instance=projeto)
    return render(request, 'portfolio/editar_projeto.html', {'form': form, 'projeto': projeto})

@login_required
def apagar_projeto_view(request, projeto_id):
    projeto = get_object_or_404(Projeto, id=projeto_id)
    if request.method == 'POST':
        projeto.delete()
        return redirect('portfolio:projetos')
    return render(request, 'portfolio/apagar_projeto.html', {'projeto': projeto})

# ==========================================
# VIEWS DE CRUD: TECNOLOGIAS (protegidas)
# ==========================================

@login_required
def nova_tecnologia_view(request):
    if request.method == 'POST':
        form = TecnologiaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('portfolio:tecnologias')
    else:
        form = TecnologiaForm()
    return render(request, 'portfolio/nova_tecnologia.html', {'form': form})

@login_required
def editar_tecnologia_view(request, tecnologia_id):
    tecnologia = get_object_or_404(Tecnologia, id=tecnologia_id)
    if request.method == 'POST':
        form = TecnologiaForm(request.POST, request.FILES, instance=tecnologia)
        if form.is_valid():
            form.save()
            return redirect('portfolio:tecnologias')
    else:
        form = TecnologiaForm(instance=tecnologia)
    return render(request, 'portfolio/editar_tecnologia.html', {'form': form, 'tecnologia': tecnologia})

@login_required
def apagar_tecnologia_view(request, tecnologia_id):
    tecnologia = get_object_or_404(Tecnologia, id=tecnologia_id)
    if request.method == 'POST':
        tecnologia.delete()
        return redirect('portfolio:tecnologias')
    return render(request, 'portfolio/apagar_tecnologia.html', {'tecnologia': tecnologia})

# ==========================================
# VIEWS DE CRUD: COMPETÊNCIAS (protegidas)
# ==========================================

@login_required
def nova_competencia_view(request):
    if request.method == 'POST':
        form = CompetenciaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('portfolio:competencias')
    else:
        form = CompetenciaForm()
    return render(request, 'portfolio/nova_competencia.html', {'form': form})

@login_required
def editar_competencia_view(request, competencia_id):
    competencia = get_object_or_404(Competencia, id=competencia_id)
    if request.method == 'POST':
        form = CompetenciaForm(request.POST, instance=competencia)
        if form.is_valid():
            form.save()
            return redirect('portfolio:competencias')
    else:
        form = CompetenciaForm(instance=competencia)
    return render(request, 'portfolio/editar_competencia.html', {'form': form, 'competencia': competencia})

@login_required
def apagar_competencia_view(request, competencia_id):
    competencia = get_object_or_404(Competencia, id=competencia_id)
    if request.method == 'POST':
        competencia.delete()
        return redirect('portfolio:competencias')
    return render(request, 'portfolio/apagar_competencia.html', {'competencia': competencia})

# ==========================================
# VIEWS DE CRUD: FORMAÇÕES (protegidas)
# ==========================================

@login_required
def nova_formacao_view(request):
    if request.method == 'POST':
        form = FormacaoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('portfolio:formacoes')
    else:
        form = FormacaoForm()
    return render(request, 'portfolio/nova_formacao.html', {'form': form})

@login_required
def editar_formacao_view(request, formacao_id):
    formacao = get_object_or_404(Formacao, id=formacao_id)
    if request.method == 'POST':
        form = FormacaoForm(request.POST, request.FILES, instance=formacao)
        if form.is_valid():
            form.save()
            return redirect('portfolio:formacoes')
    else:
        form = FormacaoForm(instance=formacao)
    return render(request, 'portfolio/editar_formacao.html', {'form': form, 'formacao': formacao})

@login_required
def apagar_formacao_view(request, formacao_id):
    formacao = get_object_or_404(Formacao, id=formacao_id)
    if request.method == 'POST':
        formacao.delete()
        return redirect('portfolio:formacoes')
    return render(request, 'portfolio/apagar_formacao.html', {'formacao': formacao})