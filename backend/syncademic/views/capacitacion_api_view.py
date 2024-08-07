from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework import permissions

from ..models.capacitacion import Capacitacion
from ..serializers import ListaDocenteSerializer, DocenteSerializer
from ..serializers import ListaCapacitacionSerializer, CapacitacionSerializer
from ..services import CapacitacionService
from ..exceptions.not_found import ObjectNotFound


class CapacitacionAPIView(viewsets.ModelViewSet):
    """ API Endpoint para ControlAreas.
            Utilizado para Feature 8
            Creado por Christopher Zambrano
    """
    queryset = Capacitacion.objects.all()
    serializer_class = CapacitacionSerializer
    permission_classes = (permissions.AllowAny,)
    service = CapacitacionService()

    #get lista de capacitaciones de un profesor
    @action(detail=False, methods=['get'],
            url_path='(?P<id_docente>[^/.]+)/capacitaciones')
    def get_lista_capacitaciones_docente(self, request, id_docente):
        self.service.id_docente = id_docente
        """ Obtiene la lista de capacitaciones de un profesor.
                    GET /<int:id_docente>/capacitaciones>
        """
        try:
            docente = self.service.get_lista_capacitaciones(id_docente)
            return Response(docente, status=status.HTTP_200_OK)
        except ObjectNotFound as e:
            return Response({'Error': e.detail}, status=status.HTTP_404_NOT_FOUND)

    #get lista docentes
    @action(detail=False, methods=['get'], url_path='docentes')
    def get_lista_docentes(self, request):
        """ Obtiene la lista de docentes.
                            GET /docentes>
        """
        try:
            docentes = self.service.get_lista_docentes()
            serializer = ListaDocenteSerializer(docentes, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ObjectNotFound as e:
            return Response({'Error': e.detail}, status=status.HTTP_404_NOT_FOUND)

    # Obtener docente por ID
    @action(detail=False, methods=['get'], url_path='docente/(?P<id_docente>[^/.]+)')
    def get_docente_by_id(self, request, id_docente):
        """ Obtiene un docente por su id.
                            GET /docente/<int:id_docente>
        """
        try:
            docente = self.service.get_docente(id_docente)
            return Response(docente, status=status.HTTP_200_OK)
        except ObjectNotFound as e:
            return Response({'Error': e.detail}, status=status.HTTP_404_NOT_FOUND)

    #get lista capacitaciones
    @action(detail=False, methods=['get'], url_path='capacitaciones')
    def get_lista_capacitaciones(self, request):
        """ Obtiene la lista de capacitaciones.
                            GET /capacitaciones>
        """
        try:
            capacitaciones = self.service.get_lista_docentes()
            serializer = ListaCapacitacionSerializer(capacitaciones, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ObjectNotFound as e:
            return Response({'Error': e.detail}, status=status.HTTP_404_NOT_FOUND)

    # get lista de puntuaciones de un docente
    @action(detail=False, methods=['get'], url_path='(?P<id_docente>[^/.]+)/puntuacionesViejas')
    def get_lista_puntaje_docente(self, request, id_docente):
        """ Obtiene la lista de puntuaciones de un docente.
                            GET /<int:id_docente>/puntuacionesViejas>
        """
        try:
            puntuaciones = self.service.get_lista_puntuaciones(id_docente)
            serializer = ListaCapacitacionSerializer(puntuaciones, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ObjectNotFound as e:
            return Response({'Error': e.detail}, status=status.HTTP_404_NOT_FOUND)

            # Método POST para añadir una nueva capacitación

    @action(detail=True, methods=['post'], url_path='capacitacion/nueva/')
    def post_capacitacion(self, request, id_profesor):
        """ Actualiza la lista de capacitaciones.
            POST /capacitacion/nueva

            Body: lista de objetos con atributos [id_profesor, nombre, area, periodo]

            Response: [capacitacion_agregada, registro_minimo]
        """
        periodo = 6
        for capacitacion_data in request.data:
            data = {
                'id_profesor': capacitacion_data['id_profesor'],
                'nombre_capacitacion': capacitacion_data['nombre'],
                'area': capacitacion_data['area'],
                'periodo': capacitacion_data['periodo']
            }

            self.service.id_profesor = id_profesor
            self.service.periodo = periodo
            self.service.save_capacitacion(data)

        mensaje = self.service.get_alertas()
        return Response(mensaje, status=status.HTTP_201_CREATED)
