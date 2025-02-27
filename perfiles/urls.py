from django.urls import path
from perfiles.views import perfil

urlpatterns = [
    
    path('ver_perfil', perfil.ver_perfil, name = 'ver_perfil'),

    path('modificar_nodos', perfil.modificar_nodos, name = 'modificar_nodos'),

    path('actualizar_datos', perfil.actualizar_datos, name = 'actualizar_datos'),

]