from link.models import Links 
from perfiles.models import Perfil
from hojaderuta.models import Envio
from estados.models import Estado
from nodos.models import Nodo
from nodos.models import Destino

class Parametros():
    """
    Clase para obterner los objetos mas utilzados por el usuario
    """

    def __init__(self,):

        self.params = {}

        self.link = Links.objects

        self.envio = Envio.objects

        self.estado = Estado.objects

        self.perfil = Perfil.objects

        self.nodos = Nodo.objects

        self.destinos = Destino.objects

        self.activo = self.estado.get(nombre = 'ACTIVO')

        self.preparado = self.estado.get(nombre = 'PREPARADO')

        self.en_camino = self.estado.get(nombre = 'EN CAMINO')

        self.entregado = self.estado.get(nombre = 'ENTREGADO')

        self.ignorado = self.estado.get(nombre = 'IGNORADO')

    def obtener_links(self,):

        self.params['links'] = self.link.filter(estado = self.activo)

    def obtener_nodos(self, request):

        self.params['perfil'] = self.perfil.filter( usuario= request.user)

    def obtener_nodos_destinos(self, nodo):

        self.params['nodos'] = nodo.filter( estado = self.activo)
