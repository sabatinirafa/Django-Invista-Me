from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Investimento

def novo_investimento(request):
    return render(request, 'investimentos/novo_investimento.html')


def investimentos(request):
    dados = {
        'dados': Investimento.objects.all()
    }
    return render(request, 'investimentos/investimentos.html', context=dados)

def detalhe(request, id_investimento):
    dados = {
        'dados': Investimento.objects.get(pk=id_investimento)
    }
    return render(request, 'investimentos/detalhe.html', dados)