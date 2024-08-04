import datetime
from ..models.tema_cronograma import TemaCronograma
from ..models.cronograma import Cronograma
from ..exceptions import ObjectNotFound
from ..services.cronograma_service import CronogramaService
from ..utils import cronograma_utils

class TemaCronogramaService:
    
    @staticmethod
    def get_temas_cronograma_by_cronograma_id(cronograma_id: int):
        temas_cronograma = TemaCronograma.objects.filter(cronograma_id=cronograma_id)
        return temas_cronograma
    
    # Se llama a esto cuando se inserta un nuevo tema_cronograma desde view
    @staticmethod
    def get_semana_finalizacion_esperada(cronograma: Cronograma, tiempo_en_semanas: int):
        semana_finalizacion_esperada = tiempo_en_semanas
        cronograma_id = cronograma.id_cronograma 

        temas = TemaCronograma.objects.filter(cronograma_id=cronograma_id)

        if len(temas) == 0:
            return semana_finalizacion_esperada

        for tema in sorted(temas, key=lambda x: x.orden):
            semana_finalizacion_esperada += tema.tiempo_en_semanas

        return semana_finalizacion_esperada
        
    @staticmethod
    def set_completar_tema(id_tema):
        tema_cronograma = TemaCronograma.objects.get(id_tema=id_tema)
        tema_cronograma.completado = True
        tema_cronograma.fecha_completado = datetime.date.today()
        tema_cronograma.save()

    @staticmethod
    def get_temas_completados_cronograma_semana(cronograma_id, semana_actual):
        temas_completados = 0
        temas = TemaCronograma.objects.filter(id_cronograma=cronograma_id)

        for tema in temas:
            if tema.completado and tema.semana_finalizacion_relativa_a_inicio <= semana_actual:
                temas_completados += 1

        return temas_completados
    
    @staticmethod
    def get_temas_completados_ideales_cronograma_semana_actual(cronograma_id, semana_actual):
        temas_completados = 0
        temas = TemaCronograma.objects.filter(id_cronograma=cronograma_id)

        for tema in temas:
            if tema.semana_finalizacion_relativa_a_inicio <= semana_actual:
                temas_completados += 1

        return temas_completados
    
    ## get temas de completos 