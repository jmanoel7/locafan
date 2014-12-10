# -*- coding: utf-8 -*-
from django import forms
from home.models import Fantasia


class FantasiaCadastrarForm(forms.ModelForm):

    class Meta:
        model = Fantasia
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
            'valor_fantasia': forms.TextInput(
                attrs={
                    'placeholder': '000.000,00',
                    'maxlength': '10',
                },
            ),
            'valor_locacao': forms.TextInput(
                attrs={
                    'placeholder': '000.000,00',
                    'maxlength': '10',
                },
            ),
            'qtde_total': forms.TextInput(
                attrs={
                    'placeholder': '00',
                    'maxlength': '2',
                },
            ),
            'qtde_disponivel': forms.TextInput(
                attrs={
                    'placeholder': '00',
                    'maxlength': '2',
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


class FantasiaEditarForm(FantasiaCadastrarForm):

    class Meta(FantasiaCadastrarForm.Meta):
        pass


class FantasiaExcluirForm(FantasiaCadastrarForm):

    class Meta(FantasiaCadastrarForm.Meta):
        widgets = {
            'nome': forms.TextInput(
                attrs={
                    'class': 'input_readonly',
                    'disabled': 'true',
                },
            ),
            'tipo': forms.Select(
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
                    'maxlength': '10',
                },
            ),
            'valor_locacao': forms.TextInput(
                attrs={
                    'class': 'input_readonly',
                    'disabled': 'true',
                    'maxlength': '10',
                },
            ),
            'qtde_total': forms.TextInput(
                attrs={
                    'class': 'input_readonly',
                    'disabled': 'true',
                    'maxlength': '2',
                },
            ),
            'qtde_disponivel': forms.TextInput(
                attrs={
                    'class': 'input_readonly',
                    'disabled': 'true',
                    'maxlength': '2',
                },
            ),
        }
