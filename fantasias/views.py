# -*- coding: utf-8 -*-
from django.shortcuts import render

def cadastrar(request):
    return render(request, 'cadastrar_fantasias.djhtml')

def editar(request):
    return render(request, 'buscar_fantasias.djhtml', {'acao': 'Editar'})

def listar(request):
    return render(request, 'listar_fantasias.djhtml')

def excluir(request):
    return render(request, 'buscar_fantasias.djhtml', {'acao': 'Excluir'})
