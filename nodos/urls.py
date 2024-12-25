from django.urls import path
from nodos import views

urlpatterns = [
    path('nodos/', views.ver_nodos, name= 'ver_nodos'),
]