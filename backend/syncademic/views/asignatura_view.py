from rest_framework import viewsets, status

from ..serializers.asignatura_serializer import AsignaturaSerializer

from ..models.asignatura import Asignatura


class AsignaturaViewSet(viewsets.ModelViewSet):
    queryset = Asignatura.objects.all()
    serializer_class = AsignaturaSerializer
