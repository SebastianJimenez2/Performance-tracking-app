from rest_framework import serializers
from ..models.estudiante import Estudiante


class EstudianteNotaPromedioSerializer(serializers.ModelSerializer):
    """
        Clase necesaria para determinar los atributos a presentar del estudiante.
        Pese a que es similar a 'estudiante_serializer', esta clase es útil porque
        define solo atributos específicos, y uno nuevo.

        Utilizado para Feature 4.
    """

    promedio_notas = serializers.FloatField()
    class Meta:
        """
            Clase que señala los atributos - campos a mostrar del modelo estudiante.
        """
        model = Estudiante
        fields = ['id_estudiante', 'nombre_estudiante', 'email', 'promedio_notas']