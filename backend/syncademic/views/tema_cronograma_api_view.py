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
    queryset = Cronograma.objects.all()
    serializer_class = CronogramaSerializer

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

    @api_view(['POST'])
    def crear_tema_cronograma(request, id_tema):
        id_cronograma = request.data.get('id_cronograma')
        if not id_cronograma:
            return Response({'error': 'id_cronograma es requerido'}, status=status.HTTP_400_BAD_REQUEST)
        
        orden = TemaCronogramaService.get_orden_tema(id_cronograma)
        semana_finalizacion = TemaCronogramaService.get_semana_finalizacion_relativa(id_cronograma)

        # Crear el tema con los datos obtenidos y adicionales del body
        nuevo_tema = TemaCronograma.objects.create(
            id_cronograma=id_cronograma,
            orden=orden,
            semana_finalizacion_relativa_a_inicio=semana_finalizacion,
            **request.data
        )
        nuevo_tema.save()

        return Response({'message': 'Tema creado exitosamente'}, status=status.HTTP_201_CREATED)
