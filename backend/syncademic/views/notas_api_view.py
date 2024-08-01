from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from ..serializers import NotasSerializer
from ..services import NotasService
from ..exceptions import ObjectNotFound


class HistorialNotasAPIView(APIView):
    permission_classes = (permissions.AllowAny,)

    @staticmethod
    def get_notas_estudiante(id_asignatura: int, id_estudiante: int, periodo: int):
        service = NotasService(id_asignatura, id_estudiante, periodo)
        try:
            notas = service.get_notas_estudiante_asignatura()
            serializer = NotasSerializer(notas, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ObjectNotFound as e:
            return Response({'Error': e.detail}, status=status.HTTP_404_NOT_FOUND)
