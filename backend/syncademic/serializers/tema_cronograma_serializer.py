from rest_framework import serializers
from ..models.tema_cronograma import TemaCronograma


class TemaCronogramaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TemaCronograma
        fields = '__all__'
