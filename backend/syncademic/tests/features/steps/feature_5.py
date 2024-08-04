from behave import *
from backend.syncademic.models.asignatura import Asignatura
from backend.syncademic.models.cronograma import Cronograma
from backend.syncademic.models.tema_cronograma import TemaCronograma
from backend.syncademic.services.cronograma_service import CronogramaService
from backend.syncademic.services.tema_cronograma_service import TemaCronogramaService
from backend.syncademic.utils import cronograma_utils as CronogramaUtils
from django.db import models


@step('el docente visualiza su progreso de la semana {semana_actual} en base a que {temas_marcados}')
def step_impl(context, semana_actual, temas_marcados):
    context.semana_actual = semana_actual
    context.temas_marcados = temas_marcados

    context.asignatura = Asignatura.objects.create(
        id_asignatura=1,
        prerequisito=None,
        subsecuente=None,
        nota_minima=0.0,
        nombre="",
        grupo="",
        area="",
        total_clases=0,
        total_inscritos=0,
        total_comprende=0
    )

    context.cronograma = Cronograma.objects.create(
        id_cronograma=1,
        id_asignatura=context.asignatura,
        fecha_inicio=models.DateField("2024-01-01")
    )

    context.tema_cronograma1 = TemaCronograma.objects.create(
        id_tema=2,
        id_cronograma=context.cronograma,
        descripcion="Tema 1",
        orden=2,
        tiempo_en_semanas=2,
        completado=False,
        semana_finalizacion_relativa_a_inicio=TemaCronogramaService.get_semana_finalizacion_esperada(
            context.cronograma, 2),
        fecha_completado=None
    )

    context.tema_cronograma2 = TemaCronograma.objects.create(
        id_tema=2,
        id_cronograma=context.cronograma,
        descripcion="Tema 2",
        orden=2,
        tiempo_en_semanas=1,
        completado=False,
        semana_finalizacion_relativa_a_inicio=TemaCronogramaService.get_semana_finalizacion_esperada(
            context.cronograma, 1),
        fecha_completado=None
    )

    context.tema_cronograma3 = TemaCronograma(
        id_tema=3,
        id_cronograma=context.cronograma,
        descripcion="Tema 3",
        orden=3,
        tiempo_en_semanas=1,
        completado=False,
        semana_finalizacion_relativa_a_inicio=TemaCronogramaService.get_semana_finalizacion_esperada(
            context.cronograma, 1),
        fecha_completado=None
    )

    TemaCronogramaService.set_completar_tema(context.tema_cronograma1.id_tema)  # setear completado=True
    TemaCronogramaService.set_completar_tema(context.tema_cronograma2.id_tema)  # setear completado=True

    # context.semana_fecha_actual = CronogramaService.get_semana_fecha(context.cronograma.id_cronograma,
    # context.semana_actual) # Obtener la fecha de la semana actual

    # # Verificar que temas tienen completado=True hasta la semana actual (devuelve int)
    context.temas_completados = TemaCronogramaService.get_temas_completados_cronograma_semana(
        context.cronograma.id_cronograma, context.semana_actual)  # Verificar que temas tienen completado=True
    # Aqui consideramos que cada tema_cronograma puede durar 1 o más semanas Ir verificando cual de los
    # temas_cronograma tiene un semana_finalizacion_relativa_a_inicio menor o igual a la semana_actual Devuelve el
    # int que se acumule
    context.temas_completados_ideales_fecha = TemaCronogramaService.get_temas_completados_ideales_cronograma_semana_actual(
        context.cronograma.id_cronograma, context.semana_actual)  # Verificar que temas tienen completado=True

    context.progreso = CronogramaUtils.obtener_progreso(context.temas_completados,
                                                        context.temas_completados_ideales_fecha)

    assert context.progreso == temas_marcados


@step('se visualiza un progreso {estado} respecto a la proyección ideal')
def step_impl(context, estado):
    context.estado = CronogramaUtils.obtener_estado_cronograma(context.temas_completados,
                                                               context.temas_completados_ideales_fecha)
    assert context.estado == estado
