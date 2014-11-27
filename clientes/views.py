# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from datetime import date

from home.models import Clientes
from clientes.forms import ClientesCadastrarForm, ClientesEditarForm, ClientesExcluirForm

def cadastrar(request):
    if request.method == 'POST':
        form = ClientesCadastrarForm(request.POST)
        if form.is_valid():
            novo_cliente = form.save()
            return render(request, 'clientes_form_ok.djhtml', {
                'tarefa': u'Inclusão',
                'nome': novo_cliente.nome,
            })
    else:
        form = ClientesCadastrarForm()
    return render(request, 'clientes_form.djhtml', {
        'form': form,
        'tarefa': 'Cadastrar',
    })

def editar(request):

    return render(request, 'clientes_busca.djhtml', {'tarefa': 'Editar'})

def editar_nome(request, nome):
    cliente = get_object_or_404(Clientes, nome=nome)
    if request.method == 'POST':
        form = ClientesEditarForm(request.POST, instance=cliente)
        if form.is_valid():
            novo_cliente = form.save()
            return render(request, 'clientes_form_ok.djhtml', {
                'tarefa': u'Alteração',
                'nome': novo_cliente.nome,
            })
    else:
        form = ClientesEditarForm(instance=cliente)
    return render(request, 'clientes_form.djhtml', {'form': form, 'nome': nome, 'tarefa': 'Editar'})

def listar(request):

    clientes = Clientes.objects.all()
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
    cliente = get_object_or_404(Clientes, nome=nome)
    if request.method == 'POST':
        cliente.delete()
        return render(request, 'clientes_form_ok.djhtml', {
            'tarefa': u'Exclusão',
            'nome': nome,
        })
    else:
        form = ClientesExcluirForm(instance=cliente)
        return render(request, 'clientes_form.djhtml', {
            'form': form,
            'nome': nome,
            'tarefa': 'Excluir',
        })
