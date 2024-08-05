from django.db import models
from .asignatura import Asignatura


class Cronograma(models.Model):
    id_cronograma = models.AutoField(primary_key=True)
    id_asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE, related_name='cronogramas')
    estado = models.CharField(max_length=20, null=True, default='n/a') # setear cuando se hace un check a tema
    fecha_inicio = models.DateField(null=True)

    def __str__(self):
        return self.id_cronograma
    