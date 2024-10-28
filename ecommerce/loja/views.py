from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import *
from .utils import exportar_csv
from django.contrib.messages import constants
from django.contrib import messages

@login_required(login_url='/usuarios/logar')
def homepage(request):
    
    produtos = Produto.objects.filter(queridinho_da_galera=True, qtd_disponivel__gte=1)

    try:
        moedas = Moeda.objects.get(usuario=request.user).qtd_moeda
    except Moeda.DoesNotExist:
        moedas = 0.00

    context = {
        'moedas': moedas,
        'produtos': produtos,
    }

    return render(request, 'loja.html', context)
    
@login_required(login_url='/usuarios/logar')
def confirmar_compra(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)

    # Obtenha a quantidade de moedas do usuário
    moedas = Moeda.objects.get(usuario=request.user).qtd_moeda

    context = {
        'produto': produto,
        'moedas': moedas,
    }

    return render(request, 'confirmar_compra.html', context)

@login_required(login_url='/usuarios/logar')
def verificar_compra(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)

    # Obtenha a quantidade de moedas do usuário
    moedas = Moeda.objects.get(usuario=request.user).qtd_moeda

    context = {
        'produto': produto,
        'moedas': moedas,
    }

    return render(request, 'verificar_compra.html', context)

@login_required(login_url='/usuarios/logar')
def finalizar_compra(request, produto_id):
    if request.method == "POST":
        produto = get_object_or_404(Produto, id=produto_id)
        moeda_usuario = Moeda.objects.get(usuario=request.user)

        # Verifique se o usuário tem saldo suficiente
        if moeda_usuario.qtd_moeda < produto.preco:
            messages.add_message(request, constants.ERROR, 'Saldo insuficiente para realizar a compra.')
            return redirect('confirmar_compra', produto_id=produto.id)

        # Realize a compra
        if produto.qtd_disponivel > 0:
            # Reduz a quantidade disponível do produto
            produto.qtd_disponivel -= 1
            produto.save()

            # Atualiza o saldo de moedas do usuário
            moeda_usuario.qtd_moeda -= produto.preco
            moeda_usuario.save()

            # Registre a compra
            Compra.objects.create(usuario=request.user, produto=produto)

            # Passa o saldo atualizado para o template de sucesso
            context = {
                'produto': produto,
                'moedas_atualizadas': moeda_usuario.qtd_moeda,  # Saldo atualizado após a compra
            }
            return render(request, 'compra_sucesso.html', context)
        else:
            messages.add_message(request, constants.ERROR, 'Erro interno do sistema, contate um Administrador.')
            return redirect('homepage')
    elif request.method == "GET":
        return redirect('compra_sucesso', produto_id=produto.id)

@login_required(login_url='/usuarios/logar')
def produtos(request):
    categorias = Categoria.objects.all()

    categorias_com_produtos = []
    for categoria in categorias:
        produtos_disponiveis = categoria.produto_set.filter(qtd_disponivel__gt=0)
        if produtos_disponiveis.exists():
            categorias_com_produtos.append({
                'categoria': categoria,
                'produtos': produtos_disponiveis
            })

    try:
        moedas = Moeda.objects.get(usuario=request.user).qtd_moeda
    except Moeda.DoesNotExist:
        moedas = 0.00

    context = {
        'moedas': moedas,
        'categorias_com_produtos': categorias_com_produtos,
    }

    return render(request, 'produtos.html', context)


@login_required(login_url='/usuarios/logar')
def gerenciar_loja(request):
    if request.user.groups.filter(name="equipe").exists():
        return render(request, 'interno/gerenciar_loja.html')
    else:
        return redirect('homepage')

@login_required(login_url='/usuarios/logar')
def exportar_relatorio(request, relatorio):
    if request.user.groups.filter(name="equipe").exists():
        if relatorio == "compras":
            info = Compra.objects.all()

        elif relatorio == "usuarios":
            info = User.objects.all()

        elif relatorio == "produtos":
            info = Produto.objects.all()
        
        return exportar_csv(info, relatorio)
    else:
        return redirect('homepage')