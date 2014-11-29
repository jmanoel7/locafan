# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from datetime import date

from home.models import Locacao
from locacoes.forms import LocacaoCadastrarForm, LocacaoEditarForm, LocacaoExcluirForm

def cadastrar(request):
    if request.method == 'POST':
        form = LocacaoCadastrarForm(request.POST)
        if form.is_valid():
            nova_locacao = form.save()
            return render(request, 'locacoes_form_ok.djhtml', {
                'tarefa': u'Cadastro',
                'dt_devolucao': nova_locacao.dt_devolucao,
                'genero': 'o',
            })
    else:
        form = LocacaoCadastrarForm()
    return render(request, 'locacoes_form.djhtml', {
        'form': form,
        'tarefa': 'Cadastrar',
        'botao': 'Cadastrar',
    })

def editar(request):

    return render(request, 'locacoes_busca.djhtml', {'tarefa': 'Editar'})

def editar_dt_devolucao(request, dt_devolucao):
    locacao = get_object_or_404(Locacao, dt_devolucao=dt_devolucao)
    if request.method == 'POST':
        form = LocacaoEditarForm(request.POST, instance=locacao)
        if form.is_valid():
            nova_locacao = form.save()
            return render(request, 'locacoes_form_ok.djhtml', {
                'tarefa': u'Edição',
                'dt_devolucao': nova_locacao.dt_devolucao,
                'genero': 'a',
            })
    else:
        form = LocacaoEditarForm(instance=locacao)
    return render(request, 'locacoes_form.djhtml', {
        'form': form,
        'dt_devolucao': dt_devolucao,
        'tarefa': 'Editar',
        'botao': 'Alterar',
    })

def listar(request):

    locacoes = Locacao.objects.all()
    #nome_cliente=Cliente.objects.get(id=locacoes.cliente_id).nome
    return render(request, 'locacoes_lista.djhtml', {'locacoes': locacoes})

def excluir(request):

    return render(request, 'locacoes_busca.djhtml', {'tarefa': 'Excluir'})

def excluir_dt_devolucao(request, dt_devolucao):
    """Da a opcao de excluir o cliente cujo dt_devolucao = dt_devolucao. Senao existir tal cliente, eh mostrado um erro http 404.
    :TODO: verificar se o cliente pode ser excluido antes de apresentar os seus dados.
    :request: eh a requisicao http
    :dt_devolucao: eh o dt_devolucao do cliente
    :returns: uma requisicao http de um formulario de exclusao com os dados do cliente se existir o cliente, senao um erro http 404

    """
    locacao = get_object_or_404(Locacao, dt_devolucao=dt_devolucao)
    if request.method == 'POST':
        locacao.delete()
        return render(request, 'locacoes_form_ok.djhtml', {
            'tarefa': u'Exclusão',
            'dt_devolucao': dt_devolucao,
            'genero': 'a',
        })
    else:
        form = LocacaoExcluirForm(instance=locacao)
        return render(request, 'locacoes_form.djhtml', {
            'form': form,
            'dt_devolucao': dt_devolucao,
            'tarefa': 'Excluir',
            'botao': 'Excuir',
        })
