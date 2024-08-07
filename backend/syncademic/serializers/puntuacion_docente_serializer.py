from rest_framework import serializers

from ..models.puntuacion_docente import Puntuacion_docente


class PuntuacionesDocenteSerializer(serializers.ModelSerializer):
    """ Serializer para modelo Puntuacion_ocente

                Utilizado para Feature 8
                Creado por Christopher Zambrano
    """
    class Meta:
        model = Puntuacion_docente
        fields = '__all__'
