from rest_framework import viewsets
from hojaderuta.models import Envio
from api.serializer import EnvioSerializer

class EnvioViewset(viewsets.ModelViewSet):

	queryset = Envio.objects.all()

	serializer_class = EnvioSerializer
