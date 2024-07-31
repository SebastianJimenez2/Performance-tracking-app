from behave import *
from unittest import TestCase


# use_step_matcher("re")


@step('que el docente desea conocer el promedio histórico con las siguientes notas finales de los estudiantes que '
      'cursaron "{asignatura_prerequisito}" en el periodo "{periodo_anterior}", y obtuvieron una nota final menor '
      'a "{nota_minima:f}" en "{asignatura_subsecuente}" en el periodo {periodo_actual}')
def step_impl(context, asignatura_prerequisito, periodo_anterior, periodo_actual, nota_minima, asignatura_subsecuente):
    valores_notas_finales = []
    context.promedio = 0.0
    context.curriculum_general = CurriculumGeneral()

    for fila in context.table:
        if float(fila['nota_materia_subsecuente_periodo_actual']) < nota_minima:
            valores_notas_finales.append(float(fila['nota_materia_prerequisito_periodo_anterior']))

    for notas in valores_notas_finales:
        context.promedio += notas

    context.promedio /= len(valores_notas_finales)

    assert context.promedio == context.curriculum_geneal.obtener_promedio_histórico(asignatura_prerequisito,
                                                                            periodo_anterior)


@step('las siguientes notas finales de los estudiante que actualmente están cursando "{asignatura_prerequisito}" '
      'se encuentre dentro del rango entre "{nota_minima_aprobar}" y el promedio histórico')
def step_impl(context, asignatura_prerequisito, nota_minima_aprobar):
    context.estudiantes_en_rango = []

    for fila in context.table:
        if nota_minima_aprobar<=float(fila['nota_final_materia_prerequisito'])<=context.promedio:
            context.estudiantes_en_rango = (fila['estudiante'], float(fila['nota_final_materia_prerequisito']))

    notas = [nota for estudiante, nota in context.estudiantes_en_rango]

    assert set(notas) == context.curriculum_general.obtener_estudiantes_candidatos(asignatura_prerequisito, )['notas']


@step("se listarán los siguientes estudiantes candidatos a tomar un curso vacacional de bienestar estudiantil")
def step_impl(context):
    context.curriculum_geneal = CurriculumGeneral()

    estudiantes_candidatos = context.curriculum_geneal.obtener_estudiantes_candidatos()

    estudiantes_listados = [estudiante for estudiante, nota in context.nota_final_por_estudiantes]

    assert set(estudiantes_candidatos) == set(estudiantes_listados)
