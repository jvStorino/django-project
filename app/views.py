from django.shortcuts import render
from .models import Pessoa

def home(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'index.html', {'pessoas': pessoas})

def cadastrar(request):
    _nome = request.POST.get('nome')
    Pessoa.objects.create(nome=_nome)
    pessoas = Pessoa.objects.all()
    return render(request, 'index.html', {'pessoas': pessoas})
