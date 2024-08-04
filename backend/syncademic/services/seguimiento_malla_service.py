from ..models.notas import HistorialNotas
from ..models.asignatura import Asignatura
from ..models.periodo import Periodo
from ..models.estudiante import Estudiante


class SeguimientoService:
    def __init__(self, asignatura_prerequisito: str, periodo_actual: str):
        self.asignatura_prerequisito = asignatura_prerequisito
        self.periodo_actual = periodo_actual

    def obtener_promedio_historico(self):
        try:
            asignatura_prerequisito = Asignatura.objects.get(nombre=self.asignatura_prerequisito)
            asignatura_subsecuente = Asignatura.objects.get(subsecuente=asignatura_prerequisito.subsecuente)
            periodo_actual = Periodo.objects.get(nombre=self.periodo_actual)
            periodo_anterior = Periodo.objects.get(id_periodo=periodo_actual.id_periodo-1)

            estudiantes_asignatura_subsecuente_periodo_actual = (
                HistorialNotas.objects
                .filter(id_asignatura=asignatura_subsecuente.id_asignatura)
                .filter(periodo=periodo_actual.id_periodo)
                .filter(nota__lt=asignatura_subsecuente.nota_minima)
            )

            if estudiantes_asignatura_subsecuente_periodo_actual.exists():
                ids_estudiantes = estudiantes_asignatura_subsecuente_periodo_actual.values_list('id_estudiante',
                                                                                                flat=True)

                notas_prerequisito = HistorialNotas.objects.filter(
                    id_estudiante__in=ids_estudiantes,
                    id_asignatura=asignatura_prerequisito.id_asignatura,
                    periodo=periodo_anterior.id_periodo
                ).values_list('nota', flat=True)

                if notas_prerequisito:
                    promedio_historico = sum(notas_prerequisito) / len(notas_prerequisito)
                else:
                    promedio_historico = 0
            else:
                promedio_historico = 0

            return promedio_historico

        except Asignatura.DoesNotExist:
            raise ValueError(
                "Hay un problema al localizar las asignaturas.")
        except Periodo.DoesNotExist:
            raise ValueError("Periodo actual no encontrado.")
        except Exception as e:
            raise ValueError(f"Se produjo un error al calcular el promedio histórico -> {str(e)}")

    def obtener_estudiantes_candidatos(self):
        try:
            asignatura_prerequisito = Asignatura.objects.get(nombre=self.asignatura_prerequisito)
            periodo_actual = Periodo.objects.get(nombre=self.periodo_actual)

            id_estudiantes_candidatos = (
                HistorialNotas.objects
                .filter(id_asignatura=asignatura_prerequisito.id_asignatura)
                .filter(nota__lt=self.obtener_promedio_historico())
                .filter(periodo=periodo_actual.id_periodo)
            ).values_list('id_estudiante', flat=True)

            estudiantes_candidatos = Estudiante.objects.filter(
                id_estudiante__in=id_estudiantes_candidatos
            )

            return estudiantes_candidatos

        except Asignatura.DoesNotExist:
            raise ValueError(
                "No es posible identificar a los estudiantes con problemas, puesto que, la asignatura indicada "
                "no tiene una asignatura subsecuente.")
        except Periodo.DoesNotExist:
            raise ValueError("Periodo actual no encontrado.")
        except Exception as e:
            raise ValueError(f"Se produjo un error al obtener los estudiantes candidatos -> {str(e)}")
