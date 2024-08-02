from ..models.estudiante import Estudiante


class ControlNotas:
    """
        CONTROL NOTAS
        Recibe un estudiante para realizar el control respecto a su promedio.
        Verifica si existe riesgo de bajar en el promedio o si ya lo hizo,
        cuál es su prioridad de atención
    """

    def __init__(self, estudiante: Estudiante):
        self.minimo_aceptable = None
        self.rango_advertencia = 0.5
        self.estudiante = estudiante
        self.promedio = None

    def definir_prioridad_alerta(self):
        incidencias = self.estudiante.numero_incidencias

        if 0 < incidencias < 3:
            self.estudiante.prioridad = "MEDIA"
        elif incidencias >= 3:
            self.estudiante.prioridad = "ALTA"

    @property
    def existe_riesgo(self):
        return 0 < self.promedio - self.minimo_aceptable <= self.rango_advertencia

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
    def promedio(self, value):
        self._promedio = value