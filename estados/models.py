from django.db import models

class Estado(models.Model):

    """
    Modelo para crear estados 
    """

    nombre= models.CharField(max_length=30, null= False)

    def __str__(self):
        """ 
        String que representa al objeto estado
        """
        return '%s' %self.nombre
