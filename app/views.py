from django.shortcuts import render, redirect
from .models import Pessoa

def home(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'index.html', {'pessoas': pessoas})

def cadastrar(request):
    _nome = request.POST.get('nome')
    Pessoa.objects.create(nome=_nome)
    pessoas = Pessoa.objects.all()
    return render(request, 'index.html', {'pessoas': pessoas})

def editar(request, id):
    pessoa = Pessoa.objects.get(id=id)
    return render(request, 'update.html', {'pessoa': pessoa})

def update(request, id):
    _nome = request.POST.get('nome')
    pessoa = Pessoa.objects.get(id=id)
    pessoa.nome = _nome
    pessoa.save()
    return redirect(home)