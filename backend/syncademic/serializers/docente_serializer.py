from rest_framework import serializers

from ..models.docente import Docente


class DocenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Docente
        fields = '__all__'
