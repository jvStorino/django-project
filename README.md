# Cadastro de Pessoas - Django CRUD

Este projeto é uma aplicação web construída com Django para realizar operações de CRUD (Create, Read, Update, Delete) em um banco de dados de pessoas. Além das operações CRUD, o sistema inclui **autenticação de usuários** com login, registro e recuperação de senha.

## 🚀 Funcionalidades

- **CRUD completo:** Cadastrar, visualizar, atualizar e excluir registros de pessoas.
- **Sistema de Login e Registro:** Acesso restrito para usuários autenticados.
- **Exibir lista de pessoas:** Mostrar nome e ID dos registros cadastrados.

---

## 🛠 Tecnologias Utilizadas

- **Python**
- **Django**
- **Banco de dados:** SQLite

---

## 📋 Pré-requisitos

Certifique-se de ter o Python instalado. 

1. **Crie e ative um ambiente virtual:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   .\venv\Scripts\activate  # Windows

2. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt

3. **Realize as migrações:**
   ```bash
   python manage.py migrate

4. **Crie um superusuário para acessar o admin:**
   ```bash
   python manage.py createsuperuser

5. **Inicie o servidor:**
   ```bash
   python manage.py runserver



