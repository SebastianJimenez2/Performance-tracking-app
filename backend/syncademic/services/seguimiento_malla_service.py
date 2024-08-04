from django.db.models import OuterRef, Avg, Subquery

from syncademic.models.notas import HistorialNotas
from syncademic.models.asignatura import Asignatura
from syncademic.models.periodo import Periodo
from syncademic.models.estudiante import Estudiante


class SeguimientoService:
    def __init__(self, asignatura_prerequisito: str, periodo_actual: str):
        self.asignatura_prerequisito = asignatura_prerequisito
        self.periodo_actual = periodo_actual

    def obtener_estudiantes_candidatos(self):
        try:
            # Se busca la asignatura y periodo actual.
            asignatura_prerequisito = Asignatura.objects.get(nombre=self.asignatura_prerequisito)
            periodo_actual = Periodo.objects.get(nombre=self.periodo_actual)

            # Determinamos a los estudiantes candidatos al curso de verano en base a la nota mínima y promedio histórico.
            # Hay que notar, que la comparación se hace en la línea con:
            # promedio__gte -> "Mayor o igual que..."
            # promedio__lte -> "Menor o igual que..."

            id_estudiantes_candidatos = (
                HistorialNotas.objects
                .filter(id_asignatura=asignatura_prerequisito.id_asignatura)
                .filter(periodo=periodo_actual.id_periodo)
                .values('id_estudiante')
                .annotate(promedio=Subquery(self.obtener_promedio_notas_estudiantes(asignatura_prerequisito, periodo_actual)))
                .filter(promedio__gte=asignatura_prerequisito.nota_minima)
                .filter(promedio__lte=self.obtener_promedio_historico(asignatura_prerequisito, periodo_actual))
            ).values_list('id_estudiante', flat=True)

            # Con los identificadores solo hace falta hacer una consulta en tabla de estudiantes.

            estudiantes_candidatos = Estudiante.objects.filter(
                id_estudiante__in=id_estudiantes_candidatos
            ).annotate(promedio_notas=Subquery(self.obtener_promedio_notas_estudiantes(asignatura_prerequisito, periodo_actual)))

            return estudiantes_candidatos

        except Periodo.DoesNotExist:
            raise ValueError("Periodo actual no encontrado.")
        except Exception as e:
            raise ValueError(
                "No es posible identificar a los estudiantes con problemas, puesto que, la asignatura indicada "
                "no tiene una asignatura subsecuente.")

    def obtener_promedio_historico(self, asignatura_prerequisito, periodo_actual):
        try:
            # Para obtener el promedio histórico, hay que determinar la asignatura subsecuente y el periodo anterior.

            asignatura_subsecuente = Asignatura.objects.get(id_asignatura=asignatura_prerequisito.subsecuente_id)
            periodo_anterior = Periodo.objects.get(id_periodo=periodo_actual.id_periodo - 1)

            # Obtenemos a los estudiantes que tienen menos de la nota mínima en la asignatura subsecuente actual.
            estudiantes_asignatura_subsecuente_periodo_actual = (
                HistorialNotas.objects
                .filter(id_asignatura=asignatura_subsecuente.id_asignatura)
                .filter(periodo=periodo_actual.id_periodo)
                .values('id_estudiante')
                .annotate(promedio_notas=Subquery(
                    self.obtener_promedio_notas_estudiantes(asignatura_subsecuente, periodo_actual)))
                .filter(promedio_notas__lt=asignatura_subsecuente.nota_minima)
            ).values_list('id_estudiante', flat=True)


            if estudiantes_asignatura_subsecuente_periodo_actual.exists():

                # Obtenemos las notas de los mismos estudiantes pero en la materia prerequisito y periodo anterior.
                notas_prerequisito = (
                    HistorialNotas.objects
                    .filter(id_estudiante__in=estudiantes_asignatura_subsecuente_periodo_actual,
                            id_asignatura=asignatura_prerequisito.id_asignatura,
                            periodo=periodo_anterior.id_periodo)
                    .values('id_estudiante')
                    .annotate(promedio_notas=Subquery(
                        self.obtener_promedio_notas_estudiantes(asignatura_prerequisito, periodo_anterior)))
                    .values_list('promedio_notas', flat=True)
                )

                # Sacamos el promedio histórico.
                if notas_prerequisito:
                    promedio_historico = sum(notas_prerequisito) / len(notas_prerequisito)
                else:
                    promedio_historico = 0
            else:
                promedio_historico = 0

            return promedio_historico

        except Asignatura.DoesNotExist:
            raise ValueError("Hay un problema al localizar las asignaturas.")
        except Periodo.DoesNotExist:
            raise ValueError("Periodo actual no encontrado.")
        except Exception as e:
            raise ValueError(f"Se produjo un error al calcular el promedio histórico -> {str(e)}")


    #Este método es útil para obtener el promedio de todas las notas del estudiante.
    def obtener_promedio_notas_estudiantes(self, asignatura, periodo):
        promedio_notas_estudiantes = (
            HistorialNotas.objects
            .filter(id_asignatura=asignatura.id_asignatura,
                    periodo=periodo.id_periodo,
                    id_estudiante=OuterRef('id_estudiante'))
            .annotate(promedio=Avg('nota'))
            .values('promedio')
        )

        return promedio_notas_estudiantes
