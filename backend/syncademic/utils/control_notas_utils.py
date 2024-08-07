class EstadoEstudiante:
    """
            EstadoEstudiante
            Clase auxiliar para recopilar solo la información necesaria del estudiante
            para realizar la verificación de incidencias por bajas calificaciones.

            Atributos: nombre, email, numero_incidencias, prioridad
    """

    def __init__(self, nombre: str, email: str):
        self.nombre = nombre
        self.email = email
        self.numero_incidencias = None
        self.prioridad = None

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

    @property
    def numero_incidencias(self):
        return self._numero_incidencias

    @numero_incidencias.setter
    def numero_incidencias(self, numero_incidencias):
        self._numero_incidencias = numero_incidencias

    @property
    def prioridad(self):
        return self._prioridad

    @prioridad.setter
    def prioridad(self, prioridad):
        self._prioridad = prioridad


class ControlNotas:
    """
        CONTROL NOTAS
        Recibe un estudiante para realizar el control respecto a su promedio.
        Verifica si existe riesgo de bajar en el promedio o si ya lo hizo,
        cuál es su prioridad de atención
    """

    def __init__(self, estudiante: EstadoEstudiante):
        self.minimo_aceptable: float = 0.0
        self.rango_advertencia = 0.5
        self.estudiante = estudiante
        self.promedio: float = 0.0

    def definir_prioridad_alerta(self):
        incidencias = self.estudiante.numero_incidencias

        if 0 < incidencias < 3:
            self.estudiante.prioridad = "MEDIA"
        elif incidencias >= 3:
            self.estudiante.prioridad = "ALTA"
        elif incidencias == 0 and not self.existe_riesgo:
            self.estudiante.prioridad = "BAJA"

    @property
    def existe_riesgo(self):
        return 0 < float(self.promedio) - float(self.minimo_aceptable) <= self.rango_advertencia

    @property
    def existe_incidencia(self):
        return self.promedio < self.minimo_aceptable

    @property
    def estudiante(self):
        return self._estudiante

    @property
    def rango_advertencia(self):
        return self._rango_advertencia

    @property
    def minimo_aceptable(self):
        return self._minimo_aceptable

    @property
    def promedio(self):
        return self._promedio

    @rango_advertencia.setter
    def rango_advertencia(self, value):
        self._rango_advertencia = value

    @minimo_aceptable.setter
    def minimo_aceptable(self, value):
        self._minimo_aceptable = value

    @estudiante.setter
    def estudiante(self, value):
        self._estudiante = value

    @promedio.setter
    def promedio(self, value) -> float:
        self._promedio = value
