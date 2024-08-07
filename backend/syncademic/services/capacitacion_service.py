from ..exceptions.not_found import ObjectNotFound
from ..models.asignatura import Asignatura
from ..models.docente import Docente
from ..models.capacitacion import Capacitacion
from ..models.puntuacion_docente import Puntuacion_docente


class CapacitacionService:

    def __init__(self):
        self.periodo = None
        self.id_docente = None
        self.id_asignatura = None
        self.nombre_capacitacion = None
        self.area_capacitacion = None

    # Lista de Puntuaciones
    def get_lista_puntuaciones(self, id_docente):
        puntuaciones = Puntuacion_docente.objects.filter(
            id_docente__id_docente=id_docente
        ).values('id_puntuacion', 'id_docente', 'periodo', 'puntaje')
        if puntuaciones is None:
            raise ObjectNotFound(Capacitacion._meta.model_name,
                                 "No se han encontrado registros para los parámetros dados")
        else:
            return puntuaciones

    # Lista de capacitaciones de docente
    def get_lista_capacitaciones(self, id_docente):
        capacitaciones = Capacitacion.objects.filter(
            docente__id_docente=id_docente
        ).values('id_capacitacion', 'nombre_capacitacion', 'area', 'periodo')
        if capacitaciones is None:
            raise ObjectNotFound(Capacitacion._meta.model_name,
                                 "No se han encontrado registros para los parámetros dados")
        else:
            return capacitaciones

    def get_lista_docentes(self):
        docentes = Docente.objects.values('id_docente', 'nombre', 'carrera', 'correo')
        return docentes

    def get_docente(self, id_docente):
        try:
            docente = Docente.objects.filter(
                id_docente=id_docente
            ).values('id_docente', 'nombre', 'estado_capacitacion', 'carrera', 'correo', 'puntaje_actual')
            if not docente:
                raise ObjectNotFound(Docente._meta.model_name, "Docente no encontrado")
            return docente[0]
        except Exception as e:
            raise ObjectNotFound(Docente._meta.model_name, detail=str(e))


    def get_lista_all_capacitaciones(self):
        capacitaciones = Docente.objects.values('id_capacitacion', 'docente', 'nombre', 'area', 'periodo')
        return capacitaciones

    # notas de un estudiante basado en el periodo, grupo y asignatura
    def get_nota_capacitacion_docente(self, id_docente, capacitaciones) -> int:
        nota_docente = 0
        try:
            for capacitacion in capacitaciones:
                nota_docente += self.get_nota_docente(id_docente, capacitacion.get('area'))

            return nota_docente
        except Exception as e:
            print(e)

    def get_nota_docente(self, id_docente, area) -> int:
        nota = 2
        if self.get_area_docente(id_docente) == area:
            nota = 5
        return nota

    def get_area_docente(self, id_docente) -> str:
        asignaturas = Asignatura.objects.filter(
            docente__id_docente=id_docente
        ).values('area')
        return asignaturas[0].get('area')

    def save_capacitacion(self, data):
        try:

            docente_bd = Docente.objects.get(id_docente=1)

            Capacitacion.objects.create(
                docente=data.docente_bd,
                nombre_capacitacion=data.nombre_capacitacion,
                area=data.nombre_capacitacion,
                periodo=data.periodo
            )

            docente_bd.save()

        except Exception as e:
            raise ObjectNotFound(Docente._meta.model_name, detail=str(e))

    def get_alertas(self):
        alerta = {
            'Capacitacion agregada': "true",
            'Registro minimo': "completado"
        }

        return alerta

    @property
    def periodo(self):
        return self._periodo

    @periodo.setter
    def periodo(self, periodo):
        self._periodo = periodo

    @property
    def id_docente(self):
        return self._id_docente

    @id_docente.setter
    def id_docente(self, id_docente):
        self._id_docente = id_docente

    @property
    def id_asignatura(self):
        return self._id_asignatura

    @id_asignatura.setter
    def id_asignatura(self, id_asignatura):
        self._id_asignatura = id_asignatura

    @property
    def nombre_capacitacion(self):
        return self._nombre_capacitacion

    @nombre_capacitacion.setter
    def nombre_capacitacion(self, nombre_capacitacion):
        self._nombre_capacitacion = nombre_capacitacion

    @property
    def area_capacitacion(self):
        return self._area_capacitacion

    @area_capacitacion.setter
    def area_capacitacion(self, area_capacitacion):
        self._area_capacitacion = area_capacitacion

    @property
    def imagen_capacitacion(self):
        return self._imagen_capacitacion

    @imagen_capacitacion.setter
    def imagen_capacitacion(self, imagen_capacitacion):
        self._imagen_capacitacion = imagen_capacitacion
