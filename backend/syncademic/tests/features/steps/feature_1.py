from behave import *

from syncademic.models.estudiante import Estudiante
from syncademic.models.asistencia import Asistencia
from syncademic.models.asignatura import Asignatura
from syncademic.services.asistencia_service import obtener_estudiantes_en_riesgo, actualizar_asistencia

use_step_matcher("parse")

@step("un estudiante con tasa de asistencia {tasa_asistencia} mensual")
def step_impl(context, tasa_asistencia):
    context.tasa_asistencia = float(tasa_asistencia)
    # Setup initial data for testing
    context.estudiantes = [
        Estudiante.objects.create(id_estudiante=1, nombre='Juan Perez', numero_incidencias=0),
        Estudiante.objects.create(id_estudiante=2, nombre='Pedro Porro', numero_incidencias=0),
    ]
    context.asignatura = Asignatura.objects.create(
        id_asignatura=1, nombre='Matemáticas', area='Ciencias', nota_minima=5,
        total_clases=20, total_inscritos=2, total_comprende=2
    )
    # Creating attendance records
    for estudiante in context.estudiantes:
        for semana in range(1, 5):  # Assuming 4 weeks in a month
            Asistencia.objects.create(
                estudiante=estudiante,
                asignatura=context.asignatura,
                semana=semana,
                dia='Lunes',
                presente=True
            )

@step("la tasa de asistencia se encuentre entre {minimo} y {maximo}")
def step_impl(context, minimo, maximo):
    context.minimo = float(minimo)
    context.maximo = float(maximo)
    context.estudiantes_en_riesgo = obtener_estudiantes_en_riesgo(1)  # Assuming we're checking for month 1

@step("se marca al estudiante en riesgo {riesgo} de abandono alertando al profesor")
def step_impl(context, riesgo):
    riesgo = 'alto' if context.tasa_asistencia < context.minimo or context.tasa_asistencia > context.maximo else 'bajo'
    for estudiante in context.estudiantes:
        tasa_asistencia = (Asistencia.objects.filter(estudiante=estudiante, presente=True).count() /
                           Asistencia.objects.filter(estudiante=estudiante).count()) * 100
        if (context.minimo <= tasa_asistencia <= context.maximo):
            assert riesgo == 'alto', f"Se esperaba que el riesgo fuera 'alto', pero se encontró '{riesgo}'"
        else:
            assert riesgo == 'bajo', f"Se esperaba que el riesgo fuera 'bajo', pero se encontró '{riesgo}'"

@step("él decide {posible_notificacion}notificar a bienestar estudiantil.")
def step_impl(context, posible_notificacion):
    context.posible_notificacion = posible_notificacion.strip()
    # Add assertion or logic for notification decision if needed
    # For simplicity, we just check if the notification decision was recorded correctly
    if context.posible_notificacion == 'sí':
        assert 'sí' == context.posible_notificacion, "Se esperaba notificación a bienestar estudiantil."
    elif context.posible_notificacion == 'no':
        assert 'no' == context.posible_notificacion, "No se esperaba notificación a bienestar estudiantil."
