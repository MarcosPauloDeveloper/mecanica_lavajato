from django.db import models


class Client(models.Model):
    nome = models.CharField(max_length=64, null=False)
    sobrenome = models.CharField(max_length=64, null=False)
    email = models.EmailField(max_length=64, unique=True, null=False)
    cpf = models.CharField(max_length=14, unique=True, null=False, db_index=True)

    def __str__(self):
        return self.nome


class Car(models.Model):
    carro = models.CharField(max_length=256, null=False)
    placa = models.CharField(max_length=8, unique=True)
    ano = models.IntegerField()
    cliente = models.ForeignKey(Client, on_delete=models.CASCADE)
    lavagens = models.IntegerField(default=0)
    consertos = models.IntegerField(default=0)

    def __str__(self):
        return self.carro
