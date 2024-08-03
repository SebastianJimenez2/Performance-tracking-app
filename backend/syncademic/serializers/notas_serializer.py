from rest_framework import serializers
from ..models import HistorialNotas


class NotasSerializer(serializers.ModelSerializer):
    tipo_actividad_nombre = serializers.CharField(source='tipo_actividad.nombre_tipo',
                                                  read_only=True)

    class Meta:
        model = HistorialNotas
        fields = ["id_asignatura",
                  "id_estudiante",
                  "grupo",
                  "periodo",
                  "nota",
                  "tipo_actividad_nombre",
                  "tema"]
