from rest_framework import serializers
from ..models.tema_cronograma import TemaCronograma


class TemaCronogramaSerializer(serializers.ModelSerializer):
    """ Serializer para modelo TemaCronograma

        Utilizado para Feature 5
        Creado por David Yanez
    """
    class Meta:
        model = TemaCronograma
        fields = '__all__'
