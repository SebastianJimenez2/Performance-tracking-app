from rest_framework import serializers
from ..models.asistencia import Asistencia
from . import EstudianteSerializer
from . import AsignaturaSerializer


class AsistenciaSerializer(serializers.ModelSerializer):
    estudiante = EstudianteSerializer()
    asignatura = AsignaturaSerializer()

    class Meta:
        model = Asistencia
        fields = ['id_asistencia', 'estudiante', 'asignatura', 'semana', 'dia', 'presente']