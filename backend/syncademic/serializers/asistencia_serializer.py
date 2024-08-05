from rest_framework import serializers
from ..models.asistencia import Asistencia
from . import EstudianteSerializer


class AsistenciaSerializer(serializers.ModelSerializer):
    estudiante = EstudianteSerializer()

    class Meta:
        model = Asistencia
        fields = ['id_asistencia', 'estudiante', 'asignatura', 'semana', 'dia', 'presente']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        from . import AsignaturaSerializer
        self.fields['asignatura'] = AsignaturaSerializer()
