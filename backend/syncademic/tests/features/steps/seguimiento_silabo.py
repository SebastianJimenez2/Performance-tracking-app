from datetime import datetime, timedelta

from behave import *

from syncademic.models.asistencia import Asignatura
from syncademic.models.cronograma import Cronograma
from syncademic.models.tema_cronograma import TemaCronograma
from syncademic.services.cronograma_service import CronogramaService
from syncademic.services.tema_cronograma_service import TemaCronogramaService
from syncademic.utils import cronograma_utils


@step('el docente visualiza su progreso de la semana {semana_actual} en base a que {temas_marcados}')
def step_impl(context, semana_actual, temas_marcados):
    context.semana_actual = int(semana_actual)
    context.temas_marcados = temas_marcados

    context.fecha_actual = datetime.now()
    format = '%Y-%m-%d'

    context.fecha_actual = context.fecha_actual.strftime(format)

    context.asignatura = Asignatura(
        id_asignatura=8012,
        prerequisito=None,
        subsecuente=None,
        nota_minima=0.0,
        nombre="",
        area="",
        total_clases=0,
        total_inscritos=0,
        total_comprende=0
    )

    context.cronograma = Cronograma(
        id_cronograma=1,
        asignatura=context.asignatura,
        fecha_inicio=datetime.now() - timedelta(weeks=5),
    )

    context.tema_cronograma1 = TemaCronograma(
        id_tema=2,
        cronograma=context.cronograma,
        descripcion="Tema 1",
        orden=1,
        tiempo_en_semanas=1,
        completado=False,
        semana_finalizacion_relativa_a_inicio=1,
        fecha_completado=None
    )

    context.tema_cronograma2 = TemaCronograma(
        id_tema=2,
        cronograma=context.cronograma,
        descripcion="Tema 2",
        orden=2,
        tiempo_en_semanas=1,
        completado=False,
        semana_finalizacion_relativa_a_inicio=context.tema_cronograma1.semana_finalizacion_relativa_a_inicio + 1,
        fecha_completado=None
    )

    context.tema_cronograma3 = TemaCronograma(
        id_tema=3,
        cronograma=context.cronograma,
        descripcion="Tema 3",
        orden=3,
        tiempo_en_semanas=2,
        completado=False,
        semana_finalizacion_relativa_a_inicio=context.tema_cronograma2.semana_finalizacion_relativa_a_inicio + 2,
        fecha_completado=None
    )
    
    # setear el atributo completado de los 2 primeros temas en True
    context.tema_cronograma1.completado = True
    context.tema_cronograma2.completado = True

    context.temas_cronograma = [context.tema_cronograma1, context.tema_cronograma2, context.tema_cronograma3]

    context.temas_completados = 0

    for tema in context.temas_cronograma:
        if tema.completado:
            context.temas_completados += 1

    context.temas_completados_ideales_fecha = 0
    
    for tema in context.temas_cronograma:
        if tema.semana_finalizacion_relativa_a_inicio <= context.semana_actual:
            context.temas_completados_ideales_fecha += 1
    
    context.progreso = cronograma_utils.obtener_progreso(context.temas_completados,
                                                         context.temas_completados_ideales_fecha)

    assert context.progreso == temas_marcados


@step('se visualiza un progreso {estado} respecto a la proyección ideal')
def step_impl(context, estado):
    context.estado = cronograma_utils.obtener_estado_cronograma(context.temas_completados,
                                                                context.temas_completados_ideales_fecha)
    assert context.estado == estado
