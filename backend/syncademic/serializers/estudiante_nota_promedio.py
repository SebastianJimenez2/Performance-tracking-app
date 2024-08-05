from rest_framework import serializers
from ..models.estudiante import Estudiante


class EstudianteNotaPromedioSerializer(serializers.ModelSerializer):
    promedio_notas = serializers.FloatField()
    class Meta:
        model = Estudiante
        fields = ['id_estudiante', 'nombre', 'numero_incidencias', 'promedio_notas']