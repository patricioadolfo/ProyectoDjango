from django.urls import path
from FAQ.views import preguntas_frecuentes

urlpatterns = [
    
    path('', preguntas_frecuentes, name= 'preguntas_frecuentes'),
    
]