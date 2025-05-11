from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class PreguntasFrecuentes(models.Model):

    titulo  = models.CharField(max_length=30)

    contenido = RichTextUploadingField('contenido')

    def __str__(self):
        
        return self.titulo 
