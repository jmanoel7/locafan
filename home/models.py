# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.localflavor.br.br_states import STATE_CHOICES
from django.template.defaultfilters import default

class Clientes(models.Model):

    nome = models.CharField(
        u'Nome',
        max_length=100,
        unique=True,
    )
    rg = models.CharField(
        u'RG',
        max_length=50,
        unique=True,
    )
    cpf = models.CharField(
        u'CPF',
        max_length=11,
        unique=True,
    )
    end = models.CharField(
        u'Endereço',
        max_length=100,
    )
    end_comp = models.CharField(
        u'Complemento',
        max_length=100,
        blank=True,
        null=True,
    )
    bairo = models.CharField(
        u'Bairro',
        max_length=100,
    )
    cidade = models.CharField(
        u'Cidade',
        max_length=100,
    )
    uf = models.CharField(
        u'Estado',
        max_length=2,
        choices=STATE_CHOICES,
        default='GO',
    )
    cep = models.CharField(
        u'CEP',
        max_length=8,
    )
    tel_fixo = models.CharField(
        u'Telefone Fixo',
        max_length=11,
        blank=True,
        null=True,
    )
    tel_cel = models.CharField(
        u'Telefone Celular',
        max_length=11,
    )
    tel_trab = models.CharField(
        u'Telefone Trabalho',
        max_length=11,
        blank=True,
        null=True,
    )
    email = models.EmailField(
        u'Email',
        max_length=100,
        blank=True,
        null=True,
    )
    multa = models.FloatField(
        u'Multa',
        default=0.00,
    )
    
    def __unicode__(self):
        return 'Nome: %s, CPF: %s, Multa: %s' % (
            self.nome,
            self.cpf,
            self.multa,
        )
        
class Locacoes(models.Model):
    
    dt_locacao = models.DateField(
        u'Data de Locação',
    )
    dt_devolucao = models.DateField(
        u'Data de Devolução',
    )
    pg_realizado = models.FloatField(
        u'Pagamento Realizado',
    )
    cliente_id = models.ForeignKey(
        Clientes,
        unique = True,
    )
    
    def __unicode__(self):
        return 'DATA DE LOCAÇÃO: %s, DATA DE DEVOLUÇÃO: %s' % (
            self.dt_locacao,
            self.dt_devolucao,
        )

class Fantasias(models.Model):

    nome = models.CharField(
        u'Nome',
        max_length=50,
    )
    tipo = models.CharField(
        u'Tipo',
        max_length=50,
    )
    tema = models.CharField(
        u'Tema',
        max_length=50,
    )
    valor_fantasia = models.FloatField(
        u'Valor da Fantasia',
    )
    valor_locacao = models.FloatField(
        u'Valor da Locação',
    )
    qtde_total = models.IntegerField(
        u'Quantidade Total',
    )
    qtde_disponivel = models.IntegerField(
        u'Quantidade Disponível',
    )
    locacao_id = models.ForeignKey(
        Locacoes,
        unique=True,
    )
    locacao_cliente_id = models.ForeignKey(
        Locacoes,
        unique=True,
        related_name='locacao_cliente_id',
        to_field='cliente_id',
    )

    def __unicode__(self):
        return 'NOME: %s, TIPO: %s, TEMA: %s, DISPONIVEIS: %s' % (
            self.nome,
            self.tipo,
            self.tema,
            self.qtde_disponivel,
        )
