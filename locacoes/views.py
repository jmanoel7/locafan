# -*- coding: utf-8 -*-
from django.shortcuts import render

def cadastrar(request):
    return render(request, 'cadastrar_locacoes.djhtml')

def editar(request):
    return render(request, 'buscar_locacoes.djhtml', {'acao': 'Editar'})

def listar(request):
    return render(request, 'listar_locacoes.djhtml')

def excluir(request):
    return render(request, 'buscar_locacoes.djhtml', {'acao': 'Excluir'})
