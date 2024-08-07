from behave import *
from syncademic.utils.umbral_comprension import *


# Escenario 1

@step('que el docente de "{asignatura}" ha finalizado la enseñanza del tema "{tema}"')
def step_impl(context, asignatura, tema):
    context.asignatura = asignatura
    context.tema = tema
    context.gestor_evaluacion_tematica = GestorEvaluacionTematica(context.asignatura, context.tema)


@step('se han registrado las siguientes puntuaciones en las evaluaciones para determinar el umbral de comprensión')
def step_impl(context):
    context.evaluaciones = []
    for row in context.table:
        evaluacion = {
            'tipo': row['Tipo de evaluación'],
            'puntuacion_maxima': int(row['Puntuación máxima']),
            'puntuacion_obtenida': int(row['Puntuación obtenida'])
        }
        context.evaluaciones.append(evaluacion)

    context.gestor_evaluacion_tematica.registrar_evaluaciones(context.evaluaciones)


@step('se calcula el umbral de comprensión promedio del tema y es inferior al {umbral:d}%')
def step_impl(context, umbral):
    context.umbral_requerido = int(umbral)
    context.umbral_calculado = context.gestor_evaluacion_tematica.calcular_umbral_comprension()
    assert context.umbral_calculado < context.umbral_requerido


@step('el docente debe tener la capacidad de visualizar el tema sobre un fondo rojo '
      'para determinar la necesidad de implementar actividades de refuerzo')
def step_impl(context):
    alerta = context.gestor_evaluacion_tematica.generar_alerta_refuerzo()
    assert alerta is not None
    assert "refuerzo académico" in alerta


# Escenario 2

@step('que el docente de "{asignatura}" ha concluido la enseñanza del tema "{tema}"')
def step_impl(context, asignatura, tema):
    context.asignatura = asignatura
    context.tema = tema
    context.gestor_evaluacion_tematica = GestorEvaluacionTematica(context.asignatura, context.tema)


@step('el tema "{tema}" no cuenta con todas las evaluaciones necesarias')
def step_impl(context, tema):
    context.gestor_evaluacion_tematica.set_evaluaciones_incompletas()


@step('se intenta determinar el umbral de comprensión alcanzado por los estudiantes')
def step_impl(context):
    try:
        context.gestor_evaluacion_tematica.calcular_umbral_comprension()
    except ValueError as e:
        context.error_mensaje = str(e)


@step('la fila correspondiente a "{tema}" aparecerá destacada en blanco en el informe')
def step_impl(context, tema):
    informe = context.gestor_evaluacion_tematica.generar_informe()
    assert informe.get_estilo_fila(tema) == 'blanco'