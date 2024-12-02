from django.db import models
from django.contrib.auth.models import User
from nodos.models import Nodo, Destino
from estados.models import Estado
from django.utils.html import format_html
from datetime import datetime
import time


class Envio(models.Model):

    """
    Crea los envios. Por defecto se crean los envios con la fecha y hora actual.
    """
    
    usuario= models.ForeignKey(User, on_delete=models.SET_NULL, null= True)
    
    origen = models.ForeignKey(Nodo, related_name='origen', on_delete=models.SET_NULL, null= True)

    otro_origen = models.ForeignKey(Destino, related_name='otro_origen', on_delete=models.SET_NULL, null= True, blank= True)

    estado = models.ForeignKey(Estado, on_delete=models.SET_NULL, null= True,)
   
    destino = models.ForeignKey(Nodo, related_name= 'destino', on_delete=models.SET_NULL, null= True)
    
    otro_destino = models.ForeignKey(Destino, related_name='otro_destino',  on_delete= models.SET_NULL, null= True, blank= True)
    
    descripcion = models.TextField(max_length=1000, help_text="Ingrese una breve descripción del envío.", null= False)
    
    fecha = models.DateField("Fecha de Creacion", null= True, blank=True, default= datetime.today().strftime("%Y-%m-%d"))
    
    hora = models.TimeField("Hora de Creacion", null= True, blank=True, default= time.strftime("%H:%M:%S", time.localtime()))
    
    class Meta:
        
        ordering = ["-id"]

    def __str__(self):
        """ 
        String que representa al objeto envio
        """
        return '%s' %self.id

    def envio_estado(self,):

        if self.estado.nombre == 'PREPARADO':

            return format_html('<span style= "color: #00F44A;">{}</spam>', self.estado,)
        
        elif self.estado.nombre == 'EN CAMINO':

            return format_html('<span style= "color: #F5E900;">{}</spam>', self.estado,)
        
        elif self.estado.nombre == 'ENTREGADO':

            return format_html('<span style= "color: #0110F5;">{}</spam>', self.estado,)
        
        elif self.estado.nombre == 'IGNORADO':

            return format_html('<span style= "color: #F50101;">{}</spam>', self.estado,)           

        else:
            return self.estado

class SeguimientoDeEnvio(models.Model):
    """
    Detalla el estado actual quedando a modo de historial de cada envío.
    """
    
    usuario= models.ForeignKey(User, on_delete=models.SET_NULL, null= True)
    
    envio = models.ForeignKey(Envio, on_delete=models.SET_NULL, null=True,)
    
    estado = models.ForeignKey(Estado, on_delete=models.SET_NULL, null= True,)
    
    fecha_de_modificacion = models.DateField(null=True, blank=True, default= datetime.today().strftime("%Y-%m-%d"))
    
    hora_de_modificacion = models.TimeField("Hora de modificacion", null= True, blank=True, default= time.strftime("%H:%M:%S", time.localtime()))   
    
    class Meta:
        
        ordering = ["-fecha_de_modificacion"]

    def __str__(self):
        """
        String para representar el Objeto del Seguimiento de envio
        """
        return '%s' %(self.id)
    