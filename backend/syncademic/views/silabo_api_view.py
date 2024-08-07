from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action

from syncademic.services.silabo_service import *
from syncademic.serializers.tema_serializer import *
from syncademic.exceptions.not_found import ObjectNotFound

class SilaboAPIView(viewsets.ViewSet):

    @action(detail=True, methods=['get'], url_path='temas')
    def obtener_temas(self, request, pk=None):
        """
        Retorna todos los temas asociados a un sílabo específico.
        """
        try:
            silabo = Silabo.objects.get(pk=pk)
            temas = silabo.temas.all()
            serializer = TemaSerializer(temas, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Silabo.DoesNotExist:
            return Response({'error': 'Sílabo no encontrado'}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=True, methods=['get'], url_path='evaluaciones-tema/(?P<tema_id>\d+)')
    def obtener_evaluaciones_tema(self, request, pk=None, tema_id=None):
        """
        Retorna las evaluaciones para un tema específico de un sílabo.
        """
        try:
            evaluaciones = SilaboService.obtener_evaluaciones_tema(tema_id)
            return Response(evaluaciones, status=status.HTTP_200_OK)
        except ObjectNotFound as e:
            return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=False, methods=['get'], url_path='todos-silabos')
    def listar_todos_los_silabos(self, request):
        """
        Lista todos los sílabos.
        """
        silabos = Silabo.objects.all()
        serializer = SilaboSerializer(silabos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


