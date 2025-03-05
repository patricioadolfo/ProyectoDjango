from django.shortcuts import render
from django.shortcuts import redirect
from django.http import Http404
from farmacia.models import Parametros
from hojaderuta.models import Envio
from hojaderuta.forms import EnvioForm, EnvioOtroDestinoForm, BuscarDestino, FormFechas

class Usuario(Parametros):    

    def index(self, request):
        """
        Retorna diccionario. Con los nodos asociados al perfil, la cuenta de los pedidos creados 
        desde los nodos habilitados para el usuario, y la cuenta de los pedidos que recibiran con nodos
        asociados al usuario.
        """
        mis_envios = 0

        a_recibir = 0

        otros_destinos = 0

        self.params['preparados'] = []

        self.params['en_camino'] = []

        self.params['recibir_preparados'] = []

        self.params['recibir_en_camino'] = []

        self.params['otro_destino'] = []

        if request.user.is_authenticated:

            self.obtener_nodos(request)

            for nodo in self.params['nodos_perfil']:
                
                mis_envios+= self.envio.filter( origen = nodo.id ).filter( estado = self.preparado ).count() + self.envio.filter( estado = self.en_camino ).filter( origen = nodo.id ).count()
                  
                a_recibir+= self.envio.filter( estado = self.preparado ).filter( destino = nodo.id ).count() + self.envio.filter( estado = self.en_camino ).filter( destino = nodo.id ).count()

                otros_destinos+= self.envio.filter( origen = nodo.id ).filter( destino = None ).exclude( estado = self.entregado ).exclude( estado = self.ignorado ).count() 

                self.params['preparados'].append( self.envio.filter( origen = nodo.id ).filter( estado = self.preparado ).exclude( origen = None ).exclude( destino = None ))

                self.params['en_camino'].append( self.envio.filter( estado = self.en_camino ).filter( origen = nodo.id ).exclude( origen = None ).exclude( destino = None ))       

                self.params['recibir_preparados'].append( self.envio.filter( destino = nodo.id ).filter( estado = self.preparado ).exclude( origen = None ))

                self.params['recibir_en_camino'].append( self.envio.filter( estado = self.en_camino ).filter( destino = nodo.id ).exclude( origen = None ))       

                self.params['otro_destino'].append( self.envio.filter( origen = nodo.id ).filter( destino = None ).exclude( estado = self.entregado ).exclude( estado = self.ignorado ))   

            self.params['mis_envios'] = mis_envios

            self.params['a_recibir'] = a_recibir

            self.params['otros_destinos'] = otros_destinos

        return render(request, 'hojaderuta/index.html', self.params )

    def nuevo_envio(self, request,):

        if request.method == "POST":       
        
            form = EnvioForm(request.POST)  

            if form.is_valid():

                origen = form.cleaned_data['origen']

                destino = form.cleaned_data['destino']

                descripcion = form.cleaned_data['descripcion']

                nuevo_envio = Envio( origen = origen, destino = destino, descripcion = descripcion, usuario = request.user, estado = self.preparado )
                
                nuevo_envio.save()
                
                return redirect('index')
        
        self.obtener_nodos(request)

        self.obtener_nodos_destinos(self.nodos)

        self.params['form'] = EnvioForm()

        return render(request, 'hojaderuta/form_nuevo_envio.html', self.params )

    def envio_otro_destino(self, request,):

        if request.method == "POST":       
        
            form = EnvioOtroDestinoForm(request.POST)  

            if form.is_valid():

                origen = form.cleaned_data['origen']

                otro_destino = form.cleaned_data['otro_destino']

                descripcion = form.cleaned_data['descripcion']

                nuevo_envio = Envio( origen = origen, otro_destino = otro_destino, descripcion = descripcion, usuario = request.user, estado = self.preparado )
                
                nuevo_envio.save()
                
                return redirect('index')
        
        self.obtener_nodos(request)

        self.obtener_nodos_destinos(self.destinos)

        self.params['form'] = EnvioForm()

        return render(request, 'hojaderuta/form_nuevo_envio_otrodestino.html', self.params )    

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
  
    def todos_los_envios(self, request):

        self.obtener_nodos(request)

        form = BuscarDestino()

        form_fechas = FormFechas()
        
        self.params['form']= form

        self.params['form_fechas']= form_fechas
        
        return render(request, 'hojaderuta/todos_los_envios.html', self.params)


usuario = Usuario()

usuario.obtener_links()


