from rest_framework import serializers
from ..models import Actividad


class ActividadSerializer(serializers.ModelSerializer):
    tipo_actividad_nombre = serializers.CharField(source='tipo_actividad.nombre_tipo',
                                                  read_only=True)

    class Meta:
        model = Actividad
        fields = ["id_actividad",
                  "id_asignatura",
                  "nota",
                  "tipo_actividad_nombre",
                  "tema"]
