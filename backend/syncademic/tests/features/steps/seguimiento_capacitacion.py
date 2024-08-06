from behave import *
from syncademic.utils import AreaDocente, AreaCapacitacion
from faker import Faker

from syncademic.utils.capacitaciones_utils import ControlAreas


# from syncademic.services.seguimiento_malla_service import SeguimientoService

#use_step_matcher("re")


@step('que un docente tiene como areas afines "{areas_afines}"')
def step_impl(context, areas_afines):
    """
    :type context: behave.runner.Context
    :type areas_afines: str
    """

    faker = Faker("es")
    context.docente = AreaDocente(faker.name())
    context.docente.areas = [area.strip() for area in areas_afines.split(',')]

    assert context.docente.areas == [area.strip() for area in areas_afines.split(',')]


@step('tiene una puntuacion inicial de "{puntuacion_inicial}"')
def step_impl(context, puntuacion_inicial):
    """
    :type context: behave.runner.Context
    :type puntuacion_inicial: str
    """

    context.docente.puntos_capacitacion = int(puntuacion_inicial)

    assert context.docente.puntos_capacitacion == int(puntuacion_inicial)


@step('el docente registra una capacitación en el área de "{area}"')
def step_impl(context, area):
    """
    :type context: behave.runner.Context
    :type area: str
    """
    faker = Faker("es")
    context.capacitacion = AreaCapacitacion(faker.street_name())
    context.capacitacion.area = str(area)

    assert context.capacitacion.area == str(area)


@step("su puntuación final será de {puntuacion_final}")
def step_impl(context, puntuacion_final):
    """
    :type context: behave.runner.Context
    :type area: str
    """

    context.control_areas = ControlAreas(context.docente, context.capacitacion)
    context.control_areas.calcular_puntuacion()

    assert context.docente.puntos_capacitacion == int(puntuacion_final)


@step('que el docente tiene "{capacitaciones}" registradas')
def step_impl(context, capacitaciones):
    """
        :type context: behave.runner.Context
        :type capacitaciones: str
    """
    faker = Faker()
    context.docente = AreaDocente(faker.name)
    context.docente.capacitaciones = int(capacitaciones)
    assert context.docente.capacitaciones == int(capacitaciones)


@step('se marca al registro del docente como "{estado}"')
def step_impl(context, estado):
    """
    :type context: behave.runner.Context
    :type estado: str
    """
    if context.docente.capacitaciones == 0:
        context.docente.estado = "incompleto"
    else:
        context.docente.estado = "completo"

    assert context.docente.estado == estado


@step('la institución decide que "{envia}" un recordatorio al docente')
def step_impl(context, envia):
    context.envia = envia.strip()
    if context.envia == 'envia':
        assert 'envia' == context.envia
    elif context.envia == 'no envia':
        assert 'no envia' == context.envia
