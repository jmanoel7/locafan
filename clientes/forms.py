# -*- coding: utf-8 -*-
from django import forms
from django.forms.widgets import TextInput, Select, DateInput
from django.contrib.localflavor.br.forms import BRStateChoiceField
from cep.widgets import CEPInput
from home.models import Cliente


class ClienteCadastrarForm(forms.ModelForm):


    class Meta:
        model = Cliente
        exclude = ('multa')
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
            'cpf': TextInput(
                attrs={
                    'placeholder': '___.___.___-__',
                    'maxlength': '14',
                },
            ),
            'cep': CEPInput(
                address={
                    'street':   'id_end',
                    'district': 'id_bairro',
                    'city':     'id_cidade',
                    'state':    'id_uf',
                },
                attrs={
                    'placeholder': '_____-___',
                    'maxlength': '9',
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
            'tel_fixo': TextInput(
                attrs={
                    'placeholder': '(__) ____-____',
                    'maxlength': '14',
                },
            ),
            'tel_cel': TextInput(
                attrs={
                    'placeholder': '(__) ____-____',
                    'maxlength': '14',
                },
            ),
            'tel_trab': TextInput(
                attrs={
                    'placeholder': '(__) ____-____',
                    'maxlength': '14',
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
         js = ('site/clientes/form.js', 'site/jquery-mask/jquery.mask.min.js',)


class ClienteEditarForm(forms.ModelForm):

    class Meta:
        model = Cliente
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
            'cpf': TextInput(
                attrs={
                    'placeholder': '___.___.___-__',
                    'maxlength': '14',
                },
            ),
            'cep': CEPInput(
                address={
                    'street':   'id_end',
                    'district': 'id_bairro',
                    'city':     'id_cidade',
                    'state':    'id_uf',
                },
                attrs={
                    'placeholder': '_____-___',
                    'maxlength': '9',
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
            'tel_fixo': TextInput(
                attrs={
                    'placeholder': '(__) ____-____',
                    'maxlength': '14',
                },
            ),
            'tel_cel': TextInput(
                attrs={
                    'placeholder': '(__) ____-____',
                    'maxlength': '14',
                },
            ),
            'tel_trab': TextInput(
                attrs={
                    'placeholder': '(__) ____-____',
                    'maxlength': '14',
                },
            ),
            'email': TextInput(
                attrs={
                    'placeholder': 'Digite o email',
                    'onblur':      'this.value=trim_js(this.value)',
                },
            ),
            'multa': TextInput(
                attrs={
                    'placeholder': '000000,00',
                    'maxlength': '9',
                },
            ),
        }

    class Media:
         css = {
             'all': ('site/clientes/form.css',)
         }
         js = ('site/clientes/form.js', 'site/jquery-mask/jquery.mask.min.js',)


class ClienteExcluirForm(forms.ModelForm):

    class Meta:
        model = Cliente
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
                    'class': 'input_multa',
                    'max_length': '7',
                    'readonly': 'true'
                }
            ),
        }

    class Media:
         css = {
             'all': ('site/clientes/form.css',)
         }
         js = ('site/clientes/form.js', 'site/jquery-mask/jquery.mask.min.js',)

