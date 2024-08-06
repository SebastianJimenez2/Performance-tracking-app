from collections import defaultdict
from typing import List, Tuple, Dict
from enum import Enum
from collections import defaultdict


def calcular_promedios(evaluaciones) -> List[Tuple[str, float]]:
    resultados = defaultdict(list)
    for evaluacion in evaluaciones:
        resultados[evaluacion.docente].append(evaluacion.calificacion)

    promedios_docentes = []
    for docente, calificaciones in resultados.items():
        promedio = sum(calificaciones) / len(calificaciones)
        promedios_docentes.append((docente, promedio))

    promedios_docentes.sort(key=lambda x: x[1], reverse=True)
    return promedios_docentes


class Asignatura:
    def __init__(self, nombre: str):
        self.nombre = nombre


class TipoEvaluacion(Enum):
    Heteroevaluacion = 1
    Autoevaluacion = 2
    Coevaluacion = 3
    Total = 4

class Docente:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.evaluaciones: List[Evaluacion] = []


class Evaluacion:
    evaluaciones = []

    def __init__(self, nombre: str, tipo_evaluacion: TipoEvaluacion, calificacion: float,
                 asignatura: Asignatura, docente:Docente):
        self.nombre = nombre
        self.tipo_evaluacion = tipo_evaluacion
        self.calificacion = calificacion
        self.asignatura = asignatura
        self.docente = docente
        Evaluacion.evaluaciones.append(self)

    @classmethod
    def docentes_por_promedio(cls, tipo_evaluacion: TipoEvaluacion, asignatura: Asignatura) -> List[
        Tuple[Docente, float]]:
        resultados = defaultdict(list)

        for evaluacion in cls.evaluaciones:
            if evaluacion.tipo_evaluacion == tipo_evaluacion and evaluacion.asignatura == asignatura:
                resultados[evaluacion.docente].append(evaluacion.calificacion)

        promedios_docentes = []

        for docente, calificaciones in resultados.items():
            promedio = sum(calificaciones) / len(calificaciones)
            promedios_docentes.append((docente, promedio))

        # Ordenar por promedio de mayor a menor
        promedios_docentes.sort(key=lambda x: x[1], reverse=True)

        return promedios_docentes

    @classmethod
    def validar_docentes_asignatura(cls, nombre_asignatura: str) -> bool:
        asignatura_docentes = 0

        for evaluacion in cls.evaluaciones:
            if evaluacion.asignatura.nombre == nombre_asignatura:
                asignatura_docentes += 1

        return asignatura_docentes >= 2

    @classmethod
    def sugerencias_docentes(cls) -> List[Tuple[Docente, float]]:
        resultados = defaultdict(list)

        for evaluacion in cls.evaluaciones:
            resultados[evaluacion.docente].append(evaluacion.calificacion)

        promedios_docentes = []

        for docente, calificaciones in resultados.items():
            promedio = sum(calificaciones) / len(calificaciones)
            promedios_docentes.append((docente, promedio))

        # Ordenar por promedio de mayor a menor
        promedios_docentes.sort(key=lambda x: x[1], reverse=True)

        return promedios_docentes



