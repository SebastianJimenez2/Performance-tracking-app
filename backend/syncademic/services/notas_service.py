from ..models import HistorialNotas, TipoActividad
from ..exceptions import ObjectNotFound
from ..Utils import ControlNotas
from ..models.asignatura import Asignatura
from ..models.estudiante import Estudiante
from ..models.periodo import Periodo


class NotasService:

    def __init__(self):
        self.id_asignatura = None
        self.grupo = None
        self.periodo = None
        self.en_riesgo = None
        self.alerta_media = None
        self.alerta_alta = None

    # Lista de estudiantes de una asignatura
    def get_lista_estudiantes(self):
        estudiantes = Estudiante.objects.filter(
            asignaturas__id=self.id_asignatura,
            periodo_cursando__id_periodo=self.periodo,
            grupo_actual=self.grupo
        ).values('id_estudiante', 'nombre')
        if estudiantes is None:
            raise ObjectNotFound(HistorialNotas._meta.model_name,
                                 "No se han encontrado registros para los parámetros dados")
        else:
            return estudiantes

    # notas de un estudiante basado en el periodo, grupo y asignatura
    def get_notas_estudiante_asignatura(self, id_estudiante):
        notas = HistorialNotas.objects.filter(
            id_asignatura__id_asignatura=self.id_asignatura,
            id_estudiante__id_estudiante=id_estudiante,
            periodo__id_periodo=self.periodo,
            grupo=self.grupo
        ).values('id_estudiante', 'nombre')
        if notas is None:
            raise ObjectNotFound(HistorialNotas._meta.model_name,
                                 "No se han encontrado registros para los parámetros dados")
        else:
            return notas

    def get_promedio_asignatura(self, id_estudiante: int):
        try:
            notas_1 = self.get_notas_estudiante_asignatura(id_estudiante).filter(tipo_actividad_id=1).values('nota')
            notas_2 = self.get_notas_estudiante_asignatura(id_estudiante).filter(tipo_actividad_id=2).values('nota')

            promedio_1 = sum(notas_1) / TipoActividad.objects.filter(tipo_actividad_id=1).values('peso')
            promedio_2 = sum(notas_2) / TipoActividad.objects.filter(tipo_actividad_id=1).values('peso')

            return promedio_1 + promedio_2

        except ObjectNotFound:
            raise ObjectNotFound(HistorialNotas._meta.model_name,
                                 "No se han encontrado registros para los parámetros dados")

    def save_nota(self, nota: dict):
        try:
            id_est = nota['id_estudiante']
            estudiante = Estudiante.objects.get(id_estudiante=id_est)
            asignatura = Asignatura.objects.get(id_asignatura=self.id_asignatura)

            control_nota = ControlNotas(estudiante)
            control_nota.minimo_aceptable = asignatura.nota_minima
            control_nota.promedio = self.get_promedio_asignatura(int(id_est))

            if control_nota.existe_riesgo:
                self.en_riesgo += 1
            elif control_nota.existe_incidencia:
                control_nota.estudiante.numero_incidencias += 1
                control_nota.definir_prioridad_alerta()
                if control_nota.estudiante.prioridad == 'MEDIA':
                    self.alerta_media += 1
                else:
                    self.alerta_alta += 1

            estudiante = control_nota.estudiante
            estudiante.save()

            HistorialNotas.objects.create(
                id_asignatura=asignatura,
                id_estudiante=estudiante,
                grupo=self.grupo, periodo_id=self.periodo,
                nota=nota['nota'],
                tipo_actividad_id=nota['tipo_actividad'],
                tema=nota['tema'],
            )

        except Exception:
            raise ObjectNotFound(Estudiante._meta.model_name)

    def get_alertas(self):
        alerta = {}
        if self.en_riesgo > 0:
            alerta['en_riesgo'] = self.en_riesgo
        elif self.alerta_media > 0:
            alerta['alerta_media'] = self.alerta_media
        elif self.alerta_alta > 0:
            alerta['alerta_alta'] = self.alerta_alta
        return alerta

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

