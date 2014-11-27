# -*- coding: utf-8 -*-
from django import forms
from django.forms.widgets import TextInput, Select, DateInput
from django.contrib.localflavor.br.forms import BRStateChoiceField
from cep.widgets import CEPInput
from home.models import Clientes


class ClientesCadastrarForm(forms.ModelForm):

    nome = forms.CharField(
        label=u'Nome',
        help_text=u'Digite apenas letras com ou sem acentos.',
        widget=TextInput(
            attrs={
                'placeholder': 'Digite o nome',
                'onkeypress':  'mascara(this,mascara_nome)',
                'onblur':      'this.value=trim_js(this.value)',
            },
        ),
    )
    dt_nascimento = forms.DateField(
        label=u'Data de Nascimento',
        help_text=u'Digite a data no formato: dd/mm/aaaa',
        widget=DateInput(
            attrs={
                'placeholder': '__/__/____',
                'maxlength':   '10',
            },
        ),
    )
    rg = forms.CharField(
        label=u'RG',
        help_text=u'Digite o número do RG seguido do órgão expedidor.',
        widget=TextInput(
            attrs={
                'placeholder': 'Digite o RG',
                'onblur':      'this.value=trim_js(this.value)',
            },
        ),
    )
    cpf = forms.CharField(
        label=u'CPF',
        help_text=u'Digite apenas os números do CPF que o traço e os pontos aparecerão automaticamente.',
        max_length=14,
        widget=TextInput(
            attrs={
                'placeholder': '___.___.___-__',
            },
        ),
    )
    cep = forms.CharField(
        label=u'CEP',
        help_text=u'Ao inserir o CEP, os dados do endereço serão preenchidos automaticamente.\nCaso isso não ocorra os dados do endereço deverão ser preenchidos manualmente.',
        max_length=9,
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
    end = forms.CharField(
        label=u'Endereço',
        help_text=u'Este campo só deve ser preenchido manualmente no caso da busca do endereço pelo cep falhar.',
        widget=TextInput(
            attrs={
                'placeholder': 'Digite o endereço',
                'onblur':      'this.value=trim_js(this.value)',
            },
        ),
    )
    end_comp = forms.CharField(
        label=u'* Complemento',
        help_text=u'Número, Quadra, Lote, Apto, Bloco, etc.',
        required=False,
        widget=TextInput(
            attrs={
                'placeholder': 'Digite o complemento',
                'onblur':      'this.value=trim_js(this.value)',
            },
        ),
    )
    bairro = forms.CharField(
        label=u'Bairro',
        help_text=u'Este campo só deve ser preenchido manualmente no caso da busca do endereço pelo cep falhar.',
        widget=TextInput(
            attrs={
                'placeholder': 'Digite o bairro',
                'onblur':      'this.value=trim_js(this.value)',
            },
        ),
    )
    cidade = forms.CharField(
        label=u'Cidade',
        help_text=u'Este campo só deve ser preenchido manualmente no caso da busca do endereço pelo cep falhar.',
        widget=TextInput(
            attrs={
                'placeholder': 'Digite a cidade',
                'onblur':      'this.value=trim_js(this.value)',
            },
        ),
    )
    tel_fixo = forms.CharField(
        label=u'* Telefone Fixo',
        help_text=u'Digite apenas os digitos do telefone que o resto aparecerá automaticamente.',
        max_length=14,
        required=False,
    )
    tel_cel = forms.CharField(
        label=u'Telefone Celular',
        help_text=u'Digite apenas os digitos do telefone que o resto aparecerá automaticamente.',
        max_length=14,
    )
    tel_trab = forms.CharField(
        label=u'* Telefone Trabalho',
        help_text=u'Digite apenas os digitos do telefone que o resto aparecerá automaticamente.',
        max_length=14,
        required=False,
    )
    email = forms.CharField(
        label=u'* Email',
        help_text=u'Digite um email válido.',
        required=False,
        widget=TextInput(
            attrs={
                'placeholder': 'Digite o email',
                'onblur':      'this.value=trim_js(this.value)',
            },
        ),
    )

    class Meta:
        model = Clientes
        exclude = ('multa')

    class Media:
         css = {
             'all': ('site/clientes/form.css',)
         }
         js = ('site/clientes/form.js', 'site/jquery-mask/jquery.mask.min.js',)


class ClientesEditarForm(forms.ModelForm):

    nome = forms.CharField(
        label=u'Nome',
        help_text=u'Digite apenas letras com ou sem acentos.',
        widget=TextInput(
            attrs={
                'placeholder': 'Digite o nome',
                'onkeypress':  'mascara(this,mascara_nome)',
                'onblur':      'this.value=trim_js(this.value)',
            },
        ),
    )
    dt_nascimento = forms.DateField(
        label=u'Data de Nascimento',
        help_text=u'Digite a data no formato: dd/mm/aaaa',
        widget=DateInput(
            attrs={
                'placeholder': '__/__/____',
                'maxlength':   '10',
            },
        ),
    )
    rg = forms.CharField(
        label=u'RG',
        help_text=u'Digite o número do RG seguido do órgão expedidor.',
        widget=TextInput(
            attrs={
                'placeholder': 'Digite o RG',
                'onblur':      'this.value=trim_js(this.value)',
            },
        ),
    )
    cpf = forms.CharField(
        label=u'CPF',
        help_text=u'Digite apenas os números do CPF que o traço e os pontos aparecerão automaticamente.',
        max_length=14,
        widget=TextInput(
            attrs={
                'placeholder': '___.___.___-__',
            },
        ),
    )
    cep = forms.CharField(
        label=u'CEP',
        help_text=u'Ao inserir o CEP, os dados do endereço serão preenchidos automaticamente.\nCaso isso não ocorra os dados do endereço deverão ser preenchidos manualmente.',
        max_length=9,
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
    end = forms.CharField(
        label=u'Endereço',
        help_text=u'Este campo só deve ser preenchido manualmente no caso da busca do endereço pelo cep falhar.',
        widget=TextInput(
            attrs={
                'placeholder': 'Digite o endereço',
                'onblur':      'this.value=trim_js(this.value)',
            },
        ),
    )
    end_comp = forms.CharField(
        label=u'* Complemento',
        help_text=u'Número, Quadra, Lote, Apto, Bloco, etc.',
        required=False,
        widget=TextInput(
            attrs={
                'placeholder': 'Digite o complemento',
                'onblur':      'this.value=trim_js(this.value)',
            },
        ),
    )
    bairro = forms.CharField(
        label=u'Bairro',
        help_text=u'Este campo só deve ser preenchido manualmente no caso da busca do endereço pelo cep falhar.',
        widget=TextInput(
            attrs={
                'placeholder': 'Digite o bairro',
                'onblur':      'this.value=trim_js(this.value)',
            },
        ),
    )
    cidade = forms.CharField(
        label=u'Cidade',
        help_text=u'Este campo só deve ser preenchido manualmente no caso da busca do endereço pelo cep falhar.',
        widget=TextInput(
            attrs={
                'placeholder': 'Digite a cidade',
                'onblur':      'this.value=trim_js(this.value)',
            },
        ),
    )
    tel_fixo = forms.CharField(
        label=u'* Telefone Fixo',
        help_text=u'Digite apenas os digitos do telefone que o resto aparecerá automaticamente.',
        max_length=14,
        required=False,
    )
    tel_cel = forms.CharField(
        label=u'Telefone Celular',
        help_text=u'Digite apenas os digitos do telefone que o resto aparecerá automaticamente.',
        max_length=14,
    )
    tel_trab = forms.CharField(
        label=u'* Telefone Trabalho',
        help_text=u'Digite apenas os digitos do telefone que o resto aparecerá automaticamente.',
        max_length=14,
        required=False,
    )
    email = forms.CharField(
        label=u'* Email',
        help_text=u'Digite um email válido.',
        required=False,
        widget=TextInput(
            attrs={
                'placeholder': 'Digite o email',
                'onblur':      'this.value=trim_js(this.value)',
            },
        ),
    )
    multa = forms.DecimalField(
        label=u'Multa',
        help_text=u'Digite só os números do valor da multa, que a vírgula e o ponto aparecerão automaticamente.',
        max_value=10000.00,
        min_value=0.00,
        max_digits=6,
        decimal_places=2,
        widget=forms.TextInput(
            attrs={
                'class': 'input_multa',
                'placeholder': '0000,00',
                'maxlength': '7',
            },
        ),
    )

    class Meta:
        model = Clientes

    class Media:
         css = {
             'all': ('site/clientes/form.css',)
         }
         js = ('site/clientes/form.js', 'site/jquery-mask/jquery.mask.min.js',)

class ClientesExcluirForm(forms.ModelForm):

    class Meta:
        model = Clientes
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

