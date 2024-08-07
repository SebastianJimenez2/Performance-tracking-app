from rest_framework import serializers
from ..models.asistencia import Asistencia
from ..models.estudiante import Estudiante
from ..models.asignatura import Asignatura

class AsistenciaSerializer(serializers.ModelSerializer):
    estudiante = serializers.PrimaryKeyRelatedField(queryset=Estudiante.objects.all())
    asignatura = serializers.PrimaryKeyRelatedField(queryset=Asignatura.objects.all())

    class Meta:
        model = Asistencia
        fields = ['id_asistencia', 'estudiante', 'asignatura', 'semana', 'dia', 'presente']
