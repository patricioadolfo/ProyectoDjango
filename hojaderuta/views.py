from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):

    params= {}

    params['nombre'] = 'HojaDeRuta'

    return render(request, 'hojaderuta/index.html', params )