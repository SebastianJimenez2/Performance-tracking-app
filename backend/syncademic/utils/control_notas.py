class ControlNotas:

    def __init__(self, minimo_aceptable=7.0, rango_advertencia=0.5, promedio=0.0):
        self.minimo_aceptable = minimo_aceptable
        self.rango_advertencia = rango_advertencia
        self.promedio = promedio
        self.mensajes = {
            'advertencia': 'El estudiante está cerca del mínimo aceptable del promedio.',
            'alerta': 'El estudiante ha bajado del mínimo aceptable del promedio.',
            'respuesta': 'No existen alertas'
        }

    def definir_prioridad_alerta(self, incidencias: int):
        alerta = {'mensaje': self.mensajes['alerta']}
        if 0 < incidencias < 3:
            alerta['prioridad'] = "MEDIA"
            return alerta
        elif incidencias >= 3:
            alerta['prioridad'] = "ALTA"
            return alerta

        return None

    @property
    def existe_riesgo(self):
        return 0 < self.promedio - self.minimo_aceptable <= self.rango_advertencia

    @property
    def existe_incidencia(self):
        return self.promedio < self.minimo_aceptable

    @property
    def mensaje(self):
        return self._mensajes

    @property
    def promedio(self):
        return self._promedio

    @property
    def rango_advertencia(self):
        return self._rango_advertencia

    @property
    def minimo_aceptable(self):
        return self._minimo_aceptable

    @rango_advertencia.setter
    def rango_advertencia(self, value):
        self._rango_advertencia = value

    @minimo_aceptable.setter
    def minimo_aceptable(self, value):
        self._minimo_aceptable = value

    @promedio.setter
    def promedio(self, value):
        self._promedio = float(value)
