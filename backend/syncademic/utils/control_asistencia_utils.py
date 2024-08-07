# Clases de utilidades para control de notas
# Utilizado para Feature 1
# Creado por Christian Hernández

class EstudianteControlAsistencia:
    """ EstudianteControlAsistencia

            Clase auxiliar para recopilar solo la información necesaria del estudiante.

            Attributes:
                id_estudiante
                nombre
                numero_incidencias
    """
    def __init__(self, id_estudiante, nombre, numero_incidencias):
        self.id_estudiante = id_estudiante
        self.nombre = nombre
        self.numero_incidencias = numero_incidencias

class AsignaturaControlAsistencia:
    """ AsignaturaControlAsistencia

                Clase auxiliar para recopilar solo la información necesaria de la asignatura.

                Attributes:
                    id_asignatura
                    nombre
                    area
                    nota_minima
                    total_clases
                    total_inscritos
                    total_comprende
        """
    def __init__(self, id_asignatura, nombre, area, nota_minima, total_clases, total_inscritos, total_comprende):
        self.id_asignatura = id_asignatura
        self.nombre = nombre
        self.area = area
        self.nota_minima = nota_minima
        self.total_clases = total_clases
        self.total_inscritos = total_inscritos
        self.total_comprende = total_comprende


class ControlAsistencia:
    """ AsignaturaControlAsistencia

                    Clase auxiliar para recopilar solo la información necesaria de la asistencia.

                    Attributes:
                        estudainte
                        asignatura
                        semana
                        dia
                        presente
    """
    def __init__(self, estudiante, asignatura, semana, dia, presente):
        self.estudiante = estudiante
        self.asignatura = asignatura
        self.semana = semana
        self.dia = dia
        self.presente = presente

    def calcular_tasa_asistencia(self, estudiante, asistencias, mes):
        """Calcula la tasa de asistencia para un estudiante en un mes específico.

            Esta función calcula el porcentaje de asistencia de un estudiante en un mes dado,
            basado en una lista de registros de asistencia.

            Args:
                estudiante (Estudiante): El objeto del estudiante para el cual se calcula la tasa de asistencia.
                asistencias (QuerySet): Un conjunto de registros de asistencia.
                mes (int): El mes (como número) para el cual se calcula la tasa de asistencia.

            Returns:
                float: La tasa de asistencia del estudiante en el mes especificado como un porcentaje.
                       Si no hay registros de asistencia para el mes dado, retorna 0.
        """
        total_clases = sum(1 for a in asistencias if a.estudiante == estudiante and (mes - 1) * 4 < a.semana <= mes * 4)
        clases_asistidas = sum(
            1 for a in asistencias if a.estudiante == estudiante and a.presente and (mes - 1) * 4 < a.semana <= mes * 4)
        return (clases_asistidas / total_clases) * 100 if total_clases > 0 else 0

    @classmethod
    def obtener_estudiantes_en_riesgo(cls, estudiantes, asistencias, mes):
        """Obtiene la lista de estudiantes en riesgo de abandono basado en su tasa de asistencia.

            Esta función evalúa la tasa de asistencia de cada estudiante para un mes específico y
            determina cuáles estudiantes tienen una tasa de asistencia dentro de un rango considerado
            como de riesgo (0% a 70%).

            Args:
                cls (class): La clase que contiene la función calcular_tasa_asistencia.
                estudiantes (QuerySet): Un conjunto de objetos Estudiante a evaluar.
                asistencias (QuerySet): Un conjunto de registros de asistencia.
                mes (int): El mes (como número) para el cual se evalúa la tasa de asistencia.

            Returns:
                list: Una lista de diccionarios con el nombre y la tasa de asistencia de los estudiantes
                      en riesgo de abandono.
        """
        minimo = 0
        maximo = 70
        estudiantes_en_riesgo = []

        for estudiante in estudiantes:
            tasa_asistencia = cls.calcular_tasa_asistencia(cls, estudiante, asistencias, mes)
            if minimo <= tasa_asistencia <= maximo:
                estudiantes_en_riesgo.append({
                    'nombre': estudiante.nombre,
                    'tasa_asistencia': tasa_asistencia,
                })

        return estudiantes_en_riesgo


