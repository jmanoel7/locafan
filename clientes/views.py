# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404

from home.models import Clientes
from clientes.forms import ClientesCadastrarForm, ClientesEditarForm

def cadastrar(request):
    
    if request.method == 'POST':
        form = ClientesCadastrarForm(request.POST)
        if form.is_valid():
            novo_cliente = form.save()
            #return HttpResponseRedirect(reverse('clientes_cadastrar'))
            return render(request, 'clientes_conclusao.djhtml', {
                'nome': novo_cliente.nome,
                'tarefa': 'Cadastro',
                'genero': 'o',
                'voltar': '1',
            })
    else:
        form = ClientesCadastrarForm()
    return render(request, 'clientes_form.djhtml', {
        'form': form,
        'tarefa': 'Cadastrar',
    })

def editar(request):

    return render(request, 'clientes_buscar.djhtml', {'tarefa': 'Editar'})

def editar_nome(request, nome, voltar):
    
    cliente = get_object_or_404(Clientes, nome=nome)
    if request.method == 'POST':
        form = ClientesEditarForm(request.POST, instance=cliente)
        if form.is_valid():
            novo_cliente = form.save()
            #return HttpResponseRedirect(reverse('clientes_cadastrar'))
            return render(request, 'clientes_conclusao.djhtml',
                {
                    'nome': novo_cliente.nome,
                    'tarefa': u'Edição',
                    'genero': 'a',
                    'voltar': voltar,
                }
            )
    else:
        form = ClientesEditarForm(instance=cliente)
    return render(request, 'clientes_form.djhtml',
        {
            'form': form,
            'tarefa': 'Editar',
        }
    )

def listar(request):

    clientes = Clientes.objects.all()
    return render(request, 'clientes_listar.djhtml', {'clientes': clientes})

def excluir(request):

    return render(request, 'clientes_buscar.djhtml', {'tarefa': 'Excluir'})
