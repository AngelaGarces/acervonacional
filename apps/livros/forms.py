from django import forms
from django.forms import ModelForm

from apps.livros.models import Livros


class LivrosFormAdd(ModelForm):

    nome = forms.CharField(label='Nome:')

    class Meta:
        model = Livros
        fields = ['nome']