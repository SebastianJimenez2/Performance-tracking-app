from rest_framework import serializers

from ..models.puntuacion_docente import Puntuacion_docente


class PuntuacionesDocenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Puntuacion_docente
        fields = '__all__'
