# -*- coding: utf-8 -*-
from django import forms
from decimal import Decimal, ROUND_HALF_DOWN

from locafan.lib.mascaras import mascara_valor
from home.models import Locacao, Fantasia, Cliente


class LocacaoCadastrarForm(forms.ModelForm):

    def clean(self):

        # chama o metodo clean da classe pai
        cleaned_data = super(LocacaoCadastrarForm, self).clean()

        # pega os valores dos campos
        pg_realizado = cleaned_data.get("pg_realizado")
        custo_total = cleaned_data.get("custo_total")
        pg_apagar = cleaned_data.get("pg_apagar")
        fantasias = cleaned_data.get("fantasias")
        ctot = Decimal(0.00)

        # calculo do custo total
        for fantasia in fantasias:
            if not fantasia.valor_locacao:
                raise forms.ValidationError(
                    u"O Valor de Locação não pode ser Nulo!"
                    u" Veja se você escolheu mesmo uma fantasia pelo menos!"
                )
            ctot = Decimal(
                Decimal(ctot) + Decimal(7.0) * Decimal(fantasia.valor_locacao)
            ).quantize(
                Decimal('.01'),
                rounding=ROUND_HALF_DOWN,
            )

        ctot = Decimal(ctot).quantize(
            Decimal('.01'),
            rounding=ROUND_HALF_DOWN,
        )

        if not custo_total:
            raise forms.ValidationError(
                u"O Custo total não pode ser Nulo!"
            )

        custo_total = Decimal(custo_total).quantize(
            Decimal('.01'),
            rounding=ROUND_HALF_DOWN,
        )

        if ctot != custo_total:
            raise forms.ValidationError(u"Custo total da locação deve ser "
                u"igual a: R$ %s, porém foi informado: R$ %s. Favor corrigir "
                u"o valor deste campo ou informar outras fantasias para "
                u"locação." % (
                    mascara_valor(ctot),
                    mascara_valor(custo_total),
                )
            )

        if not pg_realizado:
            raise forms.ValidationError(
                u"O Pagamento Antecipado não pode ser Nulo!"
            )

        pg_realizado = Decimal(pg_realizado).quantize(
            Decimal('.01'),
            rounding=ROUND_HALF_DOWN,
        )

        pg_minimo = Decimal(Decimal(ctot) * Decimal(0.5)).quantize(
            Decimal('.01'),
            rounding=ROUND_HALF_DOWN,
        )

        if pg_realizado < pg_minimo:
            raise forms.ValidationError(
                u"Para as fantasias escolhidas, o valor pago antecipado deve "
                u"ser, no mínimo: R$ %s. Mas, foi pago: %s."
                u"Favor corrigir o valor do pagamento, ou "
                u"escolher outras fantasias para locação." % (
                    mascara_valor(pg_minimo),
                    mascara_valor(pg_realizado),
                )
            )

        if not pg_apagar:
            raise forms.ValidationError(
                u"O Pagamento a Pagar não pode ser Nulo!"
            )

        pg_apagar = Decimal(pg_apagar).quantize(
            Decimal('.01'),
            rounding=ROUND_HALF_DOWN,
        )

        if pg_apagar != (ctot - pg_realizado):
            raise forms.ValidationError(
                u"Para os dados informados, o valor a pagar "
                u"de ser de: R$ %s. Mas, foi informado: %s."
                u"Favor corrigir o valor a pagar, ou "
                u"escolher outras fantasias para locação." % (
                    mascara_valor(ctot - pg_realizado),
                    mascara_valor(pg_apagar),
                ),
            )

        # Sempre retorne a coleção completa de cleaned_data.
        return cleaned_data

    dt_locacao = forms.DateField(
        label=u'Data da Locação',
        help_text=u'Este campo eh preenchido automaticamente\n'
            u'com a data de hoje.',
        widget=forms.DateInput(
            attrs={
                'placeholder': 'dd/mm/aaaa',
                'maxlength': '10',
                'readonly': 'true',
            },
        ),
    )

    dt_devolucao = forms.DateField(
        label=u'Data da Devolução',
        help_text=u'Este campo é preenchido automaticamente para\n'
            u'uma semana após a data de locação.',
        widget=forms.DateInput(
            attrs={
                'placeholder': 'dd/mm/aaaa',
                'maxlength': '10',
                'readonly': 'true',
            },
        ),
    )

    pg_realizado = forms.DecimalField(
        label=u'Pagamento Antecipado',
        error_messages={
            'min_value':
                u'O valor mínimo antecipado: 50% do custo total!',
            'max_value':
                u'O valor máximo antecipado: 100% do custo total!',
        },
        help_text=u'O pagamento mínimo antecipado de uma locação\n'
            u'Deve ser de no mínimo 50% do custo total da locação.',
        max_value=999999.99,
        min_value=52.50,
        widget=forms.TextInput(
            attrs={
                'placeholder': '000.000,00',
                'maxlength': '10',
            },
        ),
    )

    pg_apagar = forms.DecimalField(
        label=u'Pagamento a Pagar',
        error_messages={
            'min_value':
                u'O valor mínimo a pagar: R$ 0,00 !',
        },
        help_text=u'Este campo é preenchido automaticamente, '
            u'caso isso não ocorra,'
            u' favor preenchê-lo manualmente.',
        max_value=999999.99,
        min_value=0.00,
        widget=forms.TextInput(
            attrs={
                'placeholder': '000.000,00',
                'maxlength': '10',
            },
        ),
    )

    custo_total = forms.DecimalField(
        label=u'Custo Total da Locação',
        error_messages={
            'min_value':
                u'O custo total mínimo de uma locação: R$ 105,00!',
        },
        help_text=u'Este campo é preenchido automaticamente, '
            u'caso isso não ocorra,'
            u' favor preenchê-lo manualmente.',
        max_value=999999.99,
        min_value=105.00,
        widget=forms.TextInput(
            attrs={
                'placeholder': '000.000,00',
                'maxlength': '10',
            },
        ),
    )

    cliente = forms.ModelChoiceField(
        label=u'Cliente',
        help_text=u'Escolha um Cliente na Lista ao lado.',
        empty_label='',
        queryset=Cliente.objects.filter(
            tem_locacao=False,
            multa=0.0,
        ),
    )

    fantasias = forms.ModelMultipleChoiceField(
        label=u'Fantasias',
        required=True,
        help_text=u'Mantenha pressionado "Control" '
            u'(ou "Command" no Mac) para selecionar mais de uma fantasia.',
        queryset=Fantasia.objects.all(),
    )

    class Meta:

        model = Locacao
        exclude = ('status')

    class Media:
        css = {
            'all': (
                'site/myscripts/locacoes_form.css',
                 'site/jquery-chosen/chosen.min.css',
            )
        }
        js = (
            'site/myscripts/locacoes_form.js',
            'site/jquery-mask/jquery.mask.min.js',
             'site/jquery-chosen/chosen.jquery.min.js',
        )


