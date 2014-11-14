# -*- coding: utf-8 -*-
from django.shortcuts import render

def cliente(request):
    return render(request, 'cliente.html')

def fantasia(request):
    return render(request, 'fantasia.html')

def locacao(request):
    return render(request, 'locacao.html')
