from rest_framework import serializers
from ..models.capacitacion import Capacitacion


class CapacitacionSerializer(serializers.ModelSerializer):
    """ Serializer para modelo Capacitacion

                Utilizado para Feature 8
                Creado por Christopher Zambrano
    """
    class Meta:
        model = Capacitacion
        fields = '__all__'


class ListaCapacitacionSerializer(serializers.ModelSerializer):
    """ Lista de capacitaciones.

        Utilizado para Feature 8
        Creado por Christopher Zambrano
    """
    class Meta:
        model = Capacitacion
        fields = [
            "id_capacitacion",
            "nombre_capacitacion"
        ]