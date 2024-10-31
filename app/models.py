from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=20)
    numero = models.IntegerField(default=00000000000)
    endereco = models.CharField(max_length=100, default='')
    cpf = models.CharField(max_length=11, default='00000000000')

    def __str__(self):
        return self.nome
