from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from ..serializers import ListaEstudianteSerializer
from ..services import NotasService
from ..exceptions import ObjectNotFound
import json


class HistorialNotasAPIView(APIView):
    permission_classes = (permissions.AllowAny,)
    service = NotasService()

    def get(self, request, id_asignatura, periodo, grupo, *args, **kwargs):

        self.service.id_asignatura = id_asignatura
        self.service.periodo = periodo
        self.service.grupo = grupo

        try:
            estudiantes = self.service.get_lista_estudiantes()
            serializer = ListaEstudianteSerializer(estudiantes, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ObjectNotFound as e:
            return Response({'Error': e.detail}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request, id_asignatura, periodo, grupo, *args, **kwargs):
        mensaje = {'response': 'No se han procesado los datos'}
        for notas_data in request.data:
            data = {
                'id_estudiante': notas_data['id_estudiante'],
                'nombre': notas_data['nombre'],
                'nota': notas_data['nota'],
                'tema': notas_data['tema'],
                'tipo_actividad': notas_data['tipo_actividad'],
            }

            self.service.id_asignatura = id_asignatura
            self.service.periodo = periodo
            self.service.grupo = grupo

            self.service.save_nota(data)

            mensaje = self.service.get_alertas()

        return Response(json.dumps(mensaje), status=status.HTTP_201_CREATED)


