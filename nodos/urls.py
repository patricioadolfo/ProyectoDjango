from django.urls import path
from nodos.views import nodos_destinos, CrearDestino, DestinoCreado

urlpatterns = [
    
    path('nodos/', nodos_destinos.ver_nodos, name= 'ver_nodos'),
    
    path('destinos/', nodos_destinos.ver_destinos, name= 'ver_destinos'),
    
    path('destinos/nuevo/', CrearDestino.as_view(), name = 'crear_destino'),
    
    path('nuevo/destino_creado/', DestinoCreado.as_view(), name = 'destino_creado'),

]