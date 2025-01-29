from django.shortcuts import render
from django.views.generic import View
from django.views.generic import FormView
from farmacia.models import Parametros
from nodos.forms import DestinoForm
# Create your views here.
class NodosDestinos(Parametros):

    def ver_nodos(self, request):

        if request.user.is_authenticated:

            self.obtener_nodos_destinos(self.nodos)

        return render(request, 'nodos/nodos.html', self.params )

    def ver_destinos(self, request):

        if request.user.is_authenticated:

            self.obtener_nodos_destinos(self.destinos)

        return render(request, 'nodos/nodos.html', self.params )
    

nodos_destinos= NodosDestinos()


class CrearDestino(FormView):

    template_name = 'nodos/crear_destino.html'

    form_class = DestinoForm

    success_url = 'destino_creado'

    def form_valid(self, form):

        form.save()

        form.notificar()

        return super().form_valid(form)
    

class DestinoCreado(View):

    template = 'nodos/destino_creado.html'

    def get(self, request):

        return render(request, self.template, {'mensaje': 'Destino Creado'})
