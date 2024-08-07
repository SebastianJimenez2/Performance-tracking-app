from rest_framework import viewsets, status
from rest_framework.response import Response

from ..serializers import AsistenciaSerializer
from ..exceptions.not_found import ObjectNotFound
from rest_framework.decorators import action
from ..services import AsistenciaService


class AsistenciaAPIView(viewsets.ViewSet):
    """ API Endpoint para Asistencia.
            Utilizado para Feature 1
            Creado por Christian Hernández
    """
    @action(detail=False, methods=['get'], url_path=r'estudiantes-en-riesgo/(?P<mes>\d+)')
    def estudiantes_en_riesgo(self, request, mes=None):
        """Obtiene la lista de estudiantes en riesgo de abandono basado en su tasa de asistencia para un mes específico.

            GET /estudiantes-en-riesgo/<int:mes>

            Parameters:
                mes (int): El mes (como número) para el cual se evalúa la tasa de asistencia.
        """
        try:
            mes = int(mes)
            estudiantes_en_riesgo = AsistenciaService.obtener_estudiantes_en_riesgo(mes)
            return Response({'estudiantes': estudiantes_en_riesgo}, status=status.HTTP_200_OK)
        except ValueError:
            return Response({'error': 'Mes no válido'}, status=status.HTTP_400_BAD_REQUEST)


    @action(detail=False, methods=['post'], url_path='registrar-asistencia')
    def actualizar_asistencia(self, request):
        """Actualiza la asistencia de un estudiante para una asignatura específica.

            POST /registrar-asistencia

            Body:
                {
                    "estudiante": <id_estudiante>,
                    "asignatura": <id_asignatura>,
                    "semana": <número_semana>,
                    "dia": <día_semana>,
                    "presente": <booleano>
                }

            Returns:
                Response: Una respuesta HTTP con un diccionario que indica si la actualización fue exitosa y si se creó un nuevo registro.
        """
        serializer = AsistenciaSerializer(data=request.data)
        if serializer.is_valid():
            estudiante_id = serializer.validated_data['estudiante'].id
            asignatura_id = serializer.validated_data['asignatura'].id
            semana = serializer.validated_data['semana']
            dia = serializer.validated_data['dia']
            presente = serializer.validated_data['presente']

            try:
                asistencia, created = AsistenciaService.actualizar_asistencia(
                    estudiante_id, asignatura_id, semana, dia, presente
                )
                return Response({'success': True, 'created': created}, status=status.HTTP_200_OK)
            except ObjectNotFound as e:
                return Response({'Error': e.detail}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    @action(detail=False, methods=['get'], url_path='lista-estudiantes')
    def lista_estudiantes(self, request):
        """Obtiene la lista de estudiantes con sus IDs y nombres.

            GET /lista-estudiantes
        """
        try:
            estudiantes = AsistenciaService.obtener_lista_estudiantes()
            return Response({'estudiantes': estudiantes}, status=status.HTTP_200_OK)
        except ObjectNotFound as e:
            return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)