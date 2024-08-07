class AreaDocente:
    """
                AreaDocente
                Clase auxiliar para recopilar solo la información necesaria del docente.

                Atributos:
                nombre,
                áreas,
                puntos_capacitacion
    """

    def __init__(self, nombre: str):
        self.nombre = nombre
        self.areas = None
        self.puntos_capacitacion = 0
        self.capacitaciones = 0
        self.ha_registrado_capacitacion = None
        self.estado: str = "incompleto"

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def areas(self):
        return self._areas

    @areas.setter
    def areas(self, areas):
        self._areas = areas

    @property
    def puntos_capacitacion(self):
        return self._puntos_capacitacion

    @puntos_capacitacion.setter
    def puntos_capacitacion(self, value):
        self._puntos_capacitacion = value

    @property
    def capacitaciones(self):
        return self._capacitaciones

    @capacitaciones.setter
    def capacitaciones(self, capacitaciones):
        self._capacitaciones = capacitaciones

    @property
    def ha_registrado_capacitacion(self):
        return self._ha_registrado_capacitacion

    @ha_registrado_capacitacion.setter
    def ha_registrado_capacitacion(self, ha_registrado_capacitacion):
        self._ha_registrado_capacitacion = ha_registrado_capacitacion

    @property
    def estado(self):
        return self._estado

    @estado.setter
    def estado(self, value) -> str:
        self._estado = value



class AreaCapacitacion:
        """
                AreaCapacitacion
                Clase auxiliar para recopilar solo la información necesaria de la capacitacion.

                Atributos:
                nombre,
                área
        """

        def __init__(self, nombre: str):
            self.nombre = nombre
            self.area = None

        @property
        def nombre(self):
            return self._nombre

        @nombre.setter
        def nombre(self, nombre):
            self._nombre = nombre

        @property
        def area(self):
            return self._area

        @area.setter
        def area(self, area):
            self._area = area


class ControlAreas:
    """
            CONTROL ÁREAS
            Recibe un docente para comparar su area respecto al area de una capacitacion.

            Attributes:
            docente (AreaDocente)
            capacitacion (AreaCapacitacion)
    """

    def __init__(self, docente: AreaDocente, capacitacion: AreaCapacitacion):
        self.docente = docente
        self.capacitacion = capacitacion

    def son_afines(self):
        if self.capacitacion.area in self.docente.areas:
            return True
        else:
            return False

    def calcular_puntuacion(self):
        if self.son_afines():
            self.docente.puntos_capacitacion = self.docente.puntos_capacitacion + 5
        else:
            self.docente.puntos_capacitacion = self.docente.puntos_capacitacion + 2