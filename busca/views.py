from django.shortcuts import render
from .models import Pessoa
from .forms import FormPessoa

def index(request):
    context = {}
    pessoas = Pessoa.objects.all()
    context['form'] = FormPessoa()
    busca =  request.GET.get('nome')
    if busca is not None:
        pessoas = pessoas.filter(nome__name__icontains=busca)
    context['pessoas'] = pessoas
    return render(request, 'index.html', context)

def pesquisa(request,busca):
    context = {}
    pessoas = Pessoa.objects.all()
    context['form'] = FormPessoa()
    busca =  request.GET.get('nome')
    if busca is not None:
        pessoas = pessoas.filter(nome__icontains=busca)
    context['pessoas'] = pessoas
    return render(request, 'index.html', context)