class LocacaoEditarForm(forms.ModelForm):

    pg_realizado = forms.DecimalField(
        label=u'Pagamento Realizado',
        required=False,
        widget=forms.TextInput(
            attrs={
                'placeholder': '000.000,00',
                'maxlength': '10',
                'disabled': 'true',
                'class': 'input_readonly',
            },
        ),
    )
    pg_apagar = forms.DecimalField(
        label=u'Pagamento a Pagar',
        required=True,
        help_text=u'Este campo é preenchido automaticamente, '
            u'caso isso não ocorra,'
            u' favor preenchê-lo manualmente.',
        max_value=999999.99,
        min_value=0.00,
        widget=forms.TextInput(
            attrs={
                'placeholder': '000.000,00',
                'maxlength': '10',
            },
        ),
    )

    custo_total = forms.DecimalField(
        label=u'Custo Total da Locação',
        required=False,
        widget=forms.TextInput(
            attrs={
                'placeholder': '000.000,00',
                'maxlength': '10',
                'disabled': 'true',
                'class': 'input_readonly',
            },
        ),
    )

    class Meta:

        model = Locacao
        exclude = ('status', 'dt_devolucao', 'dt_locacao', 'cliente',
            'fantasias')

    class Media:

        css = {
            'all': (
                'site/myscripts/locacoes_form.css',
                 'site/jquery-chosen/chosen.min.css',
            )
        }
        js = (
            'site/myscripts/locacoes_form.js',
            'site/jquery-mask/jquery.mask.min.js',
             'site/jquery-chosen/chosen.jquery.min.js',
        )


class LocacaoExcluirForm(forms.ModelForm):

    class Meta:

        model = Locacao
        exclude = ('status')
        widgets = {
            'dt_locacao': forms.TextInput(
                attrs={
                    'disabled': 'true',
                    'class': 'input_readonly',
                },
            ),
            'dt_devolucao': forms.TextInput(
                attrs={
                    'disabled': 'true',
                    'class': 'input_readonly',
                },
            ),
            'pg_realizado': forms.TextInput(
                attrs={
                    'disabled': 'true',
                    'class': 'input_readonly',
                },
            ),
            'pg_apagar': forms.TextInput(
                attrs={
                    'disabled': 'true',
                    'class': 'input_readonly',
                },
            ),
            'custo_total': forms.TextInput(
                attrs={
                    'disabled': 'true',
                    'class': 'input_readonly',
                },
            ),
            'cliente': forms.Select(
                attrs={
                    'disabled': 'true',
                    'class': 'input_readonly',
                },
            ),
            'fantasias': forms.Select(
                attrs={
                    'disabled': 'true',
                    'class': 'input_readonly',
                },
            ),
        }

    class Media:

        css = {
            'all': (
                'site/myscripts/locacoes_form.css',
                 'site/jquery-chosen/chosen.min.css',
            )
        }
        js = (
            'site/myscripts/locacoes_form.js',
            'site/jquery-mask/jquery.mask.min.js',
             'site/jquery-chosen/chosen.jquery.min.js',
        )
