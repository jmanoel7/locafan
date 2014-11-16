# -*- coding: utf-8 -*-
from django.shortcuts import render

def cadastrar(request):
    return render(request, 'cadastrar_clientes.djhtml')

def buscar(request):
    return render(request, 'buscar_clientes.djhtml')

def listar(request):
    return render(request, 'listar_clientes.djhtml')
