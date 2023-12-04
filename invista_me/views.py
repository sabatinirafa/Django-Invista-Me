from django.shortcuts import render
from django.shortcuts import HttpResponse

def pagina_inicial(request):
    return HttpResponse('<h1>Pronto para investir</h1>')


def novo_investimento(request):
    return render(request, 'investimentos/novo_investimento.html')

def investimento_registrado(request):
    investimento = {
        'tipo_investimento': request.POST.get('tipo_investimento')
    }
    return render(request, 'investimentos/investimento_registrado.html', investimento)