from rest_framework import serializers
from ..models.cronograma import Cronograma


class CronogramaSerializer(serializers.ModelSerializer):
    """ Serializer para modelo Cronograma

        Utilizado para Feature 5
        Creado por David Yanez
    """
    class Meta:
        model = Cronograma
        fields = '__all__'
