from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from ..serializers import NotasSerializer
from ..services import NotasService
from ..exceptions import ObjectNotFound


class HistorialNotasAPIView(APIView):
    permission_classes = (permissions.AllowAny,)
    service = NotasService()

    def get_notas_estudiante(self, request):

        data = {
            'id_asignatura': request.data['id_asignatura'],
            'id_estudiante': request.data['id_estudiante'],
            'periodo': request.data['periodo']
        }

        self.service.id_asignatura = data['id_asignatura']
        self.service.id_estudiante = data['id_estudiante']
        self.service.periodo = data['periodo']

        try:
            notas = self.service.get_notas_estudiante_asignatura()
            serializer = NotasSerializer(notas, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ObjectNotFound as e:
            return Response({'Error': e.detail}, status=status.HTTP_404_NOT_FOUND)
<<<<<<< HEAD

    def post_nueva_nota_estudiante(self, request):

        data = {
            'id_asignatura': request.data['id_asignatura'],
            'id_estudiante': request.data['id_estudiante'],
            'periodo': request.data['periodo'],
            'grupo': request.data['grupo'],
            'tema': request.data['tema'],
            'nota': request.data['nota'],
            'tipo_actividad_nombre': request.data['tipo_actividad'],
        }
        self.service.id_asignatura = data['id_asignatura']
        self.service.id_estudiante = data['id_estudiante']
        self.service.periodo = data['periodo']

        self.service.save_nueva_nota(nueva_nota=data['nota'], grupo=data['grupo'],
                                     tema=data['tema'], tipo_actividad_nombre=data['tipo_actividad'])

        self.service.get_alertas()
=======
>>>>>>> 2b918400d20eeafce9b3a0e7117dee2c2afa3ac6
