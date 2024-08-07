from rest_framework import serializers
from syncademic.models.silabo import Tema, Silabo

# Primero, definir TemaSerializer porque SilaboSerializer lo referencia.
class TemaSerializer(serializers.ModelSerializer):
    # Campo opcional para calcular el promedio de las evaluaciones
    promedio_evaluaciones = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Tema
        fields = ['id', 'titulo', 'prueba_kahoot', 'prueba_sentimientos', 'prueba_tema']

    def get_promedio_evaluaciones(self, obj):
        # Obtener las evaluaciones y calcular el promedio si son válidas (no None)
        evaluaciones = [obj.prueba_kahoot, obj.prueba_sentimientos, obj.prueba_tema]
        evaluaciones = [e for e in evaluaciones if e is not None]  # Filtrar None
        if evaluaciones:
            return sum(evaluaciones) / len(evaluaciones)
        return "No se puede determinar"

#TemaSerializer para los temas asociados
class SilaboSerializer(serializers.ModelSerializer):
    # Incluir temas como un campo anidado usando TemaSerializer
    temas = TemaSerializer(many=True, read_only=True)

    class Meta:
        model = Silabo
        fields = ['id', 'asignatura', 'temas']

