from ..models import HistorialNotas
from ..exceptions import ObjectNotFound
from backend.syncademic.utils.control_notas import ControlNotas


class NotasService:

    def __init__(self, id_asignatura: int, id_estudiante: int, periodo: int):
        self.id_asignatura = id_asignatura
        self.id_estudiante = id_estudiante
        self.periodo = periodo

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
