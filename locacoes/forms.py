# -*- coding: utf-8 -*-
from django import forms
#from django.forms.widgets import TextInput, Select, DateInput
from home.models import Locacao


class LocacaoCadastrarForm(forms.ModelForm):

    class Meta:
        model = Locacao

    class Media:
         css = {
             'all': ('site/locacoes/form.css',)
         }
         js = ('site/locacoes/form.js', 'site/jquery-mask/jquery.mask.min.js',)


class LocacaoEditarForm(forms.ModelForm):

    class Meta:
        model = Locacao

    class Media:
         css = {
             'all': ('site/locacoes/form.css',)
         }
         js = ('site/locacoes/form.js', 'site/jquery-mask/jquery.mask.min.js',)


class LocacaoExcluirForm(forms.ModelForm):

    class Meta:
        model = Locacao

    class Media:
         css = {
             'all': ('site/locacoes/form.css',)
         }
         js = ('site/locacoes/form.js', 'site/jquery-mask/jquery.mask.min.js',)


