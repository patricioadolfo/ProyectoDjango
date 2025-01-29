from django.db.models.signals import post_save
from django.dispatch import receiver
from hojaderuta.models import Envio, SeguimientoDeEnvio
from farmacia.models import Parametros

parametro = Parametros()

@receiver( post_save, sender = Envio )
def crear_seguimiento( sender, instance, created, **kwargs):

    if created == True:

        SeguimientoDeEnvio.objects.create( 
            
            usuario = instance.usuario, 
            
            envio = instance, 
            
            estado =  parametro.preparado
            
            )

    elif created == False:

        SeguimientoDeEnvio.objects.create( 
            
            usuario = instance.usuario, 
            
            envio = instance, 
            
            estado =  instance.estado
            
            )
