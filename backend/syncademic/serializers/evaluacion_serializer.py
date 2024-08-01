from rest_framework import serializers

from ..models.evaluacion import Evaluacion


class EvaluacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evaluacion
        fields = '__all__'
