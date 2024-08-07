from rest_framework import serializers
from ..models.asistencia import Asistencia
from ..models.estudiante import Estudiante
from ..models.asignatura import Asignatura

class AsistenciaSerializer(serializers.ModelSerializer):
    """ Serializer para modelo Asignatura

            Utilizado para Feature 1
            Creado por Christian Hernández
        """
    estudiante = serializers.PrimaryKeyRelatedField(queryset=Estudiante.objects.all())
    asignatura = serializers.PrimaryKeyRelatedField(queryset=Asignatura.objects.all())

    class Meta:
        model = Asistencia
        fields = ['id_asistencia', 'estudiante', 'asignatura', 'semana', 'dia', 'presente']
