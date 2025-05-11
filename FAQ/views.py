from django.shortcuts import render
from FAQ.models import PreguntasFrecuentes

def preguntas_frecuentes(request):

    faq = PreguntasFrecuentes.objects.all()

    return render(request, 'FAQ/faq.html', { 'preguntas': faq })
