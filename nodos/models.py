from django.db import models
from django.core.validators import RegexValidator
from estados.models import Estado

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

    estado = models.ForeignKey(Estado, on_delete= models.SET_NULL, null= True)

    def direccion(self,):
        """
        Retorna los 3 valores para panel-admin
        """

        return self.calle, self.numero, self.localidad

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

    estado = models.ForeignKey(Estado, on_delete= models.SET_NULL, null= True)

    def direccion(self,):
        """
        Retorna los 3 valores para panel-admin
        """

        return self.calle, self.numero, self.localidad
     

    def __str__(self):

        return self.nombre
