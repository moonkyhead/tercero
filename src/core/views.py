from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def saludar(request):
	return HttpResponse("Funciona por el amor de deussssss")

def saludar_con_etiqueta(request):
    return HttpResponse("<h1> La DJango ta toda rota </h1>")

def saludar_con_parametros(request, nombre: str, apellido: str):
    nombre = nombre.capitalize()
    apellido = apellido.capitalize()
    return HttpResponse(f"{apellido}, {nombre}")