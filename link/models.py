from django.db import models
from estados.models import Estado
from django.utils.html import format_html
class Links(models.Model):
    """
    Links para agregar dendro de el footer.
    """

    nombre = models.CharField(max_length=100, null= False)

    url = models.URLField(max_length= 100, null= False)

    icono = models.ImageField(upload_to="iconos/%Y/%m/%d", blank=True, null=True)

    estado = models.ForeignKey(Estado, on_delete= models.SET_NULL, null= True)

    def estado_link(self,):

        if type(self.estado.color) != 'NoneType':

            return format_html ('<span style= "color: {};">{}</span>', self.estado.color, self.estado)       

        else:
            return self.estado

    def ver_imagen(self,):

        return format_html('<img src="/media/{}" width= "30" height= "30"/>', self.icono)

    def __str__(self):
        
        return str(self.nombre)
    
