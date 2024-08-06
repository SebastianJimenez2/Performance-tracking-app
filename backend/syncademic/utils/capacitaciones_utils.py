class AreaDocente:
    """
                AreaDocente
                Clase auxiliar para recopilar solo la información necesaria del docente.

                Atributos: nombre, áreas
    """

    def __init__(self, nombre: str, areas: list):
        self.nombre = nombre
        self.area = areas
        self.puntos_capacitacion = 0

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
    def numero_incidencias(self, puntos_capacitacion):
        self._puntos_capacitacion = puntos_capacitacion

    @property
    def tiene_area(self, cadena_buscada):
        # Recorre cada elemento en la lista
        for elemento in self.areas:
            # Verifica si el elemento es una cadena y si es igual a cadena_buscada
            if isinstance(elemento, str) and elemento == cadena_buscada:
                return True
        # Si no se encontró la cadena buscada, retorna False
        return False

class AreaCapacitacion:
        """
                    AreaCapacitacion
                    Clase auxiliar para recopilar solo la información necesaria de la capacitacion.

                    Atributos: nombre, área
            """

        def __init__(self, nombre: str, area: str):
            self.nombre = nombre
            self.area = area

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
    """
    class ControlCapacitacion:
        def __init__(self, docente: AreaDocente):
            self.docente = docente
            self.calificacion_actual = 0



        def pertenece_al_area(self, capacitacion):
            areaDocente = self.docente.asignatura

            if (self.docente.id_docente == self.asignatura.id_docente):

                areaDocente = self.asignatura.area

                if (areaDocente == capacitacion.area):

                    return True
            else:
                    return False