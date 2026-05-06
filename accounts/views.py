from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.core.mail import send_mail
from .forms import RegistoForm
from .models import MagicToken
import os


def login_view(request):
    if request.user.is_authenticated:
        return redirect('portfolio:home')
    
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('portfolio:home')
    else:
        form = AuthenticationForm()
    
    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('portfolio:home')


def registo_view(request):
    if request.user.is_authenticated:
        return redirect('portfolio:home')
    
    if request.method == 'POST':
        form = RegistoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')
    else:
        form = RegistoForm()
    
    return render(request, 'accounts/registo.html', {'form': form})


def magic_link_request_view(request):
    """View para pedir magic link por email"""
    if request.method == 'POST':
        email = request.POST.get('email')
        
        # Verificar se existe user com esse email
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            
            # Gerar token único
            token = MagicToken.generate_token()
            MagicToken.objects.create(user=user, token=token)
            
            # Construir URL absoluto baseado no Codespaces ou localhost
            codespace_name = os.environ.get('CODESPACE_NAME')
            if codespace_name:
                base_url = f"https://{codespace_name}-8000.app.github.dev"
            else:
                base_url = "http://localhost:8000"
            
            link = f"{base_url}/accounts/magic-link/validate/?token={token}"
            
            # Enviar email
            send_mail(
                subject='🔐 Link de Autenticação - Portfolio',
                message=f'Olá {user.first_name},\n\nClique no link para entrar:\n{link}\n\nO link expira em 15 minutos.',
                from_email='noreply@portfolio.com',
                recipient_list=[email],
                fail_silently=False,
            )
            
            return render(request, 'accounts/magic_link_sent.html', {'email': email})
        else:
            return render(request, 'accounts/magic_link_request.html', {
                'erro': 'Email não encontrado. Registe-se primeiro.'
            })
    
    return render(request, 'accounts/magic_link_request.html')


def magic_link_validate_view(request):
    """View para validar o token e fazer login"""
    token = request.GET.get('token')
    
    try:
        magic_token = MagicToken.objects.get(token=token)
        
        # Verificar se token ainda é válido (15 minutos)
        if magic_token.is_valid():
            # Fazer login
            login(request, magic_token.user, backend='django.contrib.auth.backends.ModelBackend')
            
            # Apagar token usado
            magic_token.delete()
            
            return redirect('portfolio:home')
        else:
            return render(request, 'accounts/magic_link_error.html', {
                'erro': 'Link expirado. Peça um novo.'
            })
    
    except MagicToken.DoesNotExist:
        return render(request, 'accounts/magic_link_error.html', {
            'erro': 'Link inválido.'
        })