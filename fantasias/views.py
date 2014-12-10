# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from datetime import date

from home.models import Fantasia
from fantasias.forms import FantasiaCadastrarForm, FantasiaEditarForm, FantasiaExcluirForm

def cadastrar(request):
    if request.method == 'POST':
        form = FantasiaCadastrarForm(request.POST)
        if form.is_valid():
            nova_fantasia = form.save()
            return render(request, 'fantasias_form_ok.html', {
                'tarefa': u'Cadastro',
                'nome': nova_fantasia.nome,
                'genero': 'o',
            })
    else:
        form = FantasiaCadastrarForm()
    return render(request, 'fantasias_form.html', {
        'form': form,
        'tarefa': 'Cadastrar',
        'botao': 'Cadastrar',
    })

def editar(request):

    return render(request, 'fantasias_busca.html', {'tarefa': 'Editar'})

def editar_nome(request, nome):
    fantasia = get_object_or_404(Fantasia, nome=nome)
    if request.method == 'POST':
        form = FantasiaEditarForm(request.POST, instance=fantasia)
        if form.is_valid():
            nova_fantasia = form.save()
            return render(request, 'fantasias_form_ok.html', {
                'tarefa': u'Edição',
                'nome': nova_fantasia.nome,
                'genero': 'a',
            })
    else:
        form = FantasiaEditarForm(instance=fantasia)
    return render(request, 'fantasias_form.html', {
        'form': form,
        'nome': nome,
        'tarefa': 'Editar',
        'botao': 'Alterar',
    })

def listar(request):

    fantasias = Fantasia.objects.all()
    return render(request, 'fantasias_lista.html', {'fantasias': fantasias})

def excluir(request):

    return render(request, 'fantasias_busca.html', {'tarefa': 'Excluir'})

def excluir_nome(request, nome):
    """Da a opcao de excluir o cliente cujo nome = nome. Senao existir tal cliente, eh mostrado um erro http 404.
    :TODO: verificar se o cliente pode ser excluido antes de apresentar os seus dados.
    :request: eh a requisicao http
    :nome: eh o nome do cliente
    :returns: uma requisicao http de um formulario de exclusao com os dados do cliente se existir o cliente, senao um erro http 404

    """
    fantasia = get_object_or_404(Fantasia, nome=nome)
    if request.method == 'POST':
        fantasia.delete()
        return render(request, 'fantasias_form_ok.html', {
            'tarefa': u'Exclusão',
            'nome': nome,
            'genero': 'a',
        })
    else:
        form = FantasiaExcluirForm(instance=fantasia)
        return render(request, 'fantasias_form.html', {
            'form': form,
            'nome': nome,
            'tarefa': 'Excluir',
            'botao': 'Excuir',
        })
