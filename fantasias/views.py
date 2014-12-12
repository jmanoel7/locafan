# -*- coding: utf-8 -*-
from django.shortcuts import render
#from django.http import HttpResponse, HttpResponseRedirect
#from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
#from datetime import date

from home.models import Fantasia
from fantasias.forms import FantasiaCadastrarForm, FantasiaBuscarNomeForm, \
    FantasiaEditarForm, FantasiaExcluirForm, FantasiaBuscarTemaForm, \
    FantasiaBuscarTipoForm


def buscar_nome(request):

    if request.method == 'POST':
        form = FantasiaBuscarNomeForm(request.POST)
        if form.is_valid():
            nome = request.POST.get("nome", "")
            fantasias = list(Fantasia.objects.filter(nome__contains=nome))
            return render(
                request,
                'fantasias_lista.html',
                {
                    'fantasias': fantasias,
                    'titulo_lista': u'Lista de Fantasias que contém "%s" no '
                        u'seu Nome' % (nome),
                    'msg_lista_vazia': u'Não foi encontrado nenhuma Fantasia '
                        u'que contenha "%s" no seu Nome' % (nome),
                },
            )
    else:
        form = FantasiaBuscarNomeForm()
    return render(request, 'fantasias_form.html', {
        'form': form,
        'tarefa': 'Buscar Fantasia pelo Nome',
        'botao': 'Buscar',
    })


def buscar_tema(request):

    if request.method == 'POST':
        form = FantasiaBuscarTemaForm(request.POST)
        if form.is_valid():
            tema = request.POST.get("tema", "")
            fantasias = list(Fantasia.objects.filter(tema__contains=tema))
            return render(
                request,
                'fantasias_lista.html',
                {
                    'fantasias': fantasias,
                    'titulo_lista': u'Lista de Fantasias que contém "%s" no '
                        u'Tema' % (tema),
                    'msg_lista_vazia': u'Não foi encontrado nenhuma Fantasia '
                        u'que contenha "%s" no seu Tema' % (tema),
                },
            )
    else:
        form = FantasiaBuscarTemaForm()
    return render(request, 'fantasias_form.html', {
        'form': form,
        'tarefa': 'Buscar Fantasia pelo Tema',
        'botao': 'Buscar',
    })


def buscar_tipo(request):

    if request.method == 'POST':
        form = FantasiaBuscarTipoForm(request.POST)
        if form.is_valid():
            tipo = request.POST.get("tipo", "")
            fantasias = list(Fantasia.objects.filter(tipo=tipo))
            if tipo == 'IM':
                tipo_str = 'Inafantil Masculino'
            elif tipo == 'IF':
                tipo_str = 'Inafantil Feminino'
            elif tipo == 'AM':
                tipo_str = 'Adulto Masculino'
            elif tipo == 'AF':
                tipo_str = 'Adulto Feminino'
            elif tipo == 'CS':
                tipo_str = 'Casal'
            return render(
                request,
                'fantasias_lista.html',
                {
                    'fantasias': fantasias,
                    'titulo_lista': u'Lista de Fantasias do Tipo: "%s"'
                        % (tipo_str),
                    'msg_lista_vazia': u'Não foi encontrado nenhuma Fantasia '
                        u'do Tipo: "%s"' % (tipo_str),
                },
            )
    else:
        form = FantasiaBuscarTipoForm()
    return render(request, 'fantasias_form.html', {
        'form': form,
        'tarefa': 'Buscar Fantasia pelo Tipo',
        'botao': 'Buscar',
    })


def cadastrar(request):
    if request.method == 'POST':
        form = FantasiaCadastrarForm(request.POST)
        if form.is_valid():
            nova_fantasia = form.save()
            return render(request, 'fantasias_form_ok.html', {
                'tarefa': u'Cadastro',
                'nome': nova_fantasia.nome,
                'tipo': nova_fantasia.tipo,
                'tema': nova_fantasia.tema,
                'genero': 'o',
            })
    else:
        form = FantasiaCadastrarForm()
    return render(request, 'fantasias_form.html', {
        'form': form,
        'tarefa': 'Cadastrar Fantasia',
        'botao': 'Cadastrar',
    })


def editar(request, nome, tipo, tema):
    fantasia = get_object_or_404(Fantasia, nome=nome, tipo=tipo, tema=tema)
    if request.method == 'POST':
        form = FantasiaEditarForm(request.POST, instance=fantasia)
        if form.is_valid():
            nova_fantasia = form.save()
            return render(request, 'fantasias_form_ok.html', {
                'tarefa': u'Edição',
                'nome': nova_fantasia.nome,
                'tipo': nova_fantasia.tipo,
                'tema': nova_fantasia.tema,
                'genero': 'a',
            })
    else:
        form = FantasiaEditarForm(instance=fantasia)
    return render(request, 'fantasias_form.html', {
        'form': form,
        'nome': nome,
        'tarefa': 'Editar Fantasia',
        'botao': 'Alterar',
    })


def listar(request):

    fantasias = Fantasia.objects.all()
    return render(request, 'fantasias_lista.html', {
        'fantasias': fantasias,
        'titulo_lista': u'Lista de Fantasias Cadastradas',
        'msg_lista_vazia': u'Ainda não temos nenhuma Fantasia Cadastrada.',
    })


def excluir(request, nome, tipo, tema):

    fantasia = get_object_or_404(Fantasia, nome=nome, tipo=tipo, tema=tema)
    if request.method == 'POST':
        fantasia.delete()
        return render(request, 'fantasias_form_ok.html', {
            'tarefa': u'Exclusão',
            'nome': nome,
            'tipo': tipo,
            'tema': tema,
            'genero': 'a',
        })
    else:
        form = FantasiaExcluirForm(instance=fantasia)
        return render(request, 'fantasias_form.html', {
            'form': form,
            'nome': nome,
            'tarefa': 'Excluir Fantasia',
            'botao': 'Excuir',
        })
