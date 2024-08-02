from collections import defaultdict
from ..models.asignatura import Asignatura
from ..models.evaluacion import Evaluacion


def docentes_por_promedio(tipo_evaluacion: int, asignatura: Asignatura):
    resultados = defaultdict(list)
    evaluaciones = Evaluacion.objects.filter(tipo_evaluacion=tipo_evaluacion, asignatura=asignatura)
    for evaluacion in evaluaciones:
        resultados[evaluacion.docente].append(evaluacion.calificacion)

    promedios_docentes = []
    for docente, calificaciones in resultados.items():
        promedio = sum(calificaciones) / len(calificaciones)
        promedios_docentes.append((docente, promedio))

    promedios_docentes.sort(key=lambda x: x[1], reverse=True)
    return promedios_docentes


def validar_docentes_asignatura(nombre_asignatura: str):
    asignatura_docentes = Evaluacion.objects.filter(asignatura__nombre=nombre_asignatura).count()
    return asignatura_docentes >= 2


def sugerencias_docentes():
    resultados = defaultdict(list)
    evaluaciones = Evaluacion.objects.all()
    for evaluacion in evaluaciones:
        resultados[evaluacion.docente].append(evaluacion.calificacion)

    promedios_docentes = []
    for docente, calificaciones in resultados.items():
        promedio = sum(calificaciones) / len(calificaciones)
        promedios_docentes.append((docente, promedio))

    promedios_docentes.sort(key=lambda x: x[1], reverse=True)
    return promedios_docentes
