from django.db import models


class Client(models.Model):
    nome = models.CharField(max_length=64)
    sobrenome = models.CharField(max_length=64)
    email = models.EmailField(max_length=64)
    cpf = models.CharField(max_length=14)

    def __str__(self):
        return self.nome


class Car(models.Model):
    carro = models.CharField(max_length=256)
    placa = models.CharField(max_length=7)
    ano = models.IntegerField()
    cliente = models.ForeignKey(Client, on_delete=models.CASCADE)
    lavagens = models.IntegerField(default=0)
    consertos = models.IntegerField(default=0)

    def __str__(self):
        return self.carro
