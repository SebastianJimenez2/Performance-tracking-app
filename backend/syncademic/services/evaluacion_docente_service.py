from collections import defaultdict
from typing import List, Tuple

from ..models.asignatura import Asignatura
from ..models.evaluacion_docente import Evaluacion
from ..utils.evaluacion_docente_utils import calcular_promedios


class evaluacion_docente_service:

    @staticmethod
    def get_evaluaciones_docente(docente_id: int):
        if docente_id is not None:
            return Evaluacion.objects.filter(docente=docente_id).select_related('asignatura')
        return Evaluacion.objects.none()


    @staticmethod
    def get_evaluaciones_asignatura(self):
        if self.id_asignatura is not None:
            return Evaluacion.objects.filter(asignatura=self.id_asignatura)
        return Evaluacion.objects.none()

    @staticmethod
    def get_evaluaciones_tipo(self):
        if self.id_tipo_evaluacion is not None:
            return Evaluacion.objects.filter(tipo_evaluacion=self.id_tipo_evaluacion)
        return Evaluacion.objects.none()

    @staticmethod
    def get_mejores_docentes_por_asignatura(tipo_evaluacion: int, asignatura: Asignatura) -> List[Tuple[str, float]]:
        evaluaciones = Evaluacion.objects.filter(tipo_evaluacion=tipo_evaluacion, asignatura=asignatura)

        return calcular_promedios(evaluaciones)

    @staticmethod
    def get_mejores_evaluaciones() -> List[Tuple[str, float]]:
        evaluaciones = Evaluacion.objects.all()
        return calcular_promedios(evaluaciones)
