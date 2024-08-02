from collections import defaultdict
from typing import List, Tuple



def _calcular_promedios(evaluaciones) -> List[Tuple[str, float]]:
    resultados = defaultdict(list)
    for evaluacion in evaluaciones:
        resultados[evaluacion.docente].append(evaluacion.calificacion)

    promedios_docentes = []
    for docente, calificaciones in resultados.items():
        promedio = sum(calificaciones) / len(calificaciones)
        promedios_docentes.append((docente, promedio))

    promedios_docentes.sort(key=lambda x: x[1], reverse=True)
    return promedios_docentes
