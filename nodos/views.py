from django.shortcuts import render
from link.models import Links 
from estados.models import Estado
from nodos.models import Nodo

# Create your views here.

activo = Estado.objects.get(nombre = 'ACTIVO')

params= {}

params['links'] = Links.objects.filter(estado = activo)
# Create your views here.

def ver_nodos(request):

    if request.user.is_authenticated:

        params['nodos'] = Nodo.objects.filter( estado = activo)

    return render(request, 'nodos/nodos.html', params )