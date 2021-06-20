from rest_framework import serializers
from ..models import *


class PizzaVaultSerializer(serializers.ModelSerializer):
	class Meta:
		model = PizzaVault
		fields = '__all__'