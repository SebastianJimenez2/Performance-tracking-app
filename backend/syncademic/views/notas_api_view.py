from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from ..models import HistorialNotas
from ..serializers import NotasSerializer


class HistorialNotasAPIView(APIView):
    permission_classes = (permissions.AllowAny,)

    # Se obtienen las notas del estudiante dado una materia y un periodo
    def get_notas_estudiante(self, id_asignatura: int, id_estudiante: int, periodo: int):
        try:
            notas = HistorialNotas.objects.filter(id_asigantura=id_asignatura,
                                                  id_estudiante=id_estudiante,
                                                  periodo=periodo)
            serializer = NotasSerializer(notas, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except HistorialNotas.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    # Se obtienen todas las notas basadas en una asignatura y un periodo
    def get_notas_asignatura_periodo(self, id_asignatura: int, periodo: int):
        try:
            notas = HistorialNotas.objects.filter(id_asigantura=id_asignatura,
                                                  periodo=periodo)
            serializer = NotasSerializer(notas, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except HistorialNotas.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
