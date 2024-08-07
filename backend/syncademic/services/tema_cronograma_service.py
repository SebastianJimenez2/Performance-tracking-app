import datetime
from ..models.tema_cronograma import TemaCronograma
from ..models.cronograma import Cronograma
from ..exceptions.not_found import ObjectNotFound
from ..services import CronogramaService
from ..utils import cronograma_utils

from datetime import datetime


class TemaCronogramaService:
    """ Servicio de Tema Cronograma

        Utilizado para Feature 5
        Creado por David Yanez
    """

    @staticmethod
    def set_completar_tema(id_tema, fecha_actual_str):
        fecha_formato = '%Y-%m-%d'
        fecha_actual = datetime.strptime(fecha_actual_str, fecha_formato)

        tema = TemaCronograma.objects.get(id_tema=id_tema)
        tema.completado = True
        tema.fecha_completado = fecha_actual

        cronograma = tema.cronograma
        fecha_inicio = cronograma.fecha_inicio
        semana_actual = cronograma_utils.calcular_semana_relativa(fecha_inicio.strftime('%Y-%m-%d'), fecha_actual_str)

        temas_completados = TemaCronogramaService.get_temas_completados_cronograma_semana_actual(
            cronograma.id_cronograma, semana_actual)
        temas_esperados = TemaCronogramaService.get_temas_completados_ideales_cronograma_semana_actual(
            cronograma.id_cronograma, semana_actual)

        estado = cronograma_utils.obtener_estado_cronograma(temas_completados, temas_esperados)
        CronogramaService.set_estado_cronograma(cronograma.id_cronograma, estado)

        tema.save()

    @staticmethod
    def get_orden_tema(id_cronograma):
        # Contar los temas existentes para ese cronograma
        numero_temas = TemaCronograma.objects.filter(cronograma_id=id_cronograma).count()
        # El nuevo tema tendrá un orden que es el siguiente número en la secuencia
        return numero_temas + 1

    @staticmethod
    def get_semana_finalizacion_relativa(id_cronograma):
        try:
            cronograma = Cronograma.objects.get(id_cronograma=id_cronograma)
            fecha_inicio = cronograma.fecha_inicio.strftime('%Y-%m-%d')
            fecha_actual = datetime.now().strftime('%Y-%m-%d')
            semana_finalizacion_relativa = cronograma_utils.calcular_semana_relativa(fecha_inicio, fecha_actual)
            return semana_finalizacion_relativa
        except ObjectNotFound:
            raise ValueError("Cronograma with id '{}' does not exist.".format(id_cronograma))

    @staticmethod
    def get_temas_completados_cronograma_semana_actual(cronograma_id, semana_actual):
        temas_completados = 0
        temas = TemaCronograma.objects.filter(cronograma_id=cronograma_id)

        for tema in temas:
            if tema.completado and tema.semana_finalizacion_relativa_a_inicio is not None and tema.semana_finalizacion_relativa_a_inicio <= semana_actual:
                temas_completados += 1

        return temas_completados

    # Para definir el estado de un docente (normal, atrasado o adelantado)
    @staticmethod
    def get_temas_completados_ideales_cronograma_semana_actual(cronograma_id, semana_actual):
        temas_completados = 0
        temas = TemaCronograma.objects.filter(cronograma_id=cronograma_id)

        for tema in temas:
            if int(tema.semana_finalizacion_relativa_a_inicio) <= semana_actual:
                temas_completados += 1

        return temas_completados

    ## get temas de completos 
    @staticmethod
    def get_temas_completos(cronograma_id):
        temas_completos = TemaCronograma.objects.filter(cronograma_id=cronograma_id, completado=True)
        return temas_completos
