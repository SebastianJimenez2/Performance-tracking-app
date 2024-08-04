from behave import *
from faker import Faker
from backend.syncademic.models.asignatura import Asignatura
from backend.syncademic.models.docente import Docente
from backend.syncademic.models.tipo_evaluacion_docente import TipoEvaluacion
from backend.syncademic.models.evaluacion_docente import Evaluacion
from backend.syncademic.services.evaluacion_docente_service import evaluacion_docente_service

fake = Faker()


# Escenario 1
@step('que existen al menos dos docentes que han impartido la asignatura "{nombre_asignatura}"')
def step_impl(context, nombre_asignatura):
    context.asignatura = Asignatura.objects.create(
        nombre=nombre_asignatura,
        area="Ciencias Exactas",
        nota_minima=6.00,
        total_clases=40,
        total_inscritos=120,
        total_comprende=90,
        prerequisito=None,
        subsecuente=None
    )

    context.docente1 = Docente.objects.create(id_docente=1, nombre=fake.name(), correo=fake.email(), estado="estado")
    context.docente2 = Docente.objects.create(id_docente=2, nombre=fake.name(), correo=fake.email(), estado="estado")

    Evaluacion.objects.create(
        tipo_evaluacion=TipoEvaluacion.Heteroevaluacion,
        calificacion=fake.random_int(min=70, max=100),
        asignatura=context.asignatura,
        docente=context.docente1
    )
    Evaluacion.objects.create(
        tipo_evaluacion=TipoEvaluacion.Heteroevaluacion,
        calificacion=fake.random_int(min=70, max=100),
        asignatura=context.asignatura,
        docente=context.docente2
    )

    # Obtén las evaluaciones y calcula la cantidad de docentes
    evaluaciones = evaluacion_docente_service.get_evaluaciones_asignatura(context.asignatura.id_asignatura)
    context.val_cantidad_docentes = evaluaciones.values('docente').distinct().count()

    if context.val_cantidad_docentes < 2:
        assert False, "NO SE TIENE LA CANTIDAD SUFICIENTE DE DOCENTES"


@step('se solicita identificar el docente con mayor calificación promedio en "{tipo_evaluacion}"')
def step_impl(context, tipo_evaluacion):
    tipo = TipoEvaluacion[tipo_evaluacion]
    context.result_docentes_promedios = evaluacion_docente_service.get_mejores_docentes_por_asignatura(tipo,
                                                                                                       context.asignatura)


@step("se presenta el listado de docentes en orden de mayor a menor con respecto a su calificación")
def step_impl(context):
    print("------------------------------------------------------")
    print("Listado de mejores docentes en asignatura solicitada")
    for docente, promedio in context.result_docentes_promedios:
        print(f"Docente: {docente.nombre}, Promedio: {promedio:.2f}")


@step('que existe uno o ningún docente que ha impartido la asignatura "{nombre_asignatura}"')
def step_impl(context, nombre_asignatura):
    context.asignatura2 = Asignatura.objects.create(
        nombre=nombre_asignatura,
        area="Ciencias Exactas",
        nota_minima=6.00,
        total_clases=40,
        total_inscritos=120,
        total_comprende=90,
        prerequisito=None,
        subsecuente=None
    )

    context.docente3 = Docente.objects.create(id_docente=3, nombre=fake.name(), correo=fake.email(), estado="estado")

    Evaluacion.objects.create(
        tipo_evaluacion=TipoEvaluacion.Heteroevaluacion,
        calificacion=fake.random_int(min=70, max=100),
        asignatura=context.asignatura2,
        docente=context.docente3
    )

    context.val_cantidad_docentes2 = Evaluacion.objects.filter(asignatura=context.asignatura2).values(
        'docente').distinct().count()

    if context.val_cantidad_docentes2 >= 2:
        assert False, "CANTIDAD DE DOCENTES MAYOR O IGUAL A 2"


@step("se solicita identificar docentes afines a la asignatura")
def step_impl(context):
    context.result_docentes2 = evaluacion_docente_service.get_mejores_evaluaciones()


@step('se presenta un listado de sugerencias de docentes con mayor calificación promedio total"')
def step_impl(context):
    print("------------------------------------------------------")
    print("Sugerencia de docentes")
    for docente, promedio in context.result_docentes2:
        print(f"Docente: {docente.nombre}, Promedio: {promedio:.2f}")
