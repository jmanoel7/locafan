# -*- coding: utf-8 -*-
from django import forms
from decimal import Decimal, ROUND_HALF_DOWN

from home.models import Fantasia


class NomeField(forms.Field):

    def validate(self, value):
        """Checa se o value consiste em um valor não nulo."""

        # Valida se o nome eh vazio
        if not value:
            raise forms.ValidationError(
                u'Informe uma parte do nome para busca.'
            )

        return None


class TemaField(forms.Field):

    def validate(self, value):
        """Checa se o value consiste em um valor não nulo."""

        # Valida se o tema eh vazio
        if not value:
            raise forms.ValidationError(
                u'Informe uma parte da palavra do tema.'
            )

        return None


class TipoField(forms.ChoiceField):

    def validate(self, value):
        """Checa se o value consiste em um valor não nulo."""

        # Valida se o tipo eh vazio
        if not value:
            raise forms.ValidationError(
                u'Informe um tipo de fantasia para busca.'
            )

        return None


class FantasiaBuscarNomeForm(forms.Form):

    nome = NomeField(
        label=u'Nome da Fantasia',
        help_text=u'Informe pelo menos a parte de um nome para busca.\n'
            u'Isto é, informe pelo menos uma sílaba de um nome.',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Digite o Nome',
                'maxlength': '50',
            },
        ),
    )

    class Media:
        css = {
            'all': (
                'site/myscripts/fantasias_form.css',
                'site/jquery-chosen/chosen.min.css',
            )
        }
        js = (
            'site/myscripts/fantasias_form.js',
            'site/jquery-mask/jquery.mask.min.js',
            'site/jquery-chosen/chosen.jquery.min.js',
        )


class FantasiaBuscarTemaForm(forms.Form):

    tema = TemaField(
        label=u'Tema da Fantasia',
        help_text=u'Informe pelo menos uma parte (sílaba) da palavra do\n'
            u'tema de uma fantasia para busca.',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Digite o Tema',
                'maxlength': '50',
            },
        ),
    )

    class Media:
        css = {
            'all': (
                'site/myscripts/fantasias_form.css',
                'site/jquery-chosen/chosen.min.css',
            )
        }
        js = (
            'site/myscripts/fantasias_form.js',
            'site/jquery-mask/jquery.mask.min.js',
            'site/jquery-chosen/chosen.jquery.min.js',
        )


class FantasiaBuscarTipoForm(forms.Form):

    tipo = TipoField(
        label=u'Tipo da Fantasia',
        help_text=u'Escolha um tipo de Fantasia para busca.',
        choices=Fantasia.TIPOS_DE_FANTASIAS,
    )

    class Media:
        css = {
            'all': (
                'site/myscripts/fantasias_form.css',
                'site/jquery-chosen/chosen.min.css',
            )
        }
        js = (
            'site/myscripts/fantasias_form.js',
            'site/jquery-mask/jquery.mask.min.js',
            'site/jquery-chosen/chosen.jquery.min.js',
        )


