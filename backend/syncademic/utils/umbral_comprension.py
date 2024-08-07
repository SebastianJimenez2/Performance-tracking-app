class Docente:
    def __init__(self, nombre, asignatura):
        self.nombre = nombre
        self.asignatura = asignatura


class Tema:
    def __init__(self, nombre, asignatura):
        self.nombre = nombre
        self.asignatura = asignatura
        self.evaluaciones = []


class Evaluacion:
    def __init__(self, tipo, puntuacion_maxima, puntuacion_obtenida):
        self.tipo = tipo
        self.puntuacion_maxima = puntuacion_maxima
        self.puntuacion_obtenida = puntuacion_obtenida


class Informe:
    def __init__(self):
        self.filas = {}

    def agregar_fila(self, tema, estilo):
        self.filas[tema] = estilo

    def get_estilo_fila(self, tema):
        return self.filas.get(tema, '')


class GestorEvaluacionTematica:
    def __init__(self, asignatura, tema):
        self.asignatura = asignatura
        self.tema = Tema(tema, asignatura)
        self.evaluaciones_completas = True

    def registrar_evaluaciones(self, evaluaciones):
        for eval_data in evaluaciones:
            evaluacion = Evaluacion(eval_data['tipo'], eval_data['puntuacion_maxima'], eval_data['puntuacion_obtenida'])
            self.tema.evaluaciones.append(evaluacion)

    def set_evaluaciones_incompletas(self):
        self.evaluaciones_completas = False

    def calcular_umbral_comprension(self):
        if not self.evaluaciones_completas:
            raise ValueError("No se pueden calcular los umbrales de comprensión debido a la falta de evaluaciones.")

        total_porcentaje = 0
        for evaluacion in self.tema.evaluaciones:
            porcentaje = (evaluacion.puntuacion_obtenida / evaluacion.puntuacion_maxima) * 100
            total_porcentaje += porcentaje

        return total_porcentaje / len(self.tema.evaluaciones) if self.tema.evaluaciones else 0

    def generar_alerta_refuerzo(self):
        return f"Se sugiere implementar refuerzo académico para el tema '{self.tema.nombre}' en la asignatura '{self.asignatura}'."

    def generar_informe(self):
        informe = Informe()
        if not self.evaluaciones_completas:
            informe.agregar_fila(self.tema.nombre, 'blanco')
        else:
            informe.agregar_fila(self.tema.nombre, 'normal')
        return informe