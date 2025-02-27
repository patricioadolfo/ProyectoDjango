from django.shortcuts import render
from django.shortcuts import redirect
from farmacia.models import Parametros
from django.contrib.auth.models import User
from perfiles.models import Perfil  
from perfiles.forms import PerfilForm, UsuarioForm

# Create your views here.
class Perfiles(Parametros):

    def ver_perfil(self, request):

        if request.user.is_authenticated:

            self.obtener_nodos(request)

            self.obtener_nodos_destinos(self.nodos)

            self.params['usuario'] = User.objects.get(id= request.user.id)

            self.params['form_nodos'] = PerfilForm()
            
            return render(request, 'perfil/perfil.html', self.params )
        
    def modificar_nodos(self, request):

        if request.method == "POST": 
            
            form = PerfilForm(request.POST)  

            if form.is_valid():

                nodos = form.cleaned_data['nodos']

                try:

                    perfil = Perfil.objects.get(usuario= request.user)

                    perfil.nodos.clear()

                    for nodo in nodos:

                        perfil.nodos.add(nodo)
                    
                    perfil.save()

                except Perfil.DoesNotExist:
                    
                    Perfil.objects.create( usuario = self.params['usuario'])

                    perfil = Perfil.objects.get(usuario= request.user)

                    for nodo in nodos:

                        perfil.nodos.add(nodo)
                    
                    perfil.save()
                
                return redirect('index')
            
    def actualizar_datos(self, request):

        if request.method == "POST": 
        
            form = UsuarioForm(request.POST)  

            if form.is_valid():

                nombre = form.cleaned_data['first_name']

                apellido = form.cleaned_data['last_name']

                email = form.cleaned_data['email']

                user = User.objects.get(id = request.user.id)

                user.first_name = nombre

                user.last_name = apellido

                user.email = email

                user.save()

        return redirect('index')
        
perfil = Perfiles()

perfil.obtener_links()
