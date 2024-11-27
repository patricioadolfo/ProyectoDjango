from django.db import models
from nodos.models import Nodo
from hojaderuta.models import Envio
from estados.models import Estado

class ImpresoraNodo(models.Model):
    """
    Tabla para asignar impresoras termicas a los nodos (destinado a API)
    """

    nombre= models.CharField(max_length=100, null= False)

    nodo= models.ForeignKey(Nodo, on_delete=models.SET_NULL, null= True)

    estado= models.ForeignKey(Estado, on_delete= models.SET_NULL, null= True)

    def __str__(self,):
        
        return self.nombre
    
class ColaDeImpresion(models.Model):
    """
    Tabla para asignar trabajos de impresion a impresoras x nodo (destinado a API)
    """

    trabajo = models.ForeignKey(Envio, on_delete=models.SET_NULL, null= True)

    impresora = models.ForeignKey(ImpresoraNodo, on_delete=models.SET_NULL, null= True)

    estado = models.ForeignKey(Estado, on_delete=models.SET_NULL, null= True)

    def __str__(self,):
       
        return self.trabajo
