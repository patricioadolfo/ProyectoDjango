from django.urls import path
from hojaderuta.views import usuario

urlpatterns = [
    
    path('', usuario.index, name= 'index'),
    
    path('<int:envio_id>/ver', usuario.ver_envio, name = 'ver_envio'),

    path('nuevo_envio', usuario.nuevo_envio, name = 'nuevo_envio'),

    path('envio_otro_destino', usuario.envio_otro_destino, name = 'envio_otro_destino'),

    path('todos_los_envios', usuario.todos_los_envios, name = 'todos_los_envios'),

    path('agregar', usuario.agregar, name = 'agregar'),

]