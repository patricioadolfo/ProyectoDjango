from rest_framework import serializers
from hojaderuta.models import Envio

class EnvioSerializer(serializers.ModelSerializer):

	class Meta:

		model = Envio

		fields = '__all__'
