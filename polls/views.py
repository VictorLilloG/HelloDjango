from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Aqui se encuentran los ejercicios de Django. /hello para Hello World, /pages para las paginas y /board para el Message Board.")
def hello(request):
    return HttpResponse("Hello World.")