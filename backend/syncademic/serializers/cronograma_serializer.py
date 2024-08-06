from rest_framework import serializers
from ..models.cronograma import Cronograma


class CronogramaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cronograma
        fields = '__all__'
