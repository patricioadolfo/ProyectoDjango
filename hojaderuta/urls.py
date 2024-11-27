from django.urls import path
from hojaderuta import views

urlpatterns = [
    path('', views.index, name= 'index'),
]