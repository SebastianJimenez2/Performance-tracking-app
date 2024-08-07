from ..exceptions.not_found import ObjectNotFound
from ..models.estudiante import Estudiante
from ..models.asistencia import Asistencia


class AsistenciaService:
    """ Servicio de asistencias

        Attributes:
             id_asignatura
             periodo
             grupo

        Utilizado para Feature 1
        Creado por Christian Hernández
    """

    @staticmethod
    def calcular_tasa_asistencia(estudiante, mes):
        """
            Calcula la tasa de asistencia para un estudiante en un mes especifico

            Segun su asistencia y las clases totales recibidas en el mes

            Parameters:
                estudiante (Estudiante): El estudiante para el cual calcular la tasa de asistencia.
                mes (int): El mes para el cual calcular la tasa de asistencia (1 a 12).

            Return:
                float: La tasa de asistencia en porcentaje.
        """
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
        """
            Obtiene la lista de estudiantes en riesgo de acuerdo a su tasa de asistencia.

            Esta función evalúa la tasa de asistencia de todos los estudiantes para un mes específico.
            Si la tasa de asistencia de un estudiante se encuentra entre los valores de 'minimo' y 'maximo',
            se considera en riesgo y se agrega a la lista de estudiantes en riesgo.

            Args:
                mes (int): El mes para el cual calcular la tasa de asistencia (1 a 12).

            Returns:
                list: Una lista de diccionarios, cada uno con el nombre del estudiante y su tasa de asistencia.
        """
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
        """Obtiene la lista de estudiantes con sus identificadores y nombres.

            Esta función consulta todos los registros de la tabla Estudiante y devuelve una lista
            de diccionarios, cada uno con el id del estudiante y su nombre. Si no se encuentran
            registros, se lanza una excepción de tipo ObjectNotFound.

            Returns:
                QuerySet: Una lista de diccionarios, cada uno con el id del estudiante y su nombre.

            Raises:
                ObjectNotFound: Si no se encuentran registros en la tabla Estudiante.
        """
        estudiantes = Estudiante.objects.filter().values('id_estudiante', 'nombre_estudiante')
        if estudiantes is None:
            raise ObjectNotFound(Asistencia._meta.model_name,
                                 "No se han encontrado registros para los parámetros dados")
        else:
            return estudiantes

    @staticmethod
    def actualizar_asistencia(estudiante_id, asignatura_id, semana, dia, presente):
        """
            Actualiza o crea un registro de asistencia para un estudiante en una asignatura específica.

            Esta función busca un registro de asistencia basado en el estudiante, la asignatura, la semana y el día.
            Si el registro existe, actualiza el campo 'presente' con el valor proporcionado. Si no existe, crea un
            nuevo registro con los valores proporcionados.

            Parameters:
                estudiante_id (int):
                asignatura_id (int):
                semana (int):
                dia (str):
                presente (bool): (True si está presente, False si está ausente).

            Returns:
                tuple: Una tupla que contiene el objeto de asistencia y un booleano que indica si el registro fue creado (True) o actualizado (False).
        """
        asistencia, created = Asistencia.objects.update_or_create(
            estudiante_id=estudiante_id,
            asignatura_id=asignatura_id,
            semana=semana,
            dia=dia,
            defaults={'presente': presente}
        )
        return asistencia, created
