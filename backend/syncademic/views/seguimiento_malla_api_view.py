from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from ..models.estudiante import Estudiante
from syncademic.services.seguimiento_malla_service import SeguimientoService
from ..serializers.estudiante_nota_promedio import EstudianteNotaPromedioSerializer


class SeguimientoMallaAPIView(viewsets.ModelViewSet):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteNotaPromedioSerializer

    @action(detail=False, methods=['get'], url_path='(?P<asignatura_prerequisito>[^/.]+)/(?P<periodo_actual>[^/.]+)')
    def get(self, request, asignatura_prerequisito, periodo_actual):
        try:
            seguimiento_service = SeguimientoService(asignatura_prerequisito, periodo_actual)
            estudiantes = seguimiento_service.obtener_estudiantes_candidatos()
            serializer = self.get_serializer(estudiantes, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

