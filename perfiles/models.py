from django.db import models
from django.contrib.auth.models import User
from nodos.models import Nodo
from impresoras.models import ImpresoraNodo


class Perfil(models.Model):
    """
    Indica a que nodos pertenece el usuario, si es repartidor o no, y que 
    impresora tienen asignada
    """
    
    usuario = models.OneToOneField(User, on_delete= models.CASCADE, null= True,)

    nodos =  models.ManyToManyField(Nodo, related_name="nodos")

    reparto = models.BooleanField(default= False)

    impresora = models.ForeignKey(ImpresoraNodo, on_delete= models.CASCADE, null= True, blank= True)

    def __str__(self):
        """
        Retorna nombre de usuario.
        """   
        return str(self.usuario)
    
    def enviar_notificación(self,):
        """
        Logica para enviar email de notificación.
        """

        print('Enviar notificacion a {}', self.usuario.email )
    
    def save(self, *args, **kwargs ):
        """
        Logica para ejecutar accion al momento de guardar información.
        """

        self.enviar_notificación()

        force_update = False

        if self.id:

            force_update = True

        super( Perfil, self ).save(force_update = force_update)