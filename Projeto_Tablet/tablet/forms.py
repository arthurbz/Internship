from django import forms
from .models import Pessoa


class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = ['nome', 'sobrenome', 'matricula', 'cpf', 'senha', 'email']


class SenhaForm(forms.Form):
    senha = forms.CharField(max_length=20, widget=forms.PasswordInput())
    confirmacao_senha = forms.CharField(max_length=20, widget=forms.PasswordInput())
