from behave import *
from syncademic.services.seguimiento_malla_service import SeguimientoService
# use_step_matcher("re")

#Escenario 01
@step('que el docente desea conocer el promedio histórico con las siguientes notas finales de los estudiantes que '
      'cursaron "{asignatura_prerequisito}" en el periodo "{periodo_anterior}", y obtuvieron una nota final menor '
      'a "{nota_minima:f}" en "{asignatura_subsecuente}" en el periodo {periodo_actual}')
def step_impl(context, asignatura_prerequisito, periodo_anterior, nota_minima, asignatura_subsecuente, periodo_actual):
    context.asignatura_prerequisito = asignatura_prerequisito
    context.periodo_anterior = periodo_anterior
    context.nota_minima = nota_minima
    context.asignatura_subsecuente = asignatura_subsecuente
    context.periodo_actual = periodo_actual

    valores_notas_finales = []
    context.promedio = 0.0
    context.seguimiento_service = SeguimientoService(context.asignatura_prerequisito, context.periodo_actual)

    for fila in context.table:
        if float(fila['nota_materia_subsecuente_periodo_actual']) < context.nota_minima:
            valores_notas_finales.append(float(fila['nota_materia_prerequisito_periodo_anterior']))

    for notas in valores_notas_finales:
        context.promedio += notas

    context.promedio /= len(valores_notas_finales)

    assert context.promedio == context.seguimiento_service.obtener_promedio_historico()


@step('las siguientes notas finales de los estudiantes que actualmente están cursando la asignatura prerequisito '
      'se encuentren dentro del rango entre "{nota_minima_aprobar}" y el promedio histórico')
def step_impl(context, nota_minima_aprobar):
    context.nota_minima_aprobar = nota_minima_aprobar
    context.estudiantes_en_rango = []

    for fila in context.table:
        if context.nota_minima_aprobar <= float(fila['nota_final_materia_prerequisito']) <= context.promedio:
            context.estudiantes_en_rango = (fila['estudiante'], float(fila['nota_final_materia_prerequisito']))


    assert len(context.estudiantes_en_rango) == len(context.seguimiento_service.obtener_estudiantes_candidatos())


@step("se listarán los siguientes estudiantes candidatos a tomar un curso vacacional de bienestar estudiantil")
def step_impl(context):
    assert set(context.estudiantes_en_rango['estudiante']) == set(context.seguimiento_service.obtener_estudiantes_candidatos().values('nombre'))

#Escenario 02

@step('que el docente desea saber el promedio histórico de notas finales de los estudiantes de la materia "{asignatura_sin_subsecuente}" en el periodo actual "{periodo_actual}"')
def step_impl(context, asignatura_sin_subsecuente, periodo_actual):
    context.asignatura_sin_subsecuente = asignatura_sin_subsecuente
    context.periodo_actual = periodo_actual

    context.seguimiento_service = SeguimientoService(context.asignatura_prerequisito, context.periodo_actual)

    assert 0 == context.seguimiento_service.obtener_promedio_historico()



@step("se determine que no es posible identificar a los estudiantes con problemas debido a que la asignatura indicada no tiene una asignatura subsecuente")
def step_impl(context):
    try:
        context.seguimiento_service.obtener_estudiantes_candidatos()
    except ValueError as e:
        context.mensaje_excepcion = str(e)
        pass
    else:
        assert False, "NO se lanzó ninguna excepción indicando que la asignatura no tiene una subsecuente."


@step("se emitirá un mensaje manifestando la imposibilidad")
def step_impl(context):
    assert context.mensaje_excepcion == "No es posible identificar a los estudiantes con problemas, puesto que, la asignatura indicada no tiene una asignatura subsecuente."
