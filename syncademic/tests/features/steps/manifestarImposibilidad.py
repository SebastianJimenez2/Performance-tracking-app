from behave import *

#use_step_matcher("re")


@step('que el docente desea saber el promedio histórico de notas finales de los estudiantes de la materia "{asignatura_sin_subsecuente}" en el periodo actual "{periodo_actual}"')
def step_impl(context, asignatura_sin_subsecuente, periodo_actual):
    context.asignatura_sin_subsecuente = asignatura_sin_subsecuente
    context.periodo_actual = periodo_actual

    context.historial_notas = HistorialNotas()

    assert None == context.historial_notas.obtener_promedio_histórico(None, context.periodo_actual, context.asignatura_sin_subsecuente, None)



@step("se determine que la asignatura indicada no tiene una asignatura subsecuente")
def step_impl(context):
    try:
        context.historial_notas.obtener_estudiantes_candidatos(None, context.periodo_actual,
                                                               context.asignatura_sin_subsecuente,
                                                               None)
    except ValueError as e:
        context.mensaje_excepcion = str(e)
        pass
    else:
        assert False, "NO se lanzó ninguna excepción indicando que la asignatura no tiene una subsecuente."


@step("se emitirá un mensaje manifestando que no es posible identificar a los estudiantes con problemas")
def step_impl(context):
    assert context.mensaje_excepcion == "No es posible identificar a los estudiantes con problemas."