from farmacia.models import Parametros
from django.views.generic import View
import json
from django.http import HttpResponse


class VerDestinos(View):

    def is_ajax(self, request):
         
        return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

    def get(self, request):

        parametros = Parametros()
        
        if self.is_ajax( request = request ):
            
            palabra = request.GET.get('term', '')
            
            destinos = parametros.nodos.filter(nombre__icontains = palabra )

            otros_destinos = parametros.destinos.filter(nombre__icontains = palabra )
            
            results = []
            
            for destino in destinos:
                    
                data = {}
                
                data['label'] = destino.nombre
                    
                results.append(data)
            
            for destino in otros_destinos:
                    
                data = {}
                
                data['label'] = destino.nombre
                    
                results.append(data)
            
            data_json = json.dumps(results)

        else:
            data_json = "fallo"
        
        mimetype = "application/json"
        
        return HttpResponse(data_json, mimetype)

class VerEnviosPorDestinos(View):

    def is_ajax(self, request):
         
        return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

    def get(self, request):

        parametros = Parametros()
        
        if self.is_ajax( request = request ):
            
            valor = request.GET['valor']

            results = []

            parametros.obtener_nodos(request)

            for nodo in parametros.params['nodos_perfil']:

                try:

                    destino= parametros.nodos.get(nombre = valor)
                
                    envios = parametros.envio.filter(destino = destino ).filter(origen = nodo )

                except:

                    destino = parametros.destinos.get(nombre = valor)

                    envios = parametros.envio.filter( otro_destino = destino ).filter(origen = nodo )

                for envio in envios:
                        
                    data = {}
                    
                    data['id'] = envio.id

                    data['origen'] = envio.origen.nombre

                    try:

                        data['destino'] = envio.destino.nombre
                    
                    except:

                        data['destino'] = "---"

                    try:

                        data['otro_destino'] = envio.otro_destino.nombre
                    
                    except:

                        data['otro_destino'] = "---"
                        
                    data['fecha'] = str(envio.fecha)  
                    
                    data['hora'] = str(envio.hora) 
                    
                    data['estado'] = envio.estado.nombre    
                    
                    results.append(data)

            data_json = json.dumps(results)

        else:
            data_json = "fallo"
        
        mimetype = "application/json"
        
        return HttpResponse(data_json, mimetype)
    
class VerEnviosPorFecha(View):

    def is_ajax(self, request):
         
        return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

    def get(self, request):

        parametros = Parametros()
        
        if self.is_ajax( request = request ):
            
            desde = request.GET['desde']

            hasta = request.GET['hasta']

            results = []

            parametros.obtener_nodos(request)

            for nodo in parametros.params['nodos_perfil']:
       
                envios = parametros.envio.filter( origen= nodo).filter(fecha__range=[desde, hasta])

                for envio in envios:
                        
                    data = {}
                    
                    data['id'] = envio.id

                    data['origen'] = envio.origen.nombre

                    try:

                        data['destino'] = envio.destino.nombre
                    
                    except:

                        data['destino'] = "---"

                    try:

                        data['otro_destino'] = envio.otro_destino.nombre
                    
                    except:

                        data['otro_destino'] = "---"
                        
                    data['fecha'] = str(envio.fecha)  
                    
                    data['hora'] = str(envio.hora) 
                    
                    data['estado'] = envio.estado.nombre    
                    
                    results.append(data)

            data_json = json.dumps(results)

        else:
            data_json = "fallo"
        
        mimetype = "application/json"
        
        return HttpResponse(data_json, mimetype)
    
class VerImpresones(View):

    def __init__(self,):
        
        self.parametros = Parametros()
    
    def is_ajax(self, request):
         
        return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

    def get(self, request):

        results= []
        
        if self.is_ajax( request = request ):
            
            lista = request.GET['lista']

            lista = json.loads(lista)

            for valor in lista:

                data ={}

                valor = int(valor[4:])

                envio = self.parametros.envio.get( id = valor )  
                
                data['id'] = envio.id

                data['origen'] = envio.origen.nombre

                try:

                    data['destino'] = envio.destino.nombre
                
                except:

                    data['destino'] = envio.otro_destino.nombre

                        
                data['fecha'] = str(envio.fecha)  
                
                data['hora'] = str(envio.hora) 
                
                data['estado'] = envio.estado.nombre                   
                
                data['usuario'] = envio.usuario.username
                
                results.append(data)

            data_json = json.dumps(results)

        else:
            data_json = "fallo"
        
        mimetype = "application/json"
        
        return HttpResponse(data_json, mimetype)
    
