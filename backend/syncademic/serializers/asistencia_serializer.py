from rest_framework import serializers
from ..models.asistencia import Asistencia
from . import EstudianteSerializer


class AsistenciaSerializer(serializers.ModelSerializer):
    estudiante = EstudianteSerializer()

    class Meta:
        model = Asistencia
        fields = ['id_asistencia', 'estudiante', 'asignatura', 'semana', 'dia', 'presente']

    def _init_(self, *args, **kwargs):
        super()._init_(*args, **kwargs)
        from . import AsignaturaSerializer
        self.fields['asignatura'] = AsignaturaSerializer()