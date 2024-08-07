from rest_framework import serializers
from ..models.estudiante import Estudiante


class EstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudiante
        fields = '__all__'


class ListaEstudianteSerializer(serializers.ModelSerializer):
    """ Lista de estudiantes para iniciar proceso de ingreso de notas.

        Utilizado para Feature 2
        Creado por Alejandra Colcha
    """
    class Meta:
        model = Estudiante
        fields = [
            "id_estudiante",
            "nombre_estudiante"
        ]
