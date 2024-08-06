from django.db import models
from .asignatura import Asignatura


class Cronograma(models.Model):
    id_cronograma = models.AutoField(primary_key=True)
    asignatura = models.OneToOneField(Asignatura, on_delete=models.CASCADE, related_name='asignatura', unique=True)
    estado = models.CharField(max_length=20, null=True, default='n/a')
    fecha_inicio = models.DateField(null=True)

    def __str__(self):
        return self.id_cronograma
    