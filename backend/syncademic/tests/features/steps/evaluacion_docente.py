from behave import *
from faker import Faker
from syncademic.utils.evaluacion_docente_utils import *

fake = Faker()


# Escenario 1
@step('que existen dos o más docentes que han impartido la asignatura "{nombre_asignatura}"')
def step_impl(context, nombre_asignatura):
    context.asignatura = Asignatura(nombre_asignatura)
    context.docente1 = Docente(fake.name())
    context.docente2 = Docente(fake.name())
    context.eval1 = Evaluacion(fake.word(), TipoEvaluacion.Heteroevaluacion, fake.random_int(min=70, max=100),
                       context.asignatura, context.docente1)
    context.eval2 = Evaluacion(fake.word(), TipoEvaluacion.Heteroevaluacion, fake.random_int(min=70, max=100),
                       context.asignatura, context.docente2)

    context.val_cantidad_docentes = Evaluacion.validar_docentes_asignatura(context.asignatura.nombre)

    if ~context.val_cantidad_docentes:
        assert "NO SE TIENE LA CANTIDAD SUFICIENTE DE DOCENTES"


@step('se solicita identificar el docente con mayor calificación promedio en "{tipo_evaluacion}"')
def step_impl(context, tipo_evaluacion):
    tipo = TipoEvaluacion[tipo_evaluacion]
    context.result_docentes_promedios = Evaluacion.docentes_por_promedio(tipo, context.asignatura)


@step("se presenta el listado de docentes en orden de mayor a menor con respecto a su calificación")
def step_impl(context):
    print("------------------------------------------------------")
    print("Listado de mejores docentes en asignatura solicitada")
    for docente, promedio in context.result_docentes_promedios:
        print(f"Docente: {docente.nombre}, Promedio: {promedio:.2f}")


@step('que existe uno o ningún docente que ha impartido la asignatura "{nombre_asignatura}"')
def step_impl(context, nombre_asignatura):
    context.docente3 = Docente(fake.name())
    context.asignatura2 = Asignatura(nombre_asignatura)
    context.eval3 = Evaluacion(fake.word(), TipoEvaluacion.Heteroevaluacion, fake.random_int(min=70, max=100),
                               context.asignatura2, context.docente3)

    context.val_cantidad_docentes2 = Evaluacion.validar_docentes_asignatura(context.asignatura2.nombre)

    if context.val_cantidad_docentes2:
        assert "CANTIDAD DE DOCENTES MAYOR O IGUAL A 2"


@step("se solicita identificar docentes afines a la asignatura")
def step_impl(context):

    context.result_docentes2 = Evaluacion.sugerencias_docentes()


@step('se presenta un listado de sugerencias de docentes con mayor calificación promedio total"')
def step_impl(context):
    print("------------------------------------------------------")
    print("Sugerencia de docentes")
    for docente, promedio in context.result_docentes2:
        print(f"Docente: {docente.nombre}, Promedio: {promedio:.2f}")
