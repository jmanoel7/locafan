# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from decimal import Decimal, ROUND_HALF_DOWN
from datetime import date

from home.models import Locacao, Fantasia, Cliente
from locacoes.forms import LocacaoCadastrarForm, LocacaoEditarForm, \
    LocacaoExcluirForm


def cadastrar(request):
    if request.method == 'POST':
        form = LocacaoCadastrarForm(request.POST)
        if form.is_valid():
            nova_locacao = form.save()
            cli = Cliente.objects.get(id=nova_locacao.cliente.id)
            cli.tem_locacao = True
            cli.save()
            for fantasia in nova_locacao.fantasias.all():
                fant = Fantasia.objects.get(id=fantasia.id)
                fant.tem_locacao = True
                fant.save()
            return render(request, 'locacoes_form_ok.html', {
                'tarefa': u'Cadastro',
                'cliente': nova_locacao.cliente.nome,
                'dt_devolucao': nova_locacao.dt_devolucao,
                'genero': 'o',
            })
    else:
        form = LocacaoCadastrarForm()
    dt_locacao = date.today()
    dt_locacao = str(dt_locacao).split("-")
    dt_locacao = dt_locacao[2] + "/" + dt_locacao[1] + "/" + dt_locacao[0]
    dt_devolucao = date.fromordinal(date.today().toordinal() + 7)
    dt_devolucao = str(dt_devolucao).split("-")
    dt_devolucao = dt_devolucao[2] + "/" + \
        dt_devolucao[1] + "/" + dt_devolucao[0]
    return render(request, 'locacoes_form.html', {
        'form': form,
        'tarefa': u'Cadastrar Locação',
        'botao': 'Cadastrar',
        'data_locacao': dt_locacao,
        'data_devolucao': dt_devolucao,
    })


def receber(request, id):
    locacao = get_object_or_404(
        Locacao, id=id,
    )
    atraso = date.today().toordinal() - locacao.dt_devolucao.toordinal()
    if atraso < 0:
        atraso = 0
    atraso = Decimal(atraso).quantize(
        Decimal('.01'),
        rounding=ROUND_HALF_DOWN,
    )
    ctot = Decimal(0.00)
    for fantasia in locacao.fantasias.all():
        ctot = Decimal(
            ctot + Decimal(7.0) * fantasia.valor_locacao
        ).quantize(
            Decimal('.01'),
            rounding=ROUND_HALF_DOWN,
        )
    ctot = Decimal(ctot).quantize(
        Decimal('.01'),
        rounding=ROUND_HALF_DOWN,
    )
    multa = Decimal(atraso * Decimal(0.1) * ctot).quantize(
        Decimal('.01'),
        rounding=ROUND_HALF_DOWN,
    )
    pg_total_apagar = Decimal(multa + ctot).quantize(
        Decimal('.01'),
        rounding=ROUND_HALF_DOWN,
    )
    if request.method == 'POST':
        form = LocacaoEditarForm(request.POST, instance=locacao)
        if form.is_valid():
            edit_locacao = form.save(commit=False)
            edit_locacao.status = False
            edit_locacao.save()
            form.save_m2m()
            pg_apagar = edit_locacao.pg_apagar
            pg_realizado = edit_locacao.pg_realizado
            cli = Cliente.objects.get(id=edit_locacao.cliente.id)
            cli.tem_locacao = False
            if pg_apagar < (pg_total_apagar - pg_realizado):
                cli.multa = cli.multa + \
                    (pg_total_apagar - pg_realizado - pg_apagar)
            cli.save()
            for fantasia in edit_locacao.fantasias.all():
                for loc in Locacao.objects.filter(
                    fantasias__nome=fantasia.nome,
                    fantasias__tipo=fantasia.tipo,
                    fantasias__tema=fantasia.tema,
                ):
                    if loc.status:
                        fantasia.tem_locacao = True
                        break
                    else:
                        fantasia.tem_locacao = False
                fantasia.save()
            return render(request, 'locacoes_form_ok.html', {
                'tarefa': u'Baixa',
                'cliente': edit_locacao.cliente.nome,
                'dt_devolucao': edit_locacao.dt_devolucao,
                'genero': 'a',
            })
    else:
        form = LocacaoEditarForm(instance=locacao)
    return render(request, 'locacoes_form.html', {
        'form': form,
        'cliente': locacao.cliente.nome,
        'dt_devolucao': locacao.dt_devolucao,
        'tarefa': u'Receber Locação',
        'botao': 'Receber',
        'data_locacao': locacao.dt_locacao,
        'data_devolucao': locacao.dt_devolucao,
        'pg_total_apagar': pg_total_apagar,
    })


def listar(request):

    locacoes = Locacao.objects.filter(status=True)
    #nome_cliente=Cliente.objects.get(id=locacoes.cliente_id).nome
    return render(request, 'locacoes_lista.html', {
        'locacoes': locacoes,
        'titulo_lista': u'Lista de Locações em Aberto',
        'msg_lista_vazia': u'Não temos nenhuma Locação em Aberto.'
    })


def excluir(request, id):

    locacao = get_object_or_404(
        Locacao, id=id,
    )
    if request.method == 'POST':
        cli = Cliente.objects.get(id=locacao.cliente.id)
        cli.tem_locacao = False
        nome = cli.nome
        cli.save()
        fantasias = locacao.fantasias.all()
        dt_devolucao = locacao.dt_devolucao
        locacao.delete()
        locacao.save()
        for fantasia in fantasias:
            for loc in Locacao.objects.filter(
                fantasias__nome=fantasia.nome,
                fantasias__tipo=fantasia.tipo,
                fantasias__tema=fantasia.tema,
            ):
                if loc.status:
                    fantasia.tem_locacao = True
                    break
                else:
                    fantasia.tem_locacao = False
            fantasia.save()
        return render(request, 'locacoes_form_ok.html', {
            'tarefa': u'Exclusão',
            'cliente': nome,
            'dt_devolucao': dt_devolucao,
            'genero': 'a',
        })
    else:
        form = LocacaoExcluirForm(instance=locacao)
        return render(request, 'locacoes_form.html', {
            'form': form,
            'cliente': locacao.cliente.nome,
            'dt_devolucao': locacao.dt_devolucao,
            'tarefa': u'Excluir Locação',
            'botao': 'Excuir',
            'data_locacao': locacao.dt_locacao,
            'data_devolucao': locacao.dt_devolucao,
        })
