from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.decorators import action, api_view

from ..models.tema_cronograma import TemaCronograma

from ..serializers import CronogramaSerializer
from ..serializers import TemaCronogramaSerializer

from ..services import CronogramaService
from ..services import TemaCronogramaService
from ..exceptions.not_found import ObjectNotFound

from ..models.cronograma import Cronograma

class TemaCronogramaAPIView(viewsets.ModelViewSet):
    queryset = TemaCronograma.objects.all()
    serializer_class = TemaCronogramaSerializer

    @action(detail=True, methods=['put'], url_path='check')
    def check_tema(self, request, pk=None):
        fecha_actual = request.data.get('fecha_actual')
        if not fecha_actual:
            return Response({"error": "La fecha actual es requerida."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            TemaCronogramaService.set_completar_tema(pk, fecha_actual)
            return Response({"message": "Tema actualizado y cronograma recalculado"}, status=status.HTTP_200_OK)
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=False, methods=['post'], url_path='create')
    def crear_tema_cronograma(self, request):
        id_cronograma = request.data.get('cronograma')
        if not id_cronograma:
            return Response({'error': 'cronograma es requerido'}, status=status.HTTP_400_BAD_REQUEST)
        
        orden_cronologico = TemaCronogramaService.get_orden_tema(id_cronograma)
        semana_finalizacion = TemaCronogramaService.get_semana_finalizacion_relativa(id_cronograma)

        # Preparar los datos adicionales que no están directamente incluidos en el request.data
        data = request.data.copy()
        data['orden'] = orden_cronologico
        data['semana_finalizacion_relativa_a_inicio'] = semana_finalizacion
        data['cronograma'] = id_cronograma

        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Tema creado exitosamente'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    @api_view(['DELETE'])
    def delete_tema_cronograma(request, pk):
        try:
            tema = TemaCronograma.objects.get(id_tema=pk)
            tema.delete()
            return Response({'message': 'Eliminado exitosamente'}, status=status.HTTP_200_OK)
        except TemaCronograma.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
