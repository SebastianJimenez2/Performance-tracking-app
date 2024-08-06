from behave import *
from syncademic.utils import AreaDocente, AreaCapacitacion
from faker import Faker

# from syncademic.services.seguimiento_malla_service import SeguimientoService

use_step_matcher("re")

@step('que las áreas afines del docente son "(?P<areas_afines>.+)"')
def step_impl(context, areas_afines):
    """
    :type context: behave.runner.Context
    :type areas_afines: list
    """
    faker = Faker("es")
    context.docente = AreaDocente(faker.name(), areas_afines)

    assert context.docente.tiene_area(areas_afines)


@step('la puntuación inicial del docente es "(?P<puntuacion_inicial>.+)"')
def step_impl(context, puntuacion_inicial):
    """
    :type context: behave.runner.Context
    :type puntuacion_inicial: str
    """
    context.docente.puntos_capacitacion = int(puntuacion_inicial)

    assert context.docente.puntos_capacitacion == int(puntuacion_inicial)


@step('el docente registra una capacitación en el área de "(?P<area>.+)"')
def step_impl(context, area):
    def step_impl(context, area):
        """
        :type context: behave.runner.Context
        :type area: str
        """
        faker = Faker("es")
        context.capacitacion = AreaCapacitacion( faker.street_title(), area)

        assert context.capacitacion.area == str(area)