from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Client, Car
import re
from django.core import serializers
import json


def clients(request):
    if request.method == 'GET':
        clients_list = Client.objects.all()
        return render(request, 'clients.html', {'clients': clients_list})
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        email = request.POST.get('email')
        cpf = request.POST.get('cpf')
        carros = request.POST.getlist('carro')
        placas = request.POST.getlist('placa')
        anos = request.POST.getlist('ano')

        cliente = Client.objects.filter(cpf=cpf)

        if cliente.exists:
            return render(request, 'clients.html', {'nome': nome, 'sobrenome': sobrenome, 'email': email, 'carros': zip(carros, placas, anos), })

        if not re.fullmatch(re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'), email):
            return render(request, 'clients.html', {'nome': nome, 'sobrenome': sobrenome, 'email': email, 'carros': zip(carros, placas, anos), })

        cliente = Client(
            nome=nome,
            sobrenome=sobrenome,
            email=email,
            cpf=cpf
        )
        cliente.save()

        for carro, placa, ano in zip(carros, placas, anos):
            car = Car(carro=carro, placa=placa, ano=ano, cliente=cliente)
            car.save()

        return render(request, 'clients.html')


def att_cliente(request):
    id_client = request.POST.get('id_cliente')
    client = Client.objects.filter(id=id_client)
    client_json = json.loads(serializers.serialize('json', client))[0]['fields']
    print(client_json)
    return JsonResponse(client_json)
