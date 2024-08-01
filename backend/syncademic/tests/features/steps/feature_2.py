from behave import *
from syncademic.utils.control_notas import ControlNotas


# use_step_matcher("re")


@step('un estudiante tiene un promedio de "{promedio}"')
def step_impl(context, promedio):
    """
    :type context: behave.runner.Context
    :type promedio: str
    """
    context.control_calificaciones = ControlNotas(promedio=float(promedio))
    assert context.control_calificaciones.promedio == float(promedio)


@step(
    'el profesor estableció un rango de advertencia de "{rango_advertencia:f}" para una nota mínima aceptable de "{minimo}"')
def step_impl(context, rango_advertencia, minimo):
    """
    :type context: behave.runner.Context
    :type rango_advertencia: str
    :type minimo: str
    """
    context.control_calificaciones.rango_advertencia = float(rango_advertencia)
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

    context.control_calificaciones = ControlNotas(promedio=float(promedio))
    context.ocasiones = int(ocasiones)

    assert context.control_calificaciones.promedio == float(promedio)


@step('baje del mínimo aceptable de "{minimo}" nuevamente')
def step_impl(context, minimo):

    if context.control_calificaciones.existe_incidencia:
        context.ocasiones_final = context.ocasiones + 1

    assert context.ocasiones_final == context.ocasiones + 1


@step('el profesor de la asignatura recibe un mensaje de alerta con una prioridad "{prioridad}"')
def step_impl(context, prioridad):
    context.response = context.control_calificaciones.definir_prioridad_alerta(context.ocasiones_final)

    assert context.response['prioridad'] == prioridad
