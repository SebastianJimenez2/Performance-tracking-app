from rest_framework import serializers

from ..models.docente import Docente


class DocenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Docente
        fields = '__all__'


class ListaDocenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Docente
        fields = [
            "id_docente",
            "nombre_docente"
        ]