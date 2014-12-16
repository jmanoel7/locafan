# -*- coding: utf-8 -*-
import re


def mascara_valor(valor):

    '''poe a mascara de "000.000.000.000.000,00" em valor'''

    # se valor eh vazio retorne '0,00'
    if not valor:
        valor = '0,00'
        return valor

    # normaliza o parâmetro valor
    valor = str(valor)

    # tira tudo o que não é digito e ponto de valor
    valor = re.sub(r'[^0-9\.]', r'', valor)

    # troca '.' por ',' no valor
    valor = re.sub(r'\.', r',', valor)

    # verifica se há apenas digitos em valor, senão retorna None
    if not valor.replace(',', '', 1).isdigit():
        return None

    # verifica se não tem ',' e se for o caso põe ',00' no fim
    if valor.count(',') == 0:
        valor = re.sub(r'$', r',00', valor)

    # Coloca um zero no fim se necessário
    valor = re.sub(r'(,\d)$', r'\1 0', valor)
    valor = valor.replace(' ', '')

    # Coloca um zero antes da vírgula se necessário
    valor = re.sub(r'^(,\d{2})$', r'0\1', valor)

    # Coloca um ponto antes dos 5 últimos dígitos
    valor = re.sub(r'(\d)(\d{3}),(\d{2})$', r'\1.\2,\3', valor)

    # Coloca um ponto antes dos 8 últimos dígitos
    valor = re.sub(r'(\d)(\d{3})\.(\d{3}),(\d{2})$', r'\1.\2.\3,\4', valor)

    # Coloca um ponto antes dos 11 últimos dígitos
    valor = re.sub(
        r'(\d)(\d{3})\.(\d{3})\.(\d{3}),(\d{2})$',
        r'\1.\2.\3.\4,\5',
        valor
    )

    # Coloca um ponto antes dos 14 últimos dígitos
    valor = re.sub(
        r'(\d)(\d{3})\.(\d{3})\.(\d{3})\.(\d{3}),(\d{2})$',
        r'\1.\2.\3.\4.\5,\6',
        valor
    )

    return valor