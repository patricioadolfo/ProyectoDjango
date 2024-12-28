from django.urls import path
from hojaderuta import views

urlpatterns = [
    path('', views.index, name= 'index'),
    path('mis_envios/', views.mis_envios, name= 'mis_envios'),
    path('para_recibir/', views.para_recibir, name= 'para_recibir'),
    path('otros_destinos/', views.otros_destinos, name= 'otros_destinos'),
]