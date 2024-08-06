class EstudianteControlAsistencia:
    def __init__(self, id_estudiante, nombre, numero_incidencias):
        self.id_estudiante = id_estudiante
        self.nombre = nombre
        self.numero_incidencias = numero_incidencias

class AsignaturaControlAsistencia:
    def __init__(self, id_asignatura, nombre, area, nota_minima, total_clases, total_inscritos, total_comprende):
        self.id_asignatura = id_asignatura
        self.nombre = nombre
        self.area = area
        self.nota_minima = nota_minima
        self.total_clases = total_clases
        self.total_inscritos = total_inscritos
        self.total_comprende = total_comprende


class ControlAsistencia:
    def __init__(self, estudiante, asignatura, semana, dia, presente):
        self.estudiante = estudiante
        self.asignatura = asignatura
        self.semana = semana
        self.dia = dia
        self.presente = presente

    def calcular_tasa_asistencia(self, estudiante, asistencias, mes):
        total_clases = sum(1 for a in asistencias if a.estudiante == estudiante and (mes - 1) * 4 < a.semana <= mes * 4)
        clases_asistidas = sum(
            1 for a in asistencias if a.estudiante == estudiante and a.presente and (mes - 1) * 4 < a.semana <= mes * 4)
        return (clases_asistidas / total_clases) * 100 if total_clases > 0 else 0

    @classmethod
    def obtener_estudiantes_en_riesgo(cls, estudiantes, asistencias, mes):
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


