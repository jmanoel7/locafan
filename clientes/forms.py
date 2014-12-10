# -*- coding: utf-8 -*-
import datetime
from django import forms
from cep.widgets import CEPInput
from home.models import Cliente


class NomeField(forms.Field):

    def validate(self, value):
        """Checa se o value consiste em um valor não nulo."""

        # Usa a manipulação da classe pai de campos obrigatórios
        super(NomeField, self).validate(value)

        # Valida se o nome eh vazio
        if not value:
            raise forms.ValidationError(
                u'Informe uma parte do nome para busca.'
            )
        return None


class DataNascimentoField(forms.DateField):

    def validate(self, value):
        """Checa se o valor consiste em uma data de nascimento válida."""

        # Usa a manipulação da classe pai de campos obrigatórios
        super(DataNascimentoField, self).validate(value)

        # Valida a data de nascimento
        if value < datetime.date(1900, 1, 1):
            raise forms.ValidationError(
                u'Informe uma data a partir de 01/01/1900.'
            )
        return None


class CPFField(forms.Field):

    def validate(self, value):
        """Checa se o valor consiste em um CPF válido."""

        # Usa a manipulação da classe pai de campos obrigatórios
        super(CPFField, self).validate(value)

        # Valida o CPF
        if len(value) != 11:
            raise forms.ValidationError(u'Informe um CPF com 11 dígitos.')
        c = value[:9]
        dv = value[-2:]
        d1 = 0
        for i in range(9):
            d1 = d1 + int(c[i]) * (10 - i)
        if d1 == 0:
            raise forms.ValidationError(u'Informe um CPF válido.')
        d1 = 11 - (d1 % 11)
        if d1 > 9:
            d1 = 0
        if int(dv[0]) != d1:
            raise forms.ValidationError(u'Informe um CPF válido.')
        d1 = d1 * 2
        for i in range(9):
            d1 = d1 + int(c[i]) * (11 - i)
        d1 = 11 - (d1 % 11)
        if d1 > 9:
            d1 = 0
        if int(dv[1]) != d1:
            raise forms.ValidationError(u'Informe um CPF válido.')
        return None


