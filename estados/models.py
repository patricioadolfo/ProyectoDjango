from django.db import models
from django.utils.html import format_html

class Estado(models.Model):

    """
    Modelo para crear estados 
    """

    nombre= models.CharField(max_length=30, null= False)

    color= models.CharField(max_length=30, null= True, blank= True)

    def color_estado(self,):

        print(type(self.color))

        return format_html('<span style= "color:{};">{}</span>', self.color, self.nombre,)

    def __str__(self):
        """ 
        String que representa al objeto estado
        """
        return '%s' %self.nombre
