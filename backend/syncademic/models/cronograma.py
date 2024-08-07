from django.db import models
from .asignatura import Asignatura


class Cronograma(models.Model):
    """ Modelo Cronograma

        Utilizado para feature 5
        Creado por David Yanez

        Attributes:
            id_cronograma (int),
            asignatura (int),
            estado (str)
            fecha_inicio (date)
    """

    id_cronograma = models.AutoField(primary_key=True)
    asignatura = models.OneToOneField(Asignatura, on_delete=models.CASCADE, related_name='asignatura', unique=True)
    estado = models.CharField(max_length=20, null=True, default='n/a')
    fecha_inicio = models.DateField(null=True)

    def __str__(self):
        return self.id_cronograma
