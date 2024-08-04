from ..models.cronograma import Cronograma
from ..exceptions import ObjectNotFound


class CronogramaService:

    @staticmethod
    def get_cronograma_by_id(cronograma_id: int):
        cronograma = Cronograma.objects.filter(id_cronograma=cronograma_id)
        if not cronograma:
            raise ObjectNotFound("Cronograma no encontrado")
        return cronograma

    @staticmethod
    def get_cronograma_asignatura(asignatura_id: int):
        cronograma = Cronograma.objects.filter(asignatura_id=asignatura_id)
        return cronograma
