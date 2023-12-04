from django.shortcuts import render
from django.shortcuts import HttpResponse

def pagina_inicial(request):
    return HttpResponse('<h1>Pronto para investir</h1>')

def contato(request):
    return HttpResponse('<h1>Página de contato</h1>')

def minha_historia(request):
    pessoa = {
        'nome': 'Robert',
        'idade': 30,
        'profissao': 'Atendente'
    }
    return render(request,'investimentos/minha_historia.html', pessoa)