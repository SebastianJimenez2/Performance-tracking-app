from rest_framework.views import APIView
from rest_framework.response import Response
from syncademic.services.seguimiento_malla_service import SeguimientoService
from ..serializers.estudiante_serializer import EstudianteSerializer


class SeguimientoMallaAPIView(APIView):
    def get(self, request, asignatura_prerequisito, periodo_actual):
        seguimiento_service = SeguimientoService(asignatura_prerequisito, periodo_actual)
        estudiantes = seguimiento_service.obtener_estudiantes_candidatos()
        serializer = EstudianteSerializer(estudiantes, many=True)
        return Response(serializer.data)
