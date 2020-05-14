from django.shortcuts import render, HttpResponse


# Create your views here.

def hello(request,nome):
    return HttpResponse('Hello {}'.format(nome)) # Não aceito format string f'{variavel}', Format aceito .formart(variavel)


