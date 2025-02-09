from django.urls import path
from hojaderuta.views import usuario

urlpatterns = [
    
    path('', usuario.index, name= 'index'),
    
    path('<int:envio_id>/ver', usuario.ver_envio, name = 'ver_envio'),

]