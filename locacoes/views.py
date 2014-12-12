# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import get_object_or_404
#from datetime import date

from home.models import Locacao
from locacoes.forms import LocacaoCadastrarForm, LocacaoEditarForm, \
    LocacaoExcluirForm


def cadastrar(request):
    if request.method == 'POST':
        form = LocacaoCadastrarForm(request.POST)
        if form.is_valid():
            nova_locacao = form.save()
            return render(request, 'locacoes_form_ok.html', {
                'tarefa': u'Cadastro',
                'dt_devolucao': nova_locacao.dt_devolucao,
                'genero': 'o',
            })
    else:
        form = LocacaoCadastrarForm()
    return render(request, 'locacoes_form.html', {
        'form': form,
        'tarefa': 'Cadastrar',
        'botao': 'Cadastrar',
    })


def editar_dt_devolucao(request, dt_devolucao):
    locacao = get_object_or_404(Locacao, dt_devolucao=dt_devolucao)
    if request.method == 'POST':
        form = LocacaoEditarForm(request.POST, instance=locacao)
        if form.is_valid():
            nova_locacao = form.save()
            return render(request, 'locacoes_form_ok.html', {
                'tarefa': u'Edição',
                'dt_devolucao': nova_locacao.dt_devolucao,
                'genero': 'a',
            })
    else:
        form = LocacaoEditarForm(instance=locacao)
    return render(request, 'locacoes_form.html', {
        'form': form,
        'dt_devolucao': dt_devolucao,
        'tarefa': 'Editar',
        'botao': 'Alterar',
    })


def listar(request):

    locacoes = Locacao.objects.all()
    #nome_cliente=Cliente.objects.get(id=locacoes.cliente_id).nome
    return render(request, 'locacoes_lista.html', {'locacoes': locacoes})


def excluir_dt_devolucao(request, dt_devolucao):

    locacao = get_object_or_404(Locacao, dt_devolucao=dt_devolucao)
    if request.method == 'POST':
        locacao.delete()
        return render(request, 'locacoes_form_ok.html', {
            'tarefa': u'Exclusão',
            'dt_devolucao': dt_devolucao,
            'genero': 'a',
        })
    else:
        form = LocacaoExcluirForm(instance=locacao)
        return render(request, 'locacoes_form.html', {
            'form': form,
            'dt_devolucao': dt_devolucao,
            'tarefa': 'Excluir',
            'botao': 'Excuir',
        })
