from django.db import models
from django.core.validators import RegexValidator
from estados.models import Estado
from django.utils.html import format_html

class Nodo(models.Model):
    """
    Nodos disponibles para envios y recepcion de pedidos
    """
    nombre  = models.CharField(max_length=30)
    
    calle = models.CharField(max_length=30)

    numero = models.IntegerField(null= False)

    localidad = models.CharField(max_length=30)
    
    NumTelefonoRegex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    
    telefono = models.CharField(validators=[NumTelefonoRegex], max_length=16, unique=True)

    maps = models.TextField(max_length=1000, blank=True, null=True)

    estado = models.ForeignKey(Estado, on_delete= models.SET_NULL, null= True)

    def direccion(self,):
        """
        Retorna los 3 valores para panel-admin
        """

        return self.calle, self.numero, self.localidad
    
    def ver_maps(self):
        """
        Retorna mapa de google-maps para sitio de usuario
        """

        return format_html ('<iframe src="{}" width="300" height="225" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>', self.maps)       

    def __str__(self):

        return self.nombre


class Destino(models.Model):  
    """
    Representa destinos fuera de la organización para enviar o recibir pedidos
    """
    nombre  = models.CharField(max_length=30)
    
    calle = models.CharField(max_length=30, blank= True)

    numero = models.IntegerField(null= False)

    localidad = models.CharField(max_length=30, blank= True)
    
    NumTelefonoRegex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    
    telefono = models.CharField(validators=[NumTelefonoRegex], max_length=16, unique=True)

    maps = models.TextField(max_length=1000, blank=True, null=True)

    estado = models.ForeignKey(Estado, on_delete= models.SET_NULL, null= True)

    def direccion(self,):
        """
        Retorna los 3 valores para panel-admin
        """

        return self.calle, self.numero, self.localidad
    
    def ver_maps(self):
        """
        Retorna mapa de google-maps para sitio de usuario
        """
        
        return format_html ('<iframe src="{}" width="300" height="225" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>', self.maps)       

    
    def __str__(self):

        return self.nombre
