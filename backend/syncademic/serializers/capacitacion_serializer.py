from rest_framework import serializers
from ..models.capacitacion import Capacitacion


class CapacitacionSerializer(serializers.ModelSerializer):


    class Meta:
        model = Capacitacion
        fields = '__all__'