class ClienteCadastrarForm(forms.ModelForm):

    dt_nascimento = DataNascimentoField(
        label=u'Data de Nascimento',
        widget=forms.DateInput(
            attrs={
                'placeholder': 'dd/mm/aaaa',
                'maxlength': '10',
            },
        ),
    )
    cpf = CPFField(
        label=u'CPF',
        widget=forms.TextInput(
            attrs={
                'placeholder': '___.___.___-__',
                'maxlength': '14',
            },
        ),
    )
    cep = forms.CharField(
        label=u'CEP',
        max_length=9,
        help_text=u'Ao inserir o CEP, os dados do endereço serão preenchidos \
automaticamente.\nCaso isso não ocorra os dados do endereço \
deverão ser preenchidos manualmente.',
        widget=CEPInput(
            address={
                'street': 'id_end',
                'district': 'id_bairro',
                'city': 'id_cidade',
                'state': 'id_uf',
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
        exclude = ('multa', 'tem_locacao',)
        widgets = {
            'nome': forms.TextInput(
                attrs={
                    'placeholder': 'Digite o nome',
                    'onkeypress': 'mascara(this,mascara_nome)',
                    'onblur': 'this.value=trim_js(this.value)',
                },
            ),
            'rg': forms.TextInput(
                attrs={
                    'placeholder': 'Digite o RG',
                    'onblur': 'this.value=trim_js(this.value)',
                },
            ),
            'end': forms.TextInput(
                attrs={
                    'placeholder': 'Digite o endereço',
                    'onblur': 'this.value=trim_js(this.value)',
                },
            ),
            'end_comp': forms.TextInput(
                attrs={
                    'placeholder': 'Digite o complemento',
                    'onblur': 'this.value=trim_js(this.value)',
                },
            ),
            'bairro': forms.TextInput(
                attrs={
                    'placeholder': 'Digite o bairro',
                    'onblur': 'this.value=trim_js(this.value)',
                },
            ),
            'cidade': forms.TextInput(
                attrs={
                    'placeholder': 'Digite a cidade',
                    'onblur': 'this.value=trim_js(this.value)',
                },
            ),
            'email': forms.TextInput(
                attrs={
                    'placeholder': 'Digite o email',
                    'onblur': 'this.value=trim_js(this.value)',
                },
            ),
        }

    class Media:
        css = {
             'all': (
                 'site/myscripts/clientes_form.css',
                 'site/jquery-chosen/chosen.min.css',
             )
        }
        js = (
             'site/myscripts/clientes_form.js',
             'site/jquery-mask/jquery.mask.min.js',
             'site/jquery-chosen/chosen.jquery.min.js',
         )


class ClienteBuscarNomeForm(forms.Form):

    nome = NomeField(
        label=u'Nome',
        help_text=u'Informe pelo menos a parte de um nome para busca.\n\
Isto é, informe pelo menos uma sílaba de um nome.',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Digite o Nome',
                'maxlength': '100',
            },
        ),
    )

    class Media:
        css = {
             'all': (
                 'site/myscripts/clientes_form.css',
                 'site/jquery-chosen/chosen.min.css',
             )
        }
        js = (
             'site/myscripts/clientes_form.js',
             'site/jquery-mask/jquery.mask.min.js',
             'site/jquery-chosen/chosen.jquery.min.js',
         )


class ClienteBuscarCPFForm(forms.Form):

    cpf = CPFField(
        label=u'CPF',
        help_text=u'Informe um CPF válido de um cliente cadastrado.',
        widget=forms.TextInput(
            attrs={
                'placeholder': '___.___.___-__',
                'maxlength': '14',
            },
        ),
    )

    class Media:
        css = {
             'all': (
                 'site/myscripts/clientes_form.css',
                 'site/jquery-chosen/chosen.min.css',
             )
        }
        js = (
             'site/myscripts/clientes_form.js',
             'site/jquery-mask/jquery.mask.min.js',
             'site/jquery-chosen/chosen.jquery.min.js',
         )


class ClienteEditarForm(ClienteCadastrarForm):

    class Meta(ClienteCadastrarForm.Meta):
        exclude = ('tem_locacao',)
        widgets = {
            'multa': forms.TextInput(
                attrs={
                    'placeholder': '000.000,00',
                    'maxlength': '10',
                },
            ),
        }


class ClienteExcluirForm(ClienteEditarForm):

    dt_nascimento = forms.DateField(
        label=u'Data de Nascimento',
        widget=forms.DateInput(
            attrs={
                'disabled': 'true',
                'class': 'input_readonly',
            },
        ),
    )
    cpf = forms.CharField(
        label=u'CPF',
        max_length=14,
        widget=forms.TextInput(
            attrs={
                'disabled': 'true',
                'class': 'input_readonly',
            },
        ),
    )
    cep = forms.CharField(
        label=u'CEP',
        max_length=9,
        widget=forms.TextInput(
            attrs={
                'disabled': 'true',
                'class': 'input_readonly',
            },
        ),
    )
    tel_fixo = forms.CharField(
        label=u'Telefone Fixo',
        max_length=14,
        widget=forms.TextInput(
            attrs={
                'disabled': 'true',
                'class': 'input_readonly',
                },
            ),
    )
    tel_cel = forms.CharField(
        label=u'Telefone Celular',
        max_length=14,
        widget=forms.TextInput(
            attrs={
                'disabled': 'true',
                'class': 'input_readonly',
                },
            ),
    )
    tel_trab = forms.CharField(
        label=u'Telefone do Trabalho',
        max_length=14,
        widget=forms.TextInput(
            attrs={
                'disabled': 'true',
                'class': 'input_readonly',
                },
            ),
    )
    multa = forms.CharField(
        label=u'Multa',
        max_length=10,
        widget=forms.TextInput(
            attrs={
                'disabled': 'true',
                'class': 'input_readonly',
            },
        ),
    )
    end_comp = forms.CharField(
        label=u'Complemento',
        widget=forms.TextInput(
            attrs={
                'disabled': 'true',
                'class': 'input_readonly',
            },
        ),
    )
    email = forms.CharField(
        label=u'Email',
        widget=forms.TextInput(
            attrs={
                'disabled': 'true',
                'class': 'input_readonly',
            },
        ),
    )

    class Meta(ClienteEditarForm.Meta):
        widgets = {
            'nome': forms.TextInput(
                attrs={
                    'disabled': 'true',
                    'class': 'input_readonly',
                },
            ),
            'sexo': forms.Select(
                attrs={
                    'disabled': 'true',
                    'class': 'input_readonly',
                },
            ),
            'rg': forms.TextInput(
                attrs={
                    'disabled': 'true',
                    'class': 'input_readonly',
                },
            ),
            'end': forms.TextInput(
                attrs={
                    'disabled': 'true',
                    'class': 'input_readonly',
                },
            ),
            'bairro': forms.TextInput(
                attrs={
                    'disabled': 'true',
                    'class': 'input_readonly',
                },
            ),
            'cidade': forms.TextInput(
                attrs={
                    'disabled': 'true',
                    'class': 'input_readonly',
                },
            ),
            'uf': forms.Select(
                attrs={
                    'disabled': 'true',
                    'class': 'input_readonly',
                },
            ),
        }
