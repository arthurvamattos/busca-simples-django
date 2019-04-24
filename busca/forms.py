from django import forms

class FormPessoa(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)