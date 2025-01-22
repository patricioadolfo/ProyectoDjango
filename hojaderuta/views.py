from django.shortcuts import render
from django.shortcuts import redirect
from farmacia.models import Parametros
from hojaderuta.forms import EnvioForm

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
                
                post = form.save(commit=False)

                post.user= request.user

                post.save()
                
                return redirect('mis_envios')   
            
            else: 
                print('sdfds')

        if request.user.is_authenticated:

            self.obtener_nodos(request)

            self.obtener_nodos_destinos()

            self.params['form'] = EnvioForm()

            for nodo in self.params['perfil']:
                
                self.params['preparados'].append(self.envio.filter(origen = nodo.nodo.id).filter(estado = self.preparado).exclude( origen = None ).exclude( destino = None ))

                self.params['en_camino'].append(self.envio.filter(estado = self.en_camino).filter(origen = nodo.nodo.id).exclude( origen = None ).exclude( destino = None ))       

        return render(request, 'hojaderuta/mis_envios.html', self.params )

    def para_recibir(self, request):

        self.params['preparados'] = []

        self.params['en_camino'] = []

        if request.user.is_authenticated:

            self.obtener_nodos(request)

            for nodo in self.params['nodos']:
                
                self.params['preparados'].append(self.envio.filter(destino= nodo.nodo.id).filter(estado = self.preparado).exclude( origen = None ))

                self.params['en_camino'].append(self.envio.filter(estado= self.en_camino).filter(destino = nodo.nodo.id).exclude( origen = None ))       

        return render(request, 'hojaderuta/para_recibir.html', self.params )

    def otros_destinos(self, request):

        self.params['otros_destinos'] = []

        if request.user.is_authenticated:

            self.obtener_nodos(request)

            for nodo in self.params['nodos']:
                
                self.params['otros_destinos'].append(self.envio.filter(origen = nodo.nodo.id).filter( destino = None ).exclude( estado = self.entregado ))   

        return render(request, 'hojaderuta/otros_destinos.html', self.params )

usuario = Usuario() 