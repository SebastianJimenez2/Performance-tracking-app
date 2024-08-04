from rest_framework import serializers
from ..models.tema_cronograma import Tema

class TemaCronogramaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tema
        fields = '__all__'
        