from django.shortcuts import render, redirect, get_object_or_404
from .models import Tecnologia, UnidadeCurricular, Projeto, TFC, Competencia, Formacao, Interesse, MakingOf
from .forms import ProjetoForm, TecnologiaForm, CompetenciaForm, FormacaoForm # Importamos os forms

# ==========================================
# VIEWS DE LISTAGEM (O que já tinhas)
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

# ==========================================
# VIEWS DE CRUD: PROJETOS (Novas!)
# ==========================================

def novo_projeto_view(request):
    if request.method == 'POST':
        form = ProjetoForm(request.POST, request.FILES) 
        if form.is_valid():
            form.save()
            return redirect('portfolio:projetos') 
    else:
        form = ProjetoForm()
        
    return render(request, 'portfolio/novo_projeto.html', {'form': form})

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

def apagar_projeto_view(request, projeto_id):
    projeto = get_object_or_404(Projeto, id=projeto_id)
    
    if request.method == 'POST':
        projeto.delete()
        return redirect('portfolio:projetos')
        
    return render(request, 'portfolio/apagar_projeto.html', {'projeto': projeto})

# ==========================================
# VIEWS DE CRUD: TECNOLOGIAS
# ==========================================

def nova_tecnologia_view(request):
    if request.method == 'POST':
        form = TecnologiaForm(request.POST, request.FILES) 
        if form.is_valid():
            form.save()
            return redirect('portfolio:tecnologias') 
    else:
        form = TecnologiaForm()
        
    return render(request, 'portfolio/nova_tecnologia.html', {'form': form})

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

def apagar_tecnologia_view(request, tecnologia_id):
    tecnologia = get_object_or_404(Tecnologia, id=tecnologia_id)
    
    if request.method == 'POST':
        tecnologia.delete()
        return redirect('portfolio:tecnologias')
        
    return render(request, 'portfolio/apagar_tecnologia.html', {'tecnologia': tecnologia})

def sobre_view(request):
    # Um texto escrito em Markdown para testarmos a formatação
    texto_markdown = """
# Sobre esta Aplicação

Esta aplicação foi desenvolvida em **Django** e utiliza a arquitetura **MVT** (Model-View-Template).

## Funcionalidades principais:
* Gestão de Projetos (CRUD completo)
* Apresentação de Tecnologias
* Integração com Markdownify

**Autor:** Francisco Pearson
    """
    return render(request, 'portfolio/sobre.html', {'texto': texto_markdown})

# ==========================================
# VIEWS DE CRUD: COMPETÊNCIAS
# ==========================================
def nova_competencia_view(request):
    if request.method == 'POST':
        form = CompetenciaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('portfolio:competencias')
    else:
        form = CompetenciaForm()
    return render(request, 'portfolio/nova_competencia.html', {'form': form})

def editar_competencia_view(request, competencia_id):
    competencia = get_object_or_404(Competencia, id=competencia_id)
    if request.method == 'POST':
        form = CompetenciaForm(request.POST, request.FILES, instance=competencia)
        if form.is_valid():
            form.save()
            return redirect('portfolio:competencias')
    else:
        form = CompetenciaForm(instance=competencia)
    return render(request, 'portfolio/editar_competencia.html', {'form': form, 'competencia': competencia})

def apagar_competencia_view(request, competencia_id):
    competencia = get_object_or_404(Competencia, id=competencia_id)
    if request.method == 'POST':
        competencia.delete()
        return redirect('portfolio:competencias')
    return render(request, 'portfolio/apagar_competencia.html', {'competencia': competencia})

# ==========================================
# VIEWS DE CRUD: FORMAÇÕES
# ==========================================
def nova_formacao_view(request):
    if request.method == 'POST':
        form = FormacaoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('portfolio:formacoes')
    else:
        form = FormacaoForm()
    return render(request, 'portfolio/nova_formacao.html', {'form': form})

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

def apagar_formacao_view(request, formacao_id):
    formacao = get_object_or_404(Formacao, id=formacao_id)
    if request.method == 'POST':
        formacao.delete()
        return redirect('portfolio:formacoes')
    return render(request, 'portfolio/apagar_formacao.html', {'formacao': formacao})