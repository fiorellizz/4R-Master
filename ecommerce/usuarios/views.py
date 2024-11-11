from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def cadastro(request):
    if request.method == "GET":
        return render(request, 'acesso.html')
    else:
        nome = request.POST.get('nome')
        usuario = request.POST.get('usuario')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

        if not senha == confirmar_senha:
            messages.add_message(request, constants.ERROR, 'As senhas não coincidem')
            return redirect('/usuarios/cadastro')
        
        if len(senha) < 6:
            messages.add_message(request, constants.ERROR, 'Sua senha deve ter 7 ou mais dígitos')
            return redirect('/usuarios/cadastro')
        
        if User.objects.filter(username=usuario).exists():
            messages.add_message(request, constants.ERROR, 'Nome de usuário já existe.')
            return redirect('/usuarios/cadastro')
        
        try:
            user = User.objects.create_user(
                first_name = nome,
                username=usuario,
                email=email,
                password=senha,
            )
            user.save()
            messages.add_message(request, constants.SUCCESS, 'Usuário cadastrado com sucesso')
            return redirect('/usuarios/logar')
        except:
            messages.add_message(request, constants.ERROR, 'Erro interno do sistema, contate um adminstrador')
            return redirect('/usuarios/cadastro')

def logar(request):
    if request.method == "GET":
        return render(request, 'acesso.html')
    else:
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')

        user = authenticate(username=usuario, password=senha)

        if user:
            login(request, user)
						
            return redirect('/loja')
        else:
            messages.add_message(request, constants.ERROR, 'Usuario ou senha inválidos')
            return redirect('/usuarios/logar')

@login_required(login_url='/usuarios/logar')
def sair(request):
    logout(request)
    return redirect('/usuarios/logar')


@login_required(login_url='/usuarios/logar')
def trocar(request):
    if request.method == "GET":
        return render(request, 'trocarsenha.html')
    
    elif request.method == "POST":
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')
        
        if senha != confirmar_senha:
            messages.add_message(request, constants.ERROR, 'As senhas não coincidem')
            return redirect('/usuarios/trocar')
        
        if len(senha.strip()) < 6:
            messages.add_message(request, constants.ERROR, 'Sua senha deve ter 7 ou mais caracteres')
            return redirect('/usuarios/trocar')
        
        try:
            user = request.user
            user.set_password(senha)
            user.save()
            login(request, user)
            return redirect('/loja')
        except:
            messages.add_message(request, constants.ERROR, 'Erro ao alterar a senha. Tente novamente ou contate um administrador.')
            return redirect('/usuarios/trocar')
