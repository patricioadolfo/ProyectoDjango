from django.urls import path
from hojaderuta.views import usuario
from hojaderuta.views_ajax import VerEnviosPorDestinos
from hojaderuta.views_ajax import VerEnviosPorFecha
from hojaderuta.views_ajax import VerDestinos
from hojaderuta.views_ajax import VerImpresones 

urlpatterns = [
    
    path('', usuario.index, name= 'index'),
    
    path('<int:envio_id>/ver', usuario.ver_envio, name = 'ver_envio'),

    path('nuevo_envio', usuario.nuevo_envio, name = 'nuevo_envio'),

    path('envio_otro_destino', usuario.envio_otro_destino, name = 'envio_otro_destino'),

    path('todos_los_envios', usuario.todos_los_envios, name = 'todos_los_envios'),

    path('ver_envios', VerDestinos.as_view(), name = 'ver_envios' ),

    path('ver_envios_por_destino', VerEnviosPorDestinos.as_view(), name = 'ver_envios_por_destino' ),

    path('ver_envios_por_fecha', VerEnviosPorFecha.as_view(), name = 'ver_envios_por_fecha' ),

    path('ver_impresiones', VerImpresones.as_view(), name = 'ver_impresiones' ),

]