from django.shortcuts import render
from link.models import Links 
from estados.models import Estado
from nodos.models import Nodo
from nodos.models import Destino

# Create your views here.

activo = Estado.objects.get(nombre = 'ACTIVO')

params= {}

params['links'] = Links.objects.filter(estado = activo)
# Create your views here.

def ver_nodos(request):

    if request.user.is_authenticated:

        params['nodos'] = Nodo.objects.filter( estado = activo)

    return render(request, 'nodos/nodos.html', params )

def ver_destinos(request):

    if request.user.is_authenticated:

        params['destinos'] = Destino.objects.filter( estado = activo)

    return render(request, 'nodos/destinos.html', params )