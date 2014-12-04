# -*- coding: utf-8 -*-
from django import forms
from django.forms.widgets import TextInput, Select, DateInput
from django.contrib.localflavor.br.forms import BRStateChoiceField
from cep.widgets import CEPInput
from home.models import Cliente


class ClienteCadastrarForm(forms.ModelForm):

    cpf = forms.CharField(
        label=u'CPF',
        max_length=14,
        widget=forms.TextInput(
            attrs={
                'placeholder': '___.___.___-__',
            },
        ),
    )
    cep = forms.CharField(
        label=u'CEP',
        max_length=9,
        help_text=u'Ao inserir o CEP, os dados do endereço serão preenchidos automaticamente.\nCaso isso não ocorra os dados do endereço deverão ser preenchidos manualmente.',
        widget=CEPInput(
            address={
                'street':   'id_end',
                'district': 'id_bairro',
                'city':     'id_cidade',
                'state':    'id_uf',
            },
            attrs={
                'placeholder': '_____-___',
            },
        ),
    )
    tel_fixo = forms.CharField(
        label=u'* Telefone Fixo',
        required=False,
        max_length=14,
        widget=forms.TextInput(
            attrs={
                'placeholder': '(__) ____-____',
            },
        ),
    )
    tel_cel = forms.CharField(
        label=u'Telefone Celular',
        max_length=14,
        widget=forms.TextInput(
            attrs={
                'placeholder': '(__) ____-____',
            },
        ),
    )
    tel_trab = forms.CharField(
        label=u'* Telefone do Trabalho',
        required=False,
        max_length=14,
        widget=forms.TextInput(
            attrs={
                'placeholder': '(__) ____-____',
            },
        ),
    )

    class Meta:
        model = Cliente
        exclude = ('multa','tem_locacao',)
        widgets = {
            'nome': TextInput(
                attrs={
                    'placeholder': 'Digite o nome',
                    'onkeypress':  'mascara(this,mascara_nome)',
                    'onblur':      'this.value=trim_js(this.value)',
                },
            ),
            'dt_nascimento': DateInput(
                attrs={
                    'placeholder': 'dd/mm/aaaa',
                    'maxlength':   '10',
                },
            ),
            'rg': TextInput(
                attrs={
                    'placeholder': 'Digite o RG',
                    'onblur':      'this.value=trim_js(this.value)',
                },
            ),
            'end': TextInput(
                attrs={
                    'placeholder': 'Digite o endereço',
                    'onblur':      'this.value=trim_js(this.value)',
                },
            ),
            'end_comp': TextInput(
                attrs={
                    'placeholder': 'Digite o complemento',
                    'onblur':      'this.value=trim_js(this.value)',
                },
            ),
            'bairro': TextInput(
                attrs={
                    'placeholder': 'Digite o bairro',
                    'onblur':      'this.value=trim_js(this.value)',
                },
            ),
            'cidade': TextInput(
                attrs={
                    'placeholder': 'Digite a cidade',
                    'onblur':      'this.value=trim_js(this.value)',
                },
            ),
            'email': TextInput(
                attrs={
                    'placeholder': 'Digite o email',
                    'onblur':      'this.value=trim_js(this.value)',
                },
            ),
        }

    class Media:
         css = {
             'all': ('site/clientes/form.css',)
         }
         js = (
             'site/clientes/form.js',
             'site/jquery-mask/jquery.mask.min.js',
         )


class ClienteEditarForm(ClienteCadastrarForm):

    class Meta(ClienteCadastrarForm.Meta):
        exclude = ('tem_locacao',)
        widgets = {
            'multa': TextInput(
                attrs={
                    'placeholder': '000.000,00',
                    'maxlength': '10',
                },
            ),
        }

class ClienteExcluirForm(ClienteEditarForm):

    class Meta(ClienteEditarForm.Meta):
        widgets = {
            'nome': TextInput(
                attrs={
                    'class': 'input_nome',
                    'readonly': 'true'
                }
            ),
            'dt_nascimento': DateInput(
                attrs={
                    'class': 'input_dt_nascimento',
                    'maxlength': '10',
                    'readonly': 'true'
                }
            ),
            'cpf': TextInput(
                attrs={
                    'class': 'input_cpf',
                    'max_length': '14',
                    'readonly': 'true'
                }
            ),
            'rg': TextInput(
                attrs={
                    'class': 'input_rg',
                    'readonly': 'true'
                }
            ),
            'cep': TextInput(
                attrs={
                    'class': 'input_cep',
                    'max_length': '9',
                    'readonly': 'true'
                }
            ),
            'end': TextInput(
                attrs={
                    'class': 'input_end',
                    'readonly': 'true'
                }
            ),
            'end_comp': TextInput(
                attrs={
                    'class': 'input_end_comp',
                    'readonly': 'true'
                }
            ),
            'bairro': TextInput(
                attrs={
                    'class': 'input_bairro',
                    'readonly': 'true'
                }
            ),
            'cidade': TextInput(
                attrs={
                    'class': 'input_cidade',
                    'readonly': 'true'
                }
            ),
            'uf': Select(
                attrs={
                    'class': 'input_uf',
                    'readonly': 'true'
                }
            ),
            'tel_fixo': TextInput(
                attrs={
                    'class': 'input_tel_fixo',
                    'max_length': '14',
                    'readonly': 'true'
                }
            ),
            'tel_cel': TextInput(
                attrs={
                    'class': 'input_tel_cel',
                    'max_length': '14',
                    'readonly': 'true'
                }
            ),
            'tel_trab': TextInput(
                attrs={
                    'class': 'input_tel_trab',
                    'max_length': '14',
                    'readonly': 'true'
                }
            ),
            'email': TextInput(
                attrs={
                    'class': 'input_email',
                    'readonly': 'true'
                }
            ),
            'multa': TextInput(
                attrs={
                    'readonly': 'true',
                }
            ),
        }

