from ..exceptions.not_found import ObjectNotFound
from ..models.estudiante import Estudiante
from ..models.asistencia import Asistencia


class AsistenciaService:

    @staticmethod
    def calcular_tasa_asistencia(estudiante, mes):
        # Calcula la tasa de asistencia para un estudiante en un mes específico
        total_clases = Asistencia.objects.filter(
            estudiante=estudiante,
            semana__gte=mes * 4 - 3,
            semana__lte=mes * 4
        ).count()
        clases_asistidas = Asistencia.objects.filter(
            estudiante=estudiante,
            presente=True,
            semana__gte=mes * 4 - 3,
            semana__lte=mes * 4
        ).count()
        return (clases_asistidas / total_clases) * 100 if total_clases > 0 else 0

    @staticmethod
    def obtener_estudiantes_en_riesgo(mes):
        minimo = 0
        maximo = 70
        estudiantes_en_riesgo = []

        for estudiante in Estudiante.objects.all():
            tasa_asistencia = AsistenciaService.calcular_tasa_asistencia(estudiante, mes)
            if minimo <= tasa_asistencia <= maximo:
                estudiantes_en_riesgo.append({
                    'nombre': estudiante.nombre_estudiante,
                    'tasa_asistencia': tasa_asistencia,
                })

        return estudiantes_en_riesgo

    @staticmethod
    def obtener_lista_estudiantes():
        estudiantes = Estudiante.objects.filter().values('id_estudiante', 'nombre_estudiante')
        if estudiantes is None:
            raise ObjectNotFound(Asistencia._meta.model_name,
                                 "No se han encontrado registros para los parámetros dados")
        else:
            return estudiantes

    @staticmethod
    def actualizar_asistencia(estudiante_id, asignatura_id, semana, dia, presente):
        asistencia, created = Asistencia.objects.update_or_create(
            estudiante_id=estudiante_id,
            asignatura_id=asignatura_id,
            semana=semana,
            dia=dia,
            defaults={'presente': presente}
        )
        return asistencia, created
