from django.forms import ModelForm
from nodos.models import Destino
from captcha.fields import CaptchaField

class DestinoForm(ModelForm):

    captcha = CaptchaField()

    class Meta:

        model = Destino

        fields = [

            'nombre','calle', 'numero', 'localidad', 'telefono', 'maps', 'estado' 

        ]

    def notificar(self,):

        nombre = self.cleaned_data['nombre']
        
        calle = self.cleaned_data['calle'] 
        
        numero = self.cleaned_data['numero']
        
        localidad = self.cleaned_data['localidad']
        
        telefono = self.cleaned_data['telefono']
        
        maps = self.cleaned_data['maps']
        
        estado = self.cleaned_data['estado']

        print('logica para enviar notificacion')