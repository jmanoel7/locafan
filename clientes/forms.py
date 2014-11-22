# -*- coding: utf-8 -*-
from django import forms
from django.contrib.localflavor.br.forms import BRStateChoiceField
from cep.widgets import CEPInput

from home.models import Clientes

#class ClientesCadastrarForm(forms.ModelForm):
#    
#    class Meta:
#        model = Clientes
#        exclude = ('multa')

#class ClientesEditarForm(forms.ModelForm):
#    
#    class Meta:
#        model = Clientes

class ClientesCadastrarForm(forms.Form):
    nome = forms.CharField(
        label=u'Nome',
        widget=forms.TextInput(
            attrs={
                'class': 'input_nome',
                'placeholder': 'Digite o nome',
            },
        ),
    )
    rg = forms.CharField(
        label=u'RG',
        widget=forms.TextInput(
            attrs={
                'class': '_input_rg',
                'placeholder': 'Digite o RG',
            },
        ),
    )
    cpf = forms.CharField(
        label=u'CPF',
        widget=forms.TextInput(
            attrs={
                'class': 'input_cpf',
                'maxlength': '14',
                'placeholder': '___.___.___-__',
            },
        ),
    )
    cep = forms.IntegerField(
        label=u'CEP',
        widget=CEPInput(
            address={
                'street': 'id_end',
                'district': 'id_bairro',
                'city': 'id_cidade',
                'state': 'id_uf',
            },
            attrs={
                'class': 'input_cep',
                'placeholder': '_____-___',
            },
        ),
        help_text=u'Ao inserir o CEP, os dados do endereço serão preenchidos automaticamente.',
    )
    end = forms.CharField(
        label=u'Endereço',
        widget=forms.TextInput(
            attrs={
                'class': 'input_end',
                'placeholder': 'Digite o endereço',
            },
        ),
    )
    end_comp = forms.CharField(
        label=u'Complemento',
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'input_end_comp',
                'placeholder': 'Digite o complemento',
            },
        ),
    )
    bairro = forms.CharField(
        label=u'Bairro',
        widget=forms.TextInput(
            attrs={
                'class': 'input_bairro',
                'placeholder': 'Digite o bairro',
            },
        ),
    )
    cidade = forms.CharField(
        label=u'Cidade',
        widget=forms.TextInput(
            attrs={
                'class': 'input_cidade',
                'placeholder': 'Digite a cidade',
            },
        ),
    )
    uf = BRStateChoiceField(
        label=u'Estado',
        widget=forms.Select(
            attrs={
                'class': 'input_uf',
            },
        ),
    )
    tel_fixo = forms.CharField(
        label=u'Telefone fixo',
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'input_tel_fixo',
                'maxlength': '14',
                'placeholder': '(__) ____-____',
            },
        ),
    )
    tel_cel = forms.CharField(
        label=u'Telefone celular',
        widget=forms.TextInput(
            attrs={
                'class': 'input_tel_cel',
                'maxlength': '14',
                'placeholder': '(__) ____-____',
            },
        ),
    )
    tel_trab = forms.CharField(
        label=u'Telefone trabalho',
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'input_tel_trab',
                'maxlength': '14',
                'placeholder': '(__) ____-____',
            },
        ),
    )
    email = forms.EmailField(
        label=u'Email',
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'input_email',
                'placeholder': 'Digite o email',
            },
        ),
    )

class ClientesEditarForm(ClientesCadastrarForm):
        multa = forms.FloatField(
            label=u'Multa',
            min_value=0.00,
            widget=forms.TextInput(
                attrs={
                    'class': 'input_multa',
                    'placeholder': '0.000,00',
                },
            ),
        )