class FantasiaCadastrarForm(forms.ModelForm):

    def clean(self):
        # chama o metodo clean da classe pai
        cleaned_data = super(FantasiaCadastrarForm, self).clean()
        nome = cleaned_data.get("nome")
        tipo = cleaned_data.get("tipo")
        tema = cleaned_data.get("tema")
        fantasia = Fantasia.objects.filter(
            nome=nome,
            tipo=tipo,
            tema=tema,
        )
        if fantasia:
            raise forms.ValidationError(
                u"Fantasia com este nome, tipo e tema "
                u"já existe cadastrada. Favor escolher outro conjunto de "
                u"nome, tipo e tema para a fantasia."
            )
        valor_fantasia = cleaned_data.get("valor_fantasia")
        valor_locacao = cleaned_data.get("valor_locacao")
        if valor_fantasia:
            max_valor_locacao = Decimal(0.10 * float(valor_fantasia)).quantize(
                Decimal('.01'), rounding=ROUND_HALF_DOWN
            )
            min_valor_locacao = Decimal(0.05 * float(valor_fantasia)).quantize(
                Decimal('.01'), rounding=ROUND_HALF_DOWN
            )
        else:
            max_valor_locacao = Decimal(30.00).quantize(
                Decimal('.01'), rounding=ROUND_HALF_DOWN
            )
            min_valor_locacao = Decimal(15.00).quantize(
                Decimal('.01'), rounding=ROUND_HALF_DOWN
            )
        if not valor_locacao:
            valor_locacao = Decimal(0.00).quantize(
                Decimal('.01'), rounding=ROUND_HALF_DOWN
            )
        if valor_locacao > max_valor_locacao:
            raise forms.ValidationError(u"Valor diário da locação deve ser no"
                u" máximo 10% do valor da fantasia. Favor ajustar"
                u" coretamente os valores da fantasia e/ou da locação."
            )
        if valor_locacao < min_valor_locacao:
            raise forms.ValidationError(u"Valor diário da locação deve ser no"
                u" mínimo 05% do valor da fantasia. Favor ajustar"
                u" coretamente os valores da fantasia e/ou da locação."
            )
        # Sempre retorne a coleção completa de cleaned_data.
        return cleaned_data

    valor_fantasia = forms.DecimalField(
        label=u'Valor da Fantasia',
        error_messages={
            'min_value':
                u'O valor mínimo de uma fantasia: R$ 300,00',
            'max_value':
                u'O valor máximo de uma fantasia: R$ 3.000,00',
        },
        help_text=u'O valor de uma fantasia deve ser no mínimo de R$ 300,00'
            u'\nE, no máximo, R$ 3.000,00',
        max_value=3000.00,
        min_value=300.00,
        widget=forms.TextInput(
            attrs={
                'placeholder': '0.000,00',
                'maxlength': '8',
            },
        ),
    )
    valor_locacao = forms.DecimalField(
        label=u'Valor da Locação',
        error_messages={
            'min_value':
                u'O valor mínimo de um dia de locação: R$ 15,00',
            'max_value':
                u'O valor máximo de um dia de locação: R$ 300,00',
        },
        help_text=u'O valor diário de uma locação deve ser no mínimo '
            u'05% do valor da fantasia.\n'
            u'E, no máximo, 10% do valor da fantasia.',
        max_value=300.00,
        min_value=15.00,
        widget=forms.TextInput(
            attrs={
                'placeholder': '000,00',
                'maxlength': '6',
            },
        ),
    )

    class Meta:
        model = Fantasia
        exclude = ('tem_locacao')
        widgets = {
            'nome': forms.TextInput(
                attrs={
                    'placeholder': 'Nome da fantasia',
                },
            ),
            'tema': forms.TextInput(
                attrs={
                    'placeholder': 'Tema da fantasia',
                },
            ),
        }

    class Media:
        css = {
            'all': (
                'site/myscripts/fantasias_form.css',
                'site/jquery-chosen/chosen.min.css',
            )
        }
        js = (
            'site/myscripts/fantasias_form.js',
            'site/jquery-mask/jquery.mask.min.js',
            'site/jquery-chosen/chosen.jquery.min.js',
        )


