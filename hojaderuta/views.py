from django.shortcuts import render
from link.models import Links 
from perfiles.models import Perfil
from hojaderuta.models import Envio
from estados.models import Estado

# Create your views here.

activo = Estado.objects.get(nombre = 'ACTIVO')

preparado = Estado.objects.get(nombre = 'PREPARADO')

en_camino = Estado.objects.get(nombre = 'EN CAMINO')

entregado = Estado.objects.get(nombre = 'ENTREGADO')

params= {}

params['links'] = Links.objects.filter(estado = activo)

def index(request):
    """
    Retorna diccionario. Con los nodos asociados al perfil, la cuenta de los pedidos creados 
    desde los nodos habilitados para el usuario, y la cuenta de los pedidos que recibiran lon nodos
    asociados al usuario
    """
    mis_envios_p = 0

    mis_envios_c = 0

    a_recibir_p = 0

    a_recibir_c = 0

    if request.user.is_authenticated:

        params['nodos'] = Perfil.objects.filter( usuario= request.user)

        for nodo in params['nodos']:
            
            mis_envios_p+= Envio.objects.filter(origen= nodo.nodo.id).filter(estado= preparado).count()

            mis_envios_c+= Envio.objects.filter(estado= en_camino).filter(origen= nodo.nodo.id).count()
            
            a_recibir_p+= Envio.objects.filter(estado= preparado).filter(destino= nodo.nodo.id).count()

            a_recibir_c+= Envio.objects.filter(estado= en_camino).filter(destino= nodo.nodo.id).count()

        params['mis_envios'] = mis_envios_p + mis_envios_c

        params['a_recibir'] = a_recibir_c + a_recibir_p

    return render(request, 'hojaderuta/index.html', params )

def mis_envios(request):

    params['preparados'] = []

    params['en_camino'] = []

    if request.user.is_authenticated:

        params['nodos'] = Perfil.objects.filter( usuario= request.user)

        for nodo in params['nodos']:
            
            params['preparados'].append(Envio.objects.filter(origen = nodo.nodo.id).filter(estado = preparado).exclude( origen = None ))

            params['en_camino'].append(Envio.objects.filter(estado = en_camino).filter(origen = nodo.nodo.id).exclude( origen = None ))       

    return render(request, 'hojaderuta/mis_envios.html', params )

def para_recibir(request):

    params['preparados'] = []

    params['en_camino'] = []

    if request.user.is_authenticated:

        params['nodos'] = Perfil.objects.filter( usuario= request.user)

        for nodo in params['nodos']:
            
            params['preparados'].append(Envio.objects.filter(destino= nodo.nodo.id).filter(estado = preparado).exclude( origen = None ))

            params['en_camino'].append(Envio.objects.filter(estado= en_camino).filter(destino = nodo.nodo.id).exclude( origen = None ))       

    return render(request, 'hojaderuta/para_recibir.html', params )

def otros_destinos(request):

    params['otros_destinos'] = []

    if request.user.is_authenticated:

        params['nodos'] = Perfil.objects.filter( usuario= request.user)

        for nodo in params['nodos']:
            
            params['otros_destinos'].append(Envio.objects.filter(origen = nodo.nodo.id).filter( destino = None ).exclude( estado = entregado ))   

    return render(request, 'hojaderuta/otros_destinos.html', params )
