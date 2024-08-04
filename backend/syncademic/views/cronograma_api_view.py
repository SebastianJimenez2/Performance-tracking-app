from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from ..serializers.cronograma_serializer import CronogramaSerializer
from ..services.cronograma_service import CronogramaService
from ..exceptions import ObjectNotFound

class CronogramaAPIView(APIView):
    permission_classes = (permissions.AllowAny,)
    service = CronogramaService()

    def get_cronograma(self, request):
        data = {
            'id_cronograma': request.data['id_cronograma'],
            'tiempo_en_semanas': request.data['tiempo_en_semanas'],
            'completado': request.data['completado'],
            'fecha_completado': request.data['fecha_completado'],
            'fecha_inicio': request.data['fecha_inicio']
        }

        self.service.id_cronograma = data['id_cronograma']

        try:
            cronograma = self.service.get_cronograma()
            serializer = CronogramaSerializer(cronograma)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ObjectNotFound as e:
            return Response({'Error': e.detail}, status=status.HTTP_404_NOT_FOUND)

    def post_nuevo_cronograma(self, request):
        data = {
            'tiempo_en_semanas': request.data['tiempo_en_semanas'],
            'fecha_inicio': request.data['fecha_inicio']
        }
        self.service.tiempo_en_semanas = data['tiempo_en_semanas']
        self.service.fecha_inicio = data['fecha_inicio']

        self.service.save_nuevo_cronograma()

        self.service.get_alertas()