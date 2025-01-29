from django.shortcuts import render
from django.shortcuts import redirect
from django.http import Http404
from farmacia.models import Parametros
from hojaderuta.models import Envio
from hojaderuta.forms import EnvioForm, EnvioOtroDestinoForm


class Usuario(Parametros):    
    
    def index(self, request):
        """
        Retorna diccionario. Con los nodos asociados al perfil, la cuenta de los pedidos creados 
        desde los nodos habilitados para el usuario, y la cuenta de los pedidos que recibiran lon nodos
        asociados al usuario
        """
        mis_envios = 0

        a_recibir = 0

        if request.user.is_authenticated:

            self.obtener_nodos(request)

            for nodo in self.params['perfil']:
                
                mis_envios+= self.envio.filter(origen= nodo.nodo.id).filter(estado= self.preparado).count() + self.envio.filter(estado= self.en_camino).filter(origen= nodo.nodo.id).count()
                  
                a_recibir+= self.envio.filter(estado= self.preparado).filter(destino= nodo.nodo.id).count() + self.envio.filter(estado= self.en_camino).filter(destino= nodo.nodo.id).count()

            self.params['mis_envios'] = mis_envios

            self.params['a_recibir'] = a_recibir

        return render(request, 'hojaderuta/index.html', self.params )

    def mis_envios(self, request):

        self.params['preparados'] = []

        self.params['en_camino'] = []

        if request.method == "POST":       
        
            form = EnvioForm(request.POST)  

            if form.is_valid():

                origen = form.cleaned_data['origen']

                destino = form.cleaned_data['destino']

                descripcion = form.cleaned_data['descripcion']

                nuevo_envio = Envio( origen = origen, destino = destino, descripcion = descripcion, usuario = request.user, estado = self.preparado )
                
                nuevo_envio.save()
                
                return redirect('mis_envios')   

        if request.user.is_authenticated:

            self.obtener_nodos(request)

            self.obtener_nodos_destinos(self.nodos)

            self.params['form'] = EnvioForm()

            for nodo in self.params['perfil']:
                
                self.params['preparados'].append(self.envio.filter(origen = nodo.nodo.id).filter(estado = self.preparado).exclude( origen = None ).exclude( destino = None ))

                self.params['en_camino'].append(self.envio.filter(estado = self.en_camino).filter(origen = nodo.nodo.id).exclude( origen = None ).exclude( destino = None ))       

        return render(request, 'hojaderuta/envios.html', self.params )

    def para_recibir(self, request):

        self.params['preparados'] = []

        self.params['en_camino'] = []

        if request.user.is_authenticated:

            self.obtener_nodos(request)

            for nodo in self.params['perfil']:
                
                self.params['preparados'].append(self.envio.filter( destino = nodo.nodo.id ).filter( estado = self.preparado ).exclude( origen = None ))

                self.params['en_camino'].append(self.envio.filter(estado= self.en_camino).filter(destino = nodo.nodo.id).exclude( origen = None ))       

        return render(request, 'hojaderuta/para_recibir.html', self.params )

    def otros_destinos(self, request):

        self.params['preparados'] = []

        self.params['en_camino'] = []

        if request.user.is_authenticated:

            if request.method == "POST":       
        
                form = EnvioOtroDestinoForm(request.POST)  

                if form.is_valid():

                    origen = form.cleaned_data['origen']

                    otro_destino = form.cleaned_data['otro_destino']

                    descripcion = form.cleaned_data['descripcion']

                    nuevo_envio = Envio( origen = origen, otro_destino = otro_destino, descripcion = descripcion, usuario = request.user, estado = self.preparado )
                    
                    nuevo_envio.save()
                    
                    return redirect('otros_destinos')  

            self.obtener_nodos(request)

            self.obtener_nodos_destinos(self.destinos)

            for nodo in self.params['perfil']:
                
                self.params['preparados'].append(self.envio.filter(origen = nodo.nodo.id).filter( destino = None ).exclude( estado = self.entregado ))   

        return render(request, 'hojaderuta/otros_destinos.html', self.params )

    def ver_envio(self, request, envio_id): 

        try:
            self.obtener_nodos(request)

            envio = self.envio.get(id = envio_id)
            
            if request.method == "POST":

                estado = request.POST.get("estado")

                envio.estado = self.estado.get( id= estado )

                envio.save()

            self.params['envio'] = envio

            return render( request, 'hojaderuta/detalle_envio.html', self.params )

        except:

            raise Http404

usuario = Usuario() 

