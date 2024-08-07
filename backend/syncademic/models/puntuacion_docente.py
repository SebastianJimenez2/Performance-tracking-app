from django.db import models

from syncademic.models.docente import Docente
from syncademic.models.periodo import Periodo


class Puntuacion_docente(models.Model):
    """ Modelo Puntuacion_docente

                Utilizado para Feature 8
                Creado por Christopher Zambrano

                Attributes:
                    id_puntuacion (int),
                    id_docente (int),
                    periodo (int),
                    puntaje (char)
            """
    id_puntuacion = models.IntegerField(primary_key=True)
    id_docente = models.ForeignKey(Docente, on_delete=models.SET_NULL, null=True)
    periodo = models.ForeignKey(Periodo, on_delete=models.SET_DEFAULT, default=1)
    puntaje = models.IntegerField(max_length=50)

    def __str__(self):
        return self.docente + self.puntaje
