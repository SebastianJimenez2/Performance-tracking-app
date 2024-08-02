from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


class ListaEstudiantesCandidatosCursoVerano(APIView):
    def get(self, request, asignatura_subsecuente, periodo_actual, asignatura_prerequisito, periodo_anterior):
        pass
