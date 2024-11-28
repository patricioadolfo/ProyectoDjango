from django.db import models
from estados.models import Estado

class Link(models.Model):
    """
    Links para agregar dendro de el footer.
    """

    nombre = models.CharField(max_length=100, null= False)

    url = models.URLField(max_length= 100, null= False)

    icono = models.ImageField(upload_to="iconos/%Y/%m/%d", blank=True, null=True)

    estado = models.ForeignKey(Estado, on_delete= models.SET_NULL, null= True)

    def __str__(self):
        
        return str(self.nombre)