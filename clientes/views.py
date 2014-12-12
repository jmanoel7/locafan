# -*- coding: utf-8 -*-
import re
from django.shortcuts import render
#from django.http import HttpResponse, HttpResponseRedirect
#from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404

from home.models import Cliente
from clientes.forms import ClienteCadastrarForm, ClienteBuscarNomeForm, \
    ClienteEditarForm, ClienteExcluirForm, ClienteBuscarCPFForm


def cadastrar(request):
    if request.method == 'POST':
        form = ClienteCadastrarForm(request.POST)
        if form.is_valid():
            novo_cliente = form.save()
            return render(request, 'clientes_form_ok.html', {
                'tarefa': u'Cadastro',
                'nome': novo_cliente.nome,
                'genero': 'o',
            })
    else:
        form = ClienteCadastrarForm()
    return render(request, 'clientes_form.html', {
        'form': form,
        'tarefa': 'Cadastrar Cliente',
        'botao': 'Cadastrar',
    })


def editar(request, nome):
    cliente = get_object_or_404(Cliente, nome=nome)
    if request.method == 'POST':
        form = ClienteEditarForm(request.POST, instance=cliente)
        if form.is_valid():
            novo_cliente = form.save()
            return render(request, 'clientes_form_ok.html', {
                'tarefa': u'Edição',
                'nome': novo_cliente.nome,
                'genero': 'a',
            })
    else:
        form = ClienteEditarForm(instance=cliente)
    return render(request, 'clientes_form.html', {
        'form': form,
        'nome': nome,
        'tarefa': 'Editar Cliente',
        'botao': 'Alterar',
    })


def buscar_nome(request):

    if request.method == 'POST':
        form = ClienteBuscarNomeForm(request.POST)
        if form.is_valid():
            nome = request.POST.get("nome", "")
            clientes = list(Cliente.objects.filter(nome__contains=nome))
            return render(
                request,
                'clientes_lista.html',
                {
                    'clientes': clientes,
                    'titulo_lista': u'Lista de clientes que contém "%s" no \
nome' % (nome),
                    'msg_lista_vazia': u'Não foi encontrado nenhum cliente \
que contenha "%s" no nome' % (nome),
                },
            )
    else:
        form = ClienteBuscarNomeForm()
    return render(request, 'clientes_form.html', {
        'form': form,
        'tarefa': 'Buscar Cliente pelo Nome',
        'botao': 'Buscar',
    })


def buscar_cpf(request):

    if request.method == 'POST':
        form = ClienteBuscarCPFForm(request.POST)
        if form.is_valid():
            cpf = request.POST.get("cpf", "")
            clientes = list(Cliente.objects.filter(cpf=cpf))
            cpf = re.sub(r'(\d{3})(\d{3})(\d{3})(\d{2})', r'\1.\2.\3-\4', cpf)
            return render(
                request,
                'clientes_lista.html',
                {
                    'clientes': clientes,
                    'titulo_lista': u'Cliente com CPF = "%s"' % (cpf),
                    'msg_lista_vazia': u'Não foi encontrado nenhum cliente \
com CPF = "%s"' % (cpf),
                },
            )
    else:
        form = ClienteBuscarCPFForm()
    return render(request, 'clientes_form.html', {
        'form': form,
        'tarefa': 'Buscar Cliente pelo CPF',
        'botao': 'Buscar',
    })


def listar(request):

    clientes = Cliente.objects.all()
    return render(request, 'clientes_lista.html', {
        'clientes': clientes,
        'titulo_lista': u'Lista de Clientes Cadastrados',
        'msg_lista_vazia': u'Ainda não temos nenhum Cliente Cadastrado.',
    })


def excluir(request, nome):

    cliente = get_object_or_404(Cliente, nome=nome)
    if request.method == 'POST':
        cliente.delete()
        return render(request, 'clientes_form_ok.html', {
            'tarefa': u'Exclusão',
            'nome': nome,
            'genero': 'a',
        })
    else:
        form = ClienteExcluirForm(instance=cliente)
        return render(request, 'clientes_form.html', {
            'form': form,
            'nome': nome,
            'tarefa': 'Excluir Cliente',
            'botao': 'Excuir',
        })
