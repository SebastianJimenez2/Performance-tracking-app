from behave import *
from unittest import TestCase


# use_step_matcher("re")


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
    context.historial_notas = HistorialNotas()

    for fila in context.table:
        if float(fila['nota_materia_subsecuente_periodo_actual']) < context.nota_minima:
            valores_notas_finales.append(float(fila['nota_materia_prerequisito_periodo_anterior']))

    for notas in valores_notas_finales:
        context.promedio += notas

    context.promedio /= len(valores_notas_finales)

    assert context.promedio == context.historial_notas.obtener_promedio_histórico(context.asignatura_subsecuente, context.periodo_actual, context.asignatura_prerequisito, context.periodo_anterior)


@step('las siguientes notas finales de los estudiantes que actualmente están cursando la asignatura prerequisito '
      'se encuentren dentro del rango entre "{nota_minima_aprobar}" y el promedio histórico')
def step_impl(context, nota_minima_aprobar):
    context.nota_minima_aprobar = nota_minima_aprobar
    context.estudiantes_en_rango = []

    for fila in context.table:
        if context.nota_minima_aprobar <= float(fila['nota_final_materia_prerequisito']) <= context.promedio:
            context.estudiantes_en_rango = (fila['estudiante'], float(fila['nota_final_materia_prerequisito']))

    notas = [nota for estudiante, nota in context.estudiantes_en_rango]

    assert set(notas) == set(context.historial_notas.obtener_estudiantes_candidatos(context.asignatura_subsecuente,
                                                                                    context.periodo_actual,
                                                                                    context.asignatura_prerequisito,
                                                                                    context.periodo_anterior)['nota'])


@step("se listarán los siguientes estudiantes candidatos a tomar un curso vacacional de bienestar estudiantil")
def step_impl(context):
    assert set(context.estudiantes_en_rango['estudiante']) == set(context.historial_notas.obtener_estudiantes_candidatos(context.asignatura_subsecuente,
                                                                                                                         context.periodo_actual,
                                                                                                                         context.asignatura_prerequisito,
                                                                                                                         context.periodo_anterior)['estudiante'])
