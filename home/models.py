# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.localflavor.br.br_states import STATE_CHOICES
#from django.template.defaultfilters import default


class Cliente(models.Model):

    SEXO_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
    )
    nome = models.CharField(
        u'Nome',
        max_length=100,
        unique=True,
    )
    sexo = models.CharField(
        u'Sexo',
        max_length=1,
        choices=SEXO_CHOICES,
        default='M',
    )
    dt_nascimento = models.DateField(
        u'Data de Nascimento',
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
    cep = models.CharField(
        u'CEP',
        help_text=u'Ao inserir o CEP, os dados do endereço serão preenchidos \
            automaticamente.\nCaso isso não ocorra os dados do endereço \
            deverão ser preenchidos manualmente.',
        max_length=8,
    )
    end = models.CharField(
        u'Endereço',
        max_length=100,
    )
    end_comp = models.CharField(
        u'* Complemento',
        max_length=100,
        blank=True,
        null=True,
    )
    bairro = models.CharField(
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
    tel_fixo = models.CharField(
        u'* Telefone Fixo',
        max_length=10,
        blank=True,
        null=True,
    )
    tel_cel = models.CharField(
        u'Telefone Celular',
        max_length=10,
    )
    tel_trab = models.CharField(
        u'* Telefone do Trabalho',
        max_length=10,
        blank=True,
        null=True,
    )
    email = models.EmailField(
        u'* Email',
        max_length=100,
        blank=True,
        null=True,
    )
    multa = models.DecimalField(
        u'Multa',
        default=0.00,
        max_digits=6,
        decimal_places=2,
    )
    tem_locacao = models.BooleanField(
        u'Possui locação em aberto?',
        default=False,
    )

    def __unicode__(self):
        return 'Nome: %s, CPF: %s' % (
            self.nome,
            self.cpf,
        )


class Fantasia(models.Model):

    TIPOS_DE_FANTASIAS = (
        ('IM', 'Infantil Masculino'),
        ('IF', 'Infantil Feminino'),
        ('AF', 'Adulto Feminino'),
        ('AM', 'Adulto Masculino'),
        ('CS', 'Casal'),
    )
    nome = models.CharField(
        u'Nome da Fantasia',
        max_length=50,
    )
    tipo = models.CharField(
        u'Tipo da Fantasia',
        max_length=2,
        choices=TIPOS_DE_FANTASIAS,
    )
    tema = models.CharField(
        u'Tema da Fantasia',
        max_length=50,
    )
    valor_fantasia = models.DecimalField(
        u'Valor da Fantasia',
        default=300.00,
        max_digits=6,
        decimal_places=2,
    )
    valor_locacao = models.DecimalField(
        u'Valor da Locação',
        default=3.00,
        max_digits=6,
        decimal_places=2,
    )
    qtde_total = models.IntegerField(
        u'Quantidade Total',
        default=1,
    )
    qtde_disponivel = models.IntegerField(
        u'Quantidade Disponível',
        default=1,
    )

    def __unicode__(self):
        return 'NOME: %s, TIPO: %s, TEMA: %s, DISPONIVEIS: %s' % (
            self.nome,
            self.tipo,
            self.tema,
            self.qtde_disponivel,
        )


class Locacao(models.Model):

    dt_locacao = models.DateField(
        u'Data de Locação',
    )
    dt_devolucao = models.DateField(
        u'Data de Devolução',
    )
    pg_realizado = models.DecimalField(
        u'Pagamento Realizado',
        default=0.00,
        max_digits=6,
        decimal_places=2,
    )
    status = models.BooleanField(
        u'Status da Locação',
    )
    cliente = models.ForeignKey(Cliente)
    fantasias = models.ManyToManyField(Fantasia)

    def __unicode__(self):
        return u'CLIENTE: %s, DATA DE LOCAÇÃO: %s, DATA DE DEVOLUÇÃO: %s' % (
            self.cliente,
            self.dt_locacao,
            self.dt_devolucao,
        )
