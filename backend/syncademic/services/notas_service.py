from django.db.models import Avg
from ..exceptions.not_found import ObjectNotFound
from ..utils import ControlNotas, EstadoEstudiante
from ..models.asignatura import Asignatura
from ..models.estudiante import Estudiante
from ..models.notas import HistorialNotas, TipoActividad


class NotasService:
    """ Servicio de notas

        Attributes:
             id_asignatura
             periodo
             grupo

        Utilizado para Feature 2
        Creado por Alejandra Colcha
    """

    def __init__(self):
        self.id_asignatura = None
        self.grupo = None
        self.periodo = None
        self.en_riesgo = 0
        self.alerta_media = 0
        self.alerta_alta = 0

    def get_lista_estudiantes(self):
        """ Lista de estudiantes para ingresar notas

            Según asignatura, grupo y periodo configurado para el servicio

            Return:
                lista_estudiantes (dict): [id_estudiante, nombre_estudiante]
        """
        estudiantes = Estudiante.objects.filter(
            asignaturas__id_asignatura=self.id_asignatura,
            periodo_cursando__id_periodo=self.periodo,
            grupo_actual=self.grupo
        ).values('id_estudiante', 'nombre_estudiante')
        if estudiantes is None:
            raise ObjectNotFound(HistorialNotas._meta.model_name,
                                 "No se han encontrado registros para los parámetros dados")
        else:
            return estudiantes

    def get_promedios_estudiantes(self):
        """Lista de estudiantes para ingresar notas

            Según asignatura, grupo y periodo configurado para el servicio

            Return:
                lista_estudiantes (dict): [id_estudiante, nombre_estudiante, email, numero_incidencias, prioridad]
        """
        estudiantes = Estudiante.objects.filter(
            asignaturas__id_asignatura=self.id_asignatura,
            periodo_cursando__id_periodo=self.periodo,
            grupo_actual=self.grupo
        ).values('id_estudiante', 'nombre_estudiante', 'email', 'numero_incidencias', 'prioridad')

        for estudiante in estudiantes:
            promedio = self.get_promedio_asignatura(estudiante.get('id_estudiante'))
            estudiante['promedio'] = round(promedio, 2)

        return estudiantes

    def get_notas_estudiante_asignatura(self, id_estudiante):
        """
            Notas de un estudiante según la asignatura, grupo y periodo configurado para el servicio

            Parameters:
                id_estudiante (int): [id_estudiante]

            Return:
                lista_notas (dict): [id_estudiante, tipo_actividad, nota]
        """
        notas = HistorialNotas.objects.filter(
            id_asignatura__id_asignatura=self.id_asignatura,
            id_estudiante__id_estudiante=id_estudiante,
            periodo__id_periodo=self.periodo,
            grupo=self.grupo
        ).values('id_estudiante', 'tipo_actividad', 'nota')
        if notas is None:
            raise ObjectNotFound(HistorialNotas._meta.model_name,
                                 "No se han encontrado registros para los parámetros dados")
        else:
            return notas

    def get_promedio_asignatura(self, id_estudiante: int) -> float:
        """Promedio de un estudiante según asignatura, grupo y periodo configurado para el servicio

            Parameters:
                id_estudiante (int): [id_estudiante]

            Return:
                promedio (float)
        """

        promedio_1 = 0.0
        promedio_2 = 0.0
        try:
            notas_1 = (self.get_notas_estudiante_asignatura(id_estudiante)
            .filter(tipo_actividad_id=1).aggregate(total=Avg('nota'))['total'])
            notas_2 = (self.get_notas_estudiante_asignatura(id_estudiante)
            .filter(tipo_actividad_id=2).aggregate(total=Avg('nota'))['total'])

            peso_1 = TipoActividad.objects.filter(id_tipo_actividad=1).values('peso').first().get('peso')
            peso_2 = TipoActividad.objects.filter(id_tipo_actividad=2).values('peso').first().get('peso')

            notas_1 = float(notas_1) if notas_1 else 0.0
            notas_2 = float(notas_2) if notas_2 else 0.0
            peso_1 = float(peso_1) if peso_1 else 0.0
            peso_2 = float(peso_2) if peso_2 else 0.0

            promedio_1 = notas_1 * peso_1
            promedio_2 = notas_2 * peso_2

            if notas_2 == 0:
                return promedio_1 * 2
            elif notas_1 == 0:
                return promedio_2 * 2
            else:
                return promedio_1 + promedio_2

        except Exception as e:
            print(e)

    def save_nota(self, nota: dict):
        """ Guarda una nota en un estudiante asignatura en el modelo Historial Notas
            Contabiliza las alertas de estudiantes según prioridad: RIESGO, MEDIA, ALTA.

            Parameters:
                nota (dict): [id_estudiante, id_asignatura, grupo, nota, tipo_actividad, tema]
        """

        try:

            id_est = nota['id_estudiante']
            estudiante_bd = Estudiante.objects.get(id_estudiante=id_est)
            asignatura = Asignatura.objects.get(id_asignatura=self.id_asignatura)

            HistorialNotas.objects.create(
                id_asignatura=asignatura,
                id_estudiante=estudiante_bd,
                grupo=self.grupo, periodo_id=self.periodo,
                nota=nota['nota'],
                tipo_actividad_id=nota['tipo_actividad'],
                tema=nota['tema'],
            )

            estado_est = EstadoEstudiante(estudiante_bd.nombre_estudiante, estudiante_bd.email)
            estado_est.numero_incidencias = estudiante_bd.numero_incidencias

            control_nota = ControlNotas(estado_est)
            control_nota.minimo_aceptable = asignatura.nota_minima
            control_nota.promedio = round(self.get_promedio_asignatura(int(id_est)), 2)

            if control_nota.existe_incidencia:
                control_nota.estudiante.numero_incidencias += 1
                control_nota.definir_prioridad_alerta()
                if control_nota.estudiante.prioridad == 'MEDIA':
                    self.alerta_media += 1
                else:
                    self.alerta_alta += 1

            if control_nota.existe_riesgo and control_nota.estudiante.prioridad == 'BAJA':
                self.en_riesgo += 1
                control_nota.estudiante.prioridad = 'RIESGO'
            else:
                control_nota.definir_prioridad_alerta()

            estudiante_bd.numero_incidencias = control_nota.estudiante.numero_incidencias
            estudiante_bd.prioridad = control_nota.estudiante.prioridad if control_nota.estudiante.prioridad is not None else estudiante_bd.prioridad

            estudiante_bd.save()
        except Exception as e:
            raise ObjectNotFound(Estudiante._meta.model_name, detail=str(e))

    def get_alertas(self):
        """ Crea el objeto que retorna el conteo de las alertas según prioridad.

            Return:
                alerta (dict): [en_riesgo, alerta_media, alerta_alta]
        """

        alerta = {
            'en_riesgo': self.en_riesgo,
            'alerta_media': self.alerta_media,
            'alerta_alta': self.alerta_alta
        }

        return alerta

    def reset_conteo_alertas(self):
        """ Reinicia el contador de alertas del servicio. """

        self.en_riesgo = 0
        self.alerta_media = 0
        self.alerta_alta = 0

    @property
    def id_asignatura(self):
        return self._id_asignatura

    @id_asignatura.setter
    def id_asignatura(self, id_asignatura):
        self._id_asignatura = id_asignatura

    @property
    def grupo(self):
        return self._grupo

    @grupo.setter
    def grupo(self, grupo):
        self._grupo = grupo

    @property
    def periodo(self):
        return self._periodo

    @periodo.setter
    def periodo(self, periodo):
        self._periodo = periodo

    @property
    def alerta_media(self):
        return self._alerta_media

    @alerta_media.setter
    def alerta_media(self, alerta_media):
        self._alerta_media = alerta_media

    @property
    def alerta_alta(self):
        return self._alerta_alta

    @alerta_alta.setter
    def alerta_alta(self, alerta_alta):
        self._alerta_alta = alerta_alta

    @property
    def en_riesgo(self):
        return self._en_riesgo

    @en_riesgo.setter
    def en_riesgo(self, en_riesgo):
        self._en_riesgo = en_riesgo
