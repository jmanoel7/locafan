# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from datetime import date

from home.models import Cliente
from clientes.forms import ClienteCadastrarForm, ClienteEditarForm, ClienteExcluirForm

def cadastrar(request):
    if request.method == 'POST':
        form = ClienteCadastrarForm(request.POST)
        if form.is_valid():
            novo_cliente = form.save()
            return render(request, 'clientes_form_ok.djhtml', {
                'tarefa': u'Cadastro',
                'nome': novo_cliente.nome,
                'genero': 'o',
            })
    else:
        form = ClienteCadastrarForm()
    return render(request, 'clientes_form.djhtml', {
        'form': form,
        'tarefa': 'Cadastrar',
        'botao': 'Cadastrar',
    })

def editar(request):

    return render(request, 'clientes_busca.djhtml', {'tarefa': 'Editar'})

def editar_nome(request, nome):
    cliente = get_object_or_404(Cliente, nome=nome)
    if request.method == 'POST':
        form = ClienteEditarForm(request.POST, instance=cliente)
        if form.is_valid():
            novo_cliente = form.save()
            return render(request, 'clientes_form_ok.djhtml', {
                'tarefa': u'Edição',
                'nome': novo_cliente.nome,
                'genero': 'a',
            })
    else:
        form = ClienteEditarForm(instance=cliente)
    return render(request, 'clientes_form.djhtml', {
        'form': form,
        'nome': nome,
        'tarefa': 'Editar',
        'botao': 'Alterar',
    })

def listar(request):

    clientes = Cliente.objects.all()
    return render(request, 'clientes_lista.djhtml', {'clientes': clientes})

def excluir(request):

    return render(request, 'clientes_busca.djhtml', {'tarefa': 'Excluir'})

def excluir_nome(request, nome):
    """Da a opcao de excluir o cliente cujo nome = nome. Senao existir tal cliente, eh mostrado um erro http 404.
    :TODO: verificar se o cliente pode ser excluido antes de apresentar os seus dados.
    :request: eh a requisicao http
    :nome: eh o nome do cliente
    :returns: uma requisicao http de um formulario de exclusao com os dados do cliente se existir o cliente, senao um erro http 404

    """
    cliente = get_object_or_404(Cliente, nome=nome)
    if request.method == 'POST':
        cliente.delete()
        return render(request, 'clientes_form_ok.djhtml', {
            'tarefa': u'Exclusão',
            'nome': nome,
            'genero': 'a',
        })
    else:
        form = ClienteExcluirForm(instance=cliente)
        return render(request, 'clientes_form.djhtml', {
            'form': form,
            'nome': nome,
            'tarefa': 'Excluir',
            'botao': 'Excuir',
        })
