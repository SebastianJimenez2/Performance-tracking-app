from typing import Dict, List
from ..models.tema_cronograma import TemaCronograma
from ..models.cronograma import Cronograma
from ..exceptions.not_found import ObjectNotFound
from ..utils import cronograma_utils


class CronogramaService:

    """
    @staticmethod
    def get_cronograma_by_id(cronograma_id: int):
        try:
            return Cronograma.objects.get(id=cronograma_id)
        except Cronograma.DoesNotExist:
            raise ObjectNotFound("Cronograma no encontrado")
    """

    """
    @staticmethod
    def get_cronograma_asignatura(asignatura_id: int):
        cronograma = Cronograma.objects.filter(asignatura_id=asignatura_id)
        return cronograma
    """
    
    @staticmethod
    def get_temas_cronograma(cronograma_id):
        try:
            cronograma = Cronograma.objects.get(id_cronograma=cronograma_id)
            return cronograma.temas.all()  # Devuelve todos los temas asociados al cronograma
        except Cronograma.DoesNotExist:
            raise ObjectNotFound('Cronograma not found')
        
    @staticmethod
    def get_temas_completados(cronograma_id: int, hasta_semana: int) -> int:
        try:
            cronograma = Cronograma.objects.get(pk=cronograma_id)  # Usar pk para obtener por id primario
            temas_completados_count = cronograma.temas.filter(
                completado=True, 
                semana_finalizacion_relativa_a_inicio__lte=hasta_semana
            ).count()  # Agregar .count() aquí para obtener la cantidad de temas completados
            return temas_completados_count
        except Cronograma.DoesNotExist:  # Usar la excepción apropiada para la no existencia de un objeto
            raise ValueError("Cronograma no encontrado")

    @staticmethod
    # setear el estado del cronograma cada vez que se chequea un tema_cronograma ESTO VA EN TEMAS_CRONOGRAMA_SERVICE
    def set_estado_cronograma(cronograma_id, nuevo_estado):
        try:
            cronograma = Cronograma.objects.get(id_cronograma=cronograma_id)
            cronograma.estado = nuevo_estado
            cronograma.save()
        except ObjectNotFound:
            raise ValueError(f"Cronograma con ID {cronograma_id} no encontrado")

    @staticmethod
    def get_estado_cronograma(cronograma_id: int):
        try:
            cronograma = Cronograma.objects.get(id_cronograma=cronograma_id)
            return cronograma.estado
        except Cronograma.DoesNotExist:
            raise ValueError("Cronograma no encontrado")
    
