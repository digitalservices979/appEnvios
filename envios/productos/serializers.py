from rest_framework import serializers
from .models import Mascarilla, Pedido

class MascarillaSerializer(serializers.ModelSerializer):
	class Meta:
		model = Mascarilla
		fields = ('id','codigo','stock')

class PedidoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Pedido
		fields = ('id','nombre_negocio','nombre_propietario','dni','celular','correo','tipo_mascarilla',
			'cantidad','departamento','distrito','calle','latitud','longitud','imei'
			)