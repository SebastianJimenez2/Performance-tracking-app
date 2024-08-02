from behave import *
from syncademic.Utils import ControlNotas, EstadoEstudiante
from faker import Faker


# use_step_matcher("re")


@step('un estudiante tiene un promedio de "{promedio}"')
def step_impl(context, promedio):
    """
    :type context: behave.runner.Context
    :type promedio: str
    """
    faker = Faker("es")
    context.estudiante = EstadoEstudiante(faker.name(), faker.email(), float(promedio))

    context.control_calificaciones = ControlNotas(context.estudiante)

    assert context.estudiante.promedio == float(promedio)


@step(
    'el profesor estableció un rango de advertencia de "{rango_advertencia:f}" para una nota mínima aceptable de "{'
    'minimo}"')
def step_impl(context, rango_advertencia, minimo):
    """
    :type context: behave.runner.Context
    :type rango_advertencia: str
    :type minimo: str
    """
    context.control_calificaciones.rango_advertencia = float(rango_advertencia)
    context.control_calificaciones.minimo_aceptable = float(minimo)

    context.en_riesgo = context.control_calificaciones.existe_riesgo

    assert isinstance(context.en_riesgo, bool)


@step('el profesor de la asignatura "{recibe}" recibe un mensaje de advertencia')
def step_impl(context, recibe):
    """
    :type context: behave.runner.Context
    :type recibe: str
    """
    if context.en_riesgo:
        context.recibe = "SI"
    else:
        context.recibe = "NO"

    assert context.recibe == recibe


@step('un estudiante tiene un promedio de "{promedio}" que ha bajado del mínimo "{ocasiones}" ocasiones')
def step_impl(context, promedio, ocasiones):

    faker = Faker("es")
    context.estudiante = EstadoEstudiante(faker.name(), faker.email(), float(promedio))
    context.estudiante.incidencias = int(ocasiones)
    context.estudiante.promedio = float(promedio)

    context.control_calificaciones = ControlNotas(context.estudiante)

    assert (context.control_calificaciones.estudiante.promedio == float(promedio)
            and context.control_calificaciones.estudiante.incidencias == int(ocasiones))


@step('baje del mínimo aceptable de "{minimo}" nuevamente')
def step_impl(context, minimo):

    context.ocasiones = context.estudiante.incidencias

    if context.control_calificaciones.existe_incidencia:
        context.control_calificaciones.estudiante.incidencias += 1

    assert context.control_calificaciones.estudiante.incidencias == context.ocasiones + 1


@step('el profesor de la asignatura recibe un mensaje de alerta con una prioridad "{prioridad}"')
def step_impl(context, prioridad):
    context.control_calificaciones.definir_prioridad_alerta()

    assert context.control_calificaciones.estudiante.prioridad == prioridad
