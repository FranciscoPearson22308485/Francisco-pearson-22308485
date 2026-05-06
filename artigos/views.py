from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from .models import Artigo, Like, Comentario


def lista_artigos(request):
    artigos = Artigo.objects.all()
    return render(request, 'artigos/lista.html', {'artigos': artigos})


def detalhe_artigo(request, pk):
    artigo = get_object_or_404(Artigo, pk=pk)
    comentarios = artigo.comentarios.all()
    total_likes = artigo.likes.count()

    # Verificar se esta sessao ja deu like
    if not request.session.session_key:
        request.session.create()
    sessao = request.session.session_key
    ja_deu_like = artigo.likes.filter(sessao=sessao).exists()

    return render(request, 'artigos/detalhe.html', {
        'artigo': artigo,
        'comentarios': comentarios,
        'total_likes': total_likes,
        'ja_deu_like': ja_deu_like,
    })


@login_required
def criar_artigo(request):
    if not request.user.has_perm('artigos.add_artigo'):
        messages.error(request, 'Nao tens permissao para criar artigos.')
        return redirect('lista_artigos')

    if request.method == 'POST':
        titulo = request.POST.get('titulo', '').strip()
        texto = request.POST.get('texto', '').strip()
        link_externo = request.POST.get('link_externo', '').strip()
        fotografia = request.FILES.get('fotografia')

        if titulo and texto:
            artigo = Artigo.objects.create(
                titulo=titulo,
                texto=texto,
                link_externo=link_externo or None,
                fotografia=fotografia,
                autor=request.user,
            )
            messages.success(request, 'Artigo criado com sucesso!')
            return redirect('detalhe_artigo', pk=artigo.pk)
        else:
            messages.error(request, 'Titulo e texto sao obrigatorios.')

    return render(request, 'artigos/form.html', {'acao': 'Criar'})


@login_required
def editar_artigo(request, pk):
    artigo = get_object_or_404(Artigo, pk=pk)

    # So o proprio autor pode editar
    if artigo.autor != request.user:
        messages.error(request, 'Só o autor pode editar este artigo.')
        return redirect('detalhe_artigo', pk=pk)

    if request.method == 'POST':
        artigo.titulo = request.POST.get('titulo', '').strip()
        artigo.texto = request.POST.get('texto', '').strip()
        artigo.link_externo = request.POST.get('link_externo', '').strip() or None
        if request.FILES.get('fotografia'):
            artigo.fotografia = request.FILES.get('fotografia')
        artigo.save()
        messages.success(request, 'Artigo atualizado!')
        return redirect('detalhe_artigo', pk=artigo.pk)

    return render(request, 'artigos/form.html', {'acao': 'Editar', 'artigo': artigo})


@login_required
def apagar_artigo(request, pk):
    artigo = get_object_or_404(Artigo, pk=pk)

    if artigo.autor != request.user:
        messages.error(request, 'So o autor pode apagar este artigo.')
        return redirect('detalhe_artigo', pk=pk)

    if request.method == 'POST':
        artigo.delete()
        messages.success(request, 'Artigo apagado.')
        return redirect('lista_artigos')

    return render(request, 'artigos/confirmar_apagar.html', {'artigo': artigo})


def dar_like(request, pk):
    artigo = get_object_or_404(Artigo, pk=pk)

    if not request.session.session_key:
        request.session.create()
    sessao = request.session.session_key

    like, created = Like.objects.get_or_create(artigo=artigo, sessao=sessao)
    if not created:
        like.delete()  # toggle — remove like se ja existia

    return redirect('detalhe_artigo', pk=pk)


@login_required
def adicionar_comentario(request, pk):
    artigo = get_object_or_404(Artigo, pk=pk)

    if request.method == 'POST':
        texto = request.POST.get('texto', '').strip()
        if texto:
            Comentario.objects.create(
                artigo=artigo,
                autor=request.user,
                texto=texto,
            )
            messages.success(request, 'Comentario adicionado!')

    return redirect('detalhe_artigo', pk=pk)
