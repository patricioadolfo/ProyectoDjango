from django.urls import path
from hojaderuta.views import usuario

urlpatterns = [
    
    path('', usuario.index, name= 'index'),
    
    path('mis_envios/', usuario.mis_envios, name= 'mis_envios'),
    
    path('para_recibir/', usuario.para_recibir, name= 'para_recibir'),
    
    path('otros_destinos/', usuario.otros_destinos, name= 'otros_destinos'),
    
    path('<int:envio_id>/ver', usuario.ver_envio, name = 'ver_envio'),

]