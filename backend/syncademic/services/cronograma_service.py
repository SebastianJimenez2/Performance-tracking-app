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
    def get_temas_cronograma(cronograma_id: int) -> List[Dict[str, any]]:
        try:
            cronograma = Cronograma.objects.get(id_cronograma=cronograma_id)
        except ObjectNotFound:
            return []  # Retorna una lista vacía si el cronograma no existe

        temas = cronograma.temas.all()
        return [{
            'id_tema': tema.id_tema,
            'descripcion': tema.descripcion,
            'orden': tema.orden,
            'tiempo_en_semanas': tema.tiempo_en_semanas,
            'completado': tema.completado,
            'semana_finalizacion_relativa_a_inicio': tema.semana_finalizacion_relativa_a_inicio,
            'fecha_completado': tema.fecha_completado if tema.completado else None  # solo devolver fecha si está completado
        } for tema in temas]
        
    @staticmethod
    def get_temas_completados(cronograma_id: int, hasta_semana: int):
        try:
            cronograma = Cronograma.objects.get(id_cronograma=cronograma_id)
            temas = cronograma.temas.filter(completado=True, semana_finalizacion_relativa_a_inicio__lte=hasta_semana)
            return temas
        except ObjectNotFound:
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
    
