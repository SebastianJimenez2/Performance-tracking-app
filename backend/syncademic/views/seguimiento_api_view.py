from rest_framework.views import APIView
from rest_framework.response import Response
from syncademic.services.seguimiento_malla_service import SeguimientoService


class ListaEstudiantesCandidatosCursoVerano(APIView):
    def get(self, request, asignatura_prerequisito, periodo_actual):
        seguimiento_service = SeguimientoService(asignatura_prerequisito, periodo_actual)
        data = seguimiento_service.obtener_estudiantes_candidatos()
        return Response(data)