class FantasiaEditarForm(forms.ModelForm):

    def clean(self):
        # chama o metodo clean da classe pai
        cleaned_data = super(FantasiaEditarForm, self).clean()
        valor_fantasia = cleaned_data.get("valor_fantasia")
        valor_locacao = cleaned_data.get("valor_locacao")
        if valor_fantasia:
            max_valor_locacao = Decimal(0.10 * float(valor_fantasia)).quantize(
                Decimal('.01'), rounding=ROUND_HALF_DOWN
            )
            min_valor_locacao = Decimal(0.05 * float(valor_fantasia)).quantize(
                Decimal('.01'), rounding=ROUND_HALF_DOWN
            )
        else:
            max_valor_locacao = Decimal(30.00).quantize(
                Decimal('.01'), rounding=ROUND_HALF_DOWN
            )
            min_valor_locacao = Decimal(15.00).quantize(
                Decimal('.01'), rounding=ROUND_HALF_DOWN
            )
        if not valor_locacao:
            valor_locacao = Decimal(0.00).quantize(
                Decimal('.01'), rounding=ROUND_HALF_DOWN
            )
        if valor_locacao > max_valor_locacao:
            raise forms.ValidationError(u"Valor diário da locação deve ser no"
                u" máximo 10% do valor da fantasia. Favor ajustar"
                u" coretamente os valores da fantasia e/ou da locação."
            )
        if valor_locacao < min_valor_locacao:
            raise forms.ValidationError(u"Valor diário da locação deve ser no"
                u" mínimo 05% do valor da fantasia. Favor ajustar"
                u" coretamente os valores da fantasia e/ou da locação."
            )
        # Sempre retorne a coleção completa de cleaned_data.
        return cleaned_data

    valor_fantasia = forms.DecimalField(
        label=u'Valor da Fantasia',
        error_messages={
            'min_value':
                u'O valor mínimo de uma fantasia: R$ 300,00',
            'max_value':
                u'O valor máximo de uma fantasia: R$ 3.000,00',
        },
        help_text=u'O valor de uma fantasia deve ser no mínimo de R$ 300,00'
            u'\nE, no máximo, R$ 3.000,00',
        max_value=3000.00,
        min_value=300.00,
        widget=forms.TextInput(
            attrs={
                'placeholder': '0.000,00',
                'maxlength': '8',
            },
        ),
    )

    valor_locacao = forms.DecimalField(
        label=u'Valor da Locação',
        error_messages={
            'min_value':
                u'O valor mínimo de um dia de locação: R$ 15,00',
            'max_value':
                u'O valor máximo de um dia de locação: R$ 300,00',
        },
        help_text=u'O valor diário de uma locação deve ser no mínimo '
            u'05% do valor da fantasia.\n'
            u'E, no máximo, 10% do valor da fantasia.',
        max_value=300.00,
        min_value=15.00,
        widget=forms.TextInput(
            attrs={
                'placeholder': '000,00',
                'maxlength': '6',
            },
        ),
    )

    class Meta:
        model = Fantasia
        exclude = ('tem_locacao')
        widgets = {
            'nome': forms.TextInput(
                attrs={
                    'readonly': 'true',
                },
            ),
            'tipo': forms.TextInput(
                attrs={
                    'readonly': 'true',
                },
            ),
            'tema': forms.TextInput(
                attrs={
                    'readonly': 'true',
                },
            ),
        }

    class Media:
        css = {
            'all': (
                'site/myscripts/fantasias_form.css',
                'site/jquery-chosen/chosen.min.css',
            )
        }
        js = (
            'site/myscripts/fantasias_form.js',
            'site/jquery-mask/jquery.mask.min.js',
            'site/jquery-chosen/chosen.jquery.min.js',
        )


class FantasiaExcluirForm(forms.ModelForm):

    class Meta:
        model = Fantasia
        exclude = ('tem_locacao')
        widgets = {
            'nome': forms.TextInput(
                attrs={
                    'class': 'input_readonly',
                    'disabled': 'true',
                },
            ),
            'tipo': forms.TextInput(
                attrs={
                    'class': 'input_readonly',
                    'disabled': 'true',
                },
            ),
            'tema': forms.TextInput(
                attrs={
                    'class': 'input_readonly',
                    'disabled': 'true',
                },
            ),
            'valor_fantasia': forms.TextInput(
                attrs={
                    'class': 'input_readonly',
                    'disabled': 'true',
                    'maxlength': '8',
                },
            ),
            'valor_locacao': forms.TextInput(
                attrs={
                    'class': 'input_readonly',
                    'disabled': 'true',
                    'maxlength': '6',
                },
            ),
        }

    class Media:
        css = {
            'all': (
                'site/myscripts/fantasias_form.css',
                'site/jquery-chosen/chosen.min.css',
            )
        }
        js = (
            'site/myscripts/fantasias_form.js',
            'site/jquery-mask/jquery.mask.min.js',
            'site/jquery-chosen/chosen.jquery.min.js',
        )
