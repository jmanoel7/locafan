# -*- coding: utf-8 -*-
from django.shortcuts import render

def cadastrar(request):
    return render(request, 'cadastrar_fantasias.djhtml')

def buscar(request):
    return render(request, 'buscar_fantasias.djhtml')

def listar(request):
    return render(request, 'listar_fantasias.djhtml')
