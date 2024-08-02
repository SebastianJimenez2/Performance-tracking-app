from ..models import HistorialNotas, TipoActividad
from ..exceptions import ObjectNotFound
from backend.syncademic.utils.control_notas import ControlNotas


class NotasService:

    def __init__(self):
        self.id_asignatura = 1
        self.id_estudiante = 1
        self.periodo = 1

    # Se obtienen las notas del estudiante dado una materia y un periodo
    def get_notas_estudiante_asignatura(self):
        notas = HistorialNotas.objects.filter(id_asigantura=self.id_asignatura,
                                              id_estudiante=self.id_estudiante,
                                              periodo=self.periodo)
        if notas is None:
            raise ObjectNotFound(HistorialNotas._meta.model_name,
                                 "No se han encontrado registros para los parámetros dados")
        else:
            return notas

    # Se obtienen todas las notas basadas en una asignatura y un periodo
    def get_notas_asignatura(self):
        notas = HistorialNotas.objects.filter(id_asigantura=self.id_asignatura,
                                              periodo=self.periodo)
        if notas is None:
            raise ObjectNotFound(HistorialNotas._meta.model_name,
                                 "No se han encontrado registros para los parámetros dados")
        else:
            return notas

    def get_promedio_asignatura(self):
        try:
            notas = self.get_notas_estudiante_asignatura()

            return sum(notas['nota']) / len(notas['nota'])

        except ObjectNotFound:
            raise ObjectNotFound(HistorialNotas._meta.model_name, )

    def save_nueva_nota(self, nueva_nota: float, tema: str, tipo_actividad_nombre: str, grupo: int):
        HistorialNotas.objects.create(
            id_asignatura=self.id_asignatura,
            id_estudiante=self.id_estudiante,
            periodo=self.periodo,
            grupo=grupo,
            nota=nueva_nota,
            tema=tema,
            tipo_actividad=TipoActividad.objects.filter(nombre_tipo=tipo_actividad_nombre)
        )

    def get_alertas(self):
        control_nota = ControlNotas(promedio=self.get_promedio_asignatura())

        if control_nota.existe_riesgo:
            return control_nota.mensaje['advertencia']
        elif control_nota.existe_incidencia():
            # TODO: USAR MODELO DE ESTUDIANTE
            incidencias = 1
            return control_nota.definir_prioridad_alerta(incidencias)
        else:
            return control_nota.mensaje['respuesta']

    @property
    def id_asignatura(self):
        return self._id_asignatura

    @id_asignatura.setter
    def id_asignatura(self, id_asignatura):
        self._id_asignatura = id_asignatura

    @property
    def id_estudiante(self):
        return self._id_estudiante

    @id_estudiante.setter
    def id_estudiante(self, id_estudiante):
        self._id_estudiante = id_estudiante

    @property
    def periodo(self):
        return self._periodo

    @periodo.setter
    def periodo(self, periodo):
        self._periodo = periodo
