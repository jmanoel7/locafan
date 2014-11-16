# -*- coding: utf-8 -*-
from django.shortcuts import render

def cadastrar(request):
    return render(request, 'cadastrar_locacoes.djhtml')

def buscar(request):
    return render(request, 'buscar_locacoes.djhtml')

def listar(request):
    return render(request, 'listar_locacoes.djhtml')
