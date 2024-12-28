from django.urls import path
from nodos import views

urlpatterns = [
    path('nodos/', views.ver_nodos, name= 'ver_nodos'),
    path('destinos/', views.ver_destinos, name= 'ver_destinos'),
]