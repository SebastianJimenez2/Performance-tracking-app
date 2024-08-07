from rest_framework import serializers
from ..models.asignatura import Asignatura


class AsignaturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asignatura
        fields = '__all__'


class ListaAsignaturasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asignatura
        fields = [
            "id_asignatura",
            "nombre"
        ]