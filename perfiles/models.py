from django.db import models
from django.contrib.auth.models import User
from nodos.models import Nodo
from impresoras.models import ImpresoraNodo


class Perfil(models.Model):
    """
    Indica a que nodo pertenece el usuario, si es repartidor, y que impresora tienen asignada
    """
    
    usuario = models.ForeignKey(User, on_delete= models.CASCADE, null= True,)

    nodo =  models.ForeignKey(Nodo, on_delete= models.CASCADE, null= True, blank= True)

    reparto = models.BooleanField(default= False)

    impresora = models.ForeignKey(ImpresoraNodo, on_delete= models.CASCADE, null= True, blank= True)

    def __str__(self):
      
        return str(self.usuario)
    
    def enviar_notificación(self,):

        print('Enviar notificacion a {}', self.usuario.email )
    
    def save(self, *args, **kwargs ):

        self.enviar_notificación()

        force_update = False

        if self.id:

            force_update = True

        super( Perfil, self ).save(force_update = force_update)