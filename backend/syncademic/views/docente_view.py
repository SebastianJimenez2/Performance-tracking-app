from rest_framework import viewsets

from ..models.docente import Docente
from ..serializers.docente_serializer import DocenteSerializer

class DocenteViewSet(viewsets.ModelViewSet):
    queryset = Docente.objects.all()
    serializer_class = DocenteSerializer
