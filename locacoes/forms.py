# -*- coding: utf-8 -*-
from django import forms
#from django.forms.widgets import TextInput, Select, DateInput
from home.models import Locacao


class LocacaoCadastrarForm(forms.ModelForm):

    class Meta:
        model = Locacao

    class Media:
        css = {
            'all': (
                'site/myscripts/locacoes_form.css',
            )
        }
        js = (
            'site/myscripts/locacoes_form.js',
            'site/jquery-mask/jquery.mask.min.js',
        )


class LocacaoEditarForm(LocacaoCadastrarForm):

    class Media(LocacaoCadastrarForm.Media):
        pass


class LocacaoExcluirForm(LocacaoCadastrarForm):

    class Media(LocacaoCadastrarForm.Media):
        pass
