from behave import *
from app.modelos import *
from faker import Faker


@step('el docente visualiza su progreso de la semana {semana_actual} en base a que {temas_marcados}')
def step_visualizar_progreso(context, semana_actual, temas_marcados):
    faker = Faker("es_ES")
    nombre_docente = faker.name()
    context.docente = Docente(nombre_docente)
    context.cronograma = Cronograma("Matematicas", "gr1")
    context.semanas = [1, 1, 2]
    context.temas = ["Introducción", "Fundamentos", "Conceptos avanzados"]
    context.cronograma.agregar_tema(context.temas)
    context.cronograma.agregar_semanas(context.semanas)
    context.docente.registrar_cronograma(context.cronograma)

    context.id_tema = context.docente.marcar_tema_visto(context.cronograma.nombre_materia,
                                                        context.cronograma.grupo)
    context.id_tema = context.docente.marcar_tema_visto(context.cronograma.nombre_materia,
                                                        context.cronograma.grupo)

    context.semana_actual = semana_actual

    context.progreso = context.docente.visualizar_progreso(int(context.semana_actual),
                                                           context.cronograma.nombre_materia, context.cronograma.grupo)

    #print(context.progreso)
    #print(temas_marcados)
    assert context.progreso == temas_marcados


@step('se visualiza un progreso {estado} respecto a la proyección ideal')
def step_verificar_progreso(context, estado):
    faker = Faker("es_ES")
    nombre_docente = faker.name()
    context.docente = Docente(nombre_docente)
    context.cronograma = Cronograma("Matematicas", "gr1")
    context.semanas = [1, 1, 2]
    context.temas = ["Introducción", "Fundamentos", "Conceptos avanzados"]
    context.cronograma.agregar_tema(context.temas)
    context.cronograma.agregar_semanas(context.semanas)
    context.docente.registrar_cronograma(context.cronograma)

    context.id_tema = context.docente.marcar_tema_visto(context.cronograma.nombre_materia,
                                                        context.cronograma.grupo)
    context.id_tema = context.docente.marcar_tema_visto(context.cronograma.nombre_materia,
                                                        context.cronograma.grupo)

    context.aux = context.docente.visualizar_progreso(int(context.semana_actual),
                                                      context.cronograma.nombre_materia, context.cronograma.grupo)

    assert context.docente.estado == estado
