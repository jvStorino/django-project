from django.shortcuts import render, redirect
from .models import Pessoa

def home(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'index.html', {'pessoas': pessoas})

def cadastrar(request):
    _nome = request.POST.get('nome')
    _numero = request.POST.get('numero')
    _cpf = request.POST.get('cpf')
    _endereco = request.POST.get('endereco')
        
    # Cria um único objeto Pessoa com todos os campos
    Pessoa.objects.create(
        nome=_nome,
        numero=_numero,
        cpf=_cpf,
        endereco=_endereco
    )

    # Caso não seja POST, renderiza a página de cadastro
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

def delete(request, id):
    pessoa = Pessoa.objects.get(id=id)
    pessoa.delete()
    return redirect(home)

def buscar_pessoa(request):
    pessoas = []  # Lista que vai armazenar os resultados
    nome = ''     # Variável para armazenar o nome buscado

    if request.method == 'GET':
        nome = request.GET.get('nome')  # Obtém o nome enviado pelo formulário
        if nome:  # Se um nome foi fornecido
            pessoas = Pessoa.objects.filter(nome__icontains=nome)  # Busca pessoas com o nome

    return render(request, 'buscar_pessoa.html', {'pessoas': pessoas, 'nome': nome})

