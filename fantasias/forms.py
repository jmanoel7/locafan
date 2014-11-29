# -*- coding: utf-8 -*-
from django import forms
#from django.forms.widgets import TextInput, Select, DateInput
from home.models import Fantasia


class FantasiaCadastrarForm(forms.ModelForm):

    class Meta:
        model = Fantasia

    class Media:
         css = {
             'all': ('site/fantasias/form.css',)
         }
         js = ('site/fantasias/form.js', 'site/jquery-mask/jquery.mask.min.js',)


class FantasiaEditarForm(forms.ModelForm):

    class Meta:
        model = Fantasia

    class Media:
         css = {
             'all': ('site/fantasias/form.css',)
         }
         js = ('site/fantasias/form.js', 'site/jquery-mask/jquery.mask.min.js',)


class FantasiaExcluirForm(forms.ModelForm):

    class Meta:
        model = Fantasia

    class Media:
         css = {
             'all': ('site/fantasias/form.css',)
         }
         js = ('site/fantasias/form.js', 'site/jquery-mask/jquery.mask.min.js',)


