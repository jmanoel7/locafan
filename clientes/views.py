# -*- coding: utf-8 -*-
from django.shortcuts import render

def cadastrar(request):
    return render(request, 'cadastrar_clientes.djhtml')

def editar(request):
    return render(request, 'buscar_clientes.djhtml', {'acao': 'Editar'})

def listar(request):
    return render(request, 'listar_clientes.djhtml')

def excluir(request):
    return render(request, 'buscar_clientes.djhtml', {'acao': 'Excluir'})
