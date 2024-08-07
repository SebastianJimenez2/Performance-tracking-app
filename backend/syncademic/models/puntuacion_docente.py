from django.db import models

from syncademic.models.docente import Docente
from syncademic.models.periodo import Periodo


class Puntuacion_docente(models.Model):
    id_puntuacion = models.IntegerField(primary_key=True)
    id_docente = models.ForeignKey(Docente, on_delete=models.SET_NULL, null=True)
    periodo = models.ForeignKey(Periodo, on_delete=models.SET_DEFAULT, default=1)
    puntaje = models.CharField(max_length=50)

    def __str__(self):
        return self.docente + self.puntaje
