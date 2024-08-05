from behave import *
from faker import Faker
from syncademic.utils import obtener_estudiantes_en_riesgo, EstudianteControlAsistencia, AsignaturaControlAsistencia, ControlAsistencia

use_step_matcher("parse")

fake = Faker("es")

@step("un estudiante con tasa de asistencia {tasa_asistencia} % mensual")
def step_impl(context, tasa_asistencia):
    context.tasa_asistencia = float(tasa_asistencia)
    context.estudiantes = [
        EstudianteControlAsistencia(id_estudiante=1, nombre=fake.name(), numero_incidencias=0),
        EstudianteControlAsistencia(id_estudiante=2, nombre=fake.name(), numero_incidencias=0),
    ]
    context.asignatura = AsignaturaControlAsistencia(
        id_asignatura=1, nombre='Matemáticas', area='Ciencias', nota_minima=5,
        total_clases=20, total_inscritos=2, total_comprende=2
    )
    context.asistencias = []
    for estudiante in context.estudiantes:
        for semana in range(1, 5):  # Assuming 4 weeks in a month
            asistencia = ControlAsistencia(
                estudiante=estudiante,
                asignatura=context.asignatura,
                semana=semana,
                dia='Lunes',
                presente=True
            )
            context.asistencias.append(asistencia)

@step("la tasa de asistencia se encuentre entre {minimo} % y {maximo} %")
def step_impl(context, minimo, maximo):
    context.minimo = float(minimo)
    context.maximo = float(maximo)
    context.estudiantes_en_riesgo = obtener_estudiantes_en_riesgo(context.estudiantes, context.asistencias, 1)

@step("se marca al estudiante en riesgo {riesgo} de abandono alertando al profesor")
def step_impl(context, riesgo):
    riesgo = 'alto' if context.tasa_asistencia < context.minimo or context.tasa_asistencia > context.maximo else 'bajo'
    for estudiante in context.estudiantes:
        asistencias_estudiante = [a for a in context.asistencias if a.estudiante == estudiante]
        tasa_asistencia = (sum(a.presente for a in asistencias_estudiante) / len(asistencias_estudiante)) * 100
        if context.minimo > tasa_asistencia <= context.maximo:
            assert riesgo == 'alto', f"Se esperaba que el riesgo fuera 'alto', pero se encontró '{riesgo}'"
        else:
            assert riesgo == 'bajo', f"Se esperaba que el riesgo fuera 'bajo', pero se encontró '{riesgo}'"

@step("él decide {posible_notificacion}notificar a bienestar estudiantil.")
def step_impl(context, posible_notificacion):
    context.posible_notificacion = posible_notificacion.strip()
    if context.posible_notificacion == 'sí':
        assert 'sí' == context.posible_notificacion, "Se esperaba notificación a bienestar estudiantil."
    elif context.posible_notificacion == 'no':
        assert 'no' == context.posible_notificacion, "No se esperaba notificación a bienestar estudiantil."
