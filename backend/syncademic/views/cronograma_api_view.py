from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.decorators import action, api_view

from ..serializers import CronogramaSerializer
from ..serializers import TemaCronogramaSerializer

from ..services import CronogramaService
from ..exceptions.not_found import ObjectNotFound

from ..models.cronograma import Cronograma

class CronogramaAPIView(viewsets.ModelViewSet):
    queryset = Cronograma.objects.all()
    serializer_class = CronogramaSerializer

    @action(detail=False, methods=['get'], url_path='temas-cronograma/(?P<cronograma_id>[^/.]+)')
    def temas_cronograma(self, request, cronograma_id=None):
        """
            Obtiene todos los temas de un cronograma.
            GET /cronograma/temas-cronograma/<int:cronograma_id>
        """
        try:
            temas = CronogramaService.get_temas_cronograma(int(cronograma_id))
            if temas:
                return Response({'temas': temas}, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'No temas found for this cronograma'}, status=status.HTTP_404_NOT_FOUND)
        except ValueError:
            return Response({'error': 'Invalid cronograma ID'}, status=status.HTTP_400_BAD_REQUEST)
        except ObjectNotFound:
            return Response({'error': 'Cronograma not found'}, status=status.HTTP_404_NOT_FOUND)
        
    @action(detail=True, methods=['get'], url_path='completados')
    def get_completados(self, request, pk=None):
        """
            Obtiene el numero de temas completados hasta una semana especificada.
            GET cronograma/<int:cronograma_id>/completados?hasta_semana=<int:semana>
        """
        hasta_semana = request.query_params.get('hasta_semana')
        if hasta_semana is None:
            return Response({"error": "Se requiere el parámetro 'hasta_semana'."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            hasta_semana = int(hasta_semana)
            temas_completados_count = CronogramaService.get_temas_completados(pk, hasta_semana)
            return Response({"temas_completados": temas_completados_count}, status=status.HTTP_200_OK)
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    @action(detail=True, methods=['get'], url_path='estado')
    def get_estado(self, request, pk=None):
        """
            Obtiene el estado de un cronograma.
            GET cronograma/<int:cronograma_id>/estado
        """
        try:
            estado = CronogramaService.get_estado_cronograma(int(pk))
            return Response({'estado': estado}, status=status.HTTP_200_OK)
        except ValueError as e:
            return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    
    @api_view(['DELETE'])
    def delete_cronograma(request, pk):
        try:
            tema = Cronograma.objects.get(id_cronograma=pk)
            tema.delete()
            return Response({'message': 'Eliminado exitosamente'}, status=status.HTTP_200_OK)
        except Cronograma.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    