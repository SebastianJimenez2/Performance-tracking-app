from django.db import models
from .docente import Docente
from .periodo import Periodo


class Capacitacion(models.Model):
    """ Modelo Capacitacion

            Utilizado para Feature 8
            Creado por Christopher Zambrano

            Attributes:
                id_capacitacion (int),
                docente (int),
                nombre_capacitacion (str),
                area (int),
                periodo (int)
        """
    id_capacitacion = models.AutoField(primary_key=True)
    docente = models.ForeignKey(Docente, on_delete=models.SET_NULL, default=1, null=True)
    nombre_capacitacion = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    periodo = models.ForeignKey(Periodo, on_delete=models.SET_DEFAULT, default=6)

    def __str__(self):
        return self.nombre
