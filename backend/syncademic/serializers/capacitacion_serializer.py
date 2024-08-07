from rest_framework import serializers
from ..models.capacitacion import Capacitacion


class CapacitacionSerializer(serializers.ModelSerializer):


    class Meta:
        model = Capacitacion
        fields = '__all__'

class ListaCapacitacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Capacitacion
        fields = [
            "id_capacitacion",
            "nombre_capacitacion"
        ]