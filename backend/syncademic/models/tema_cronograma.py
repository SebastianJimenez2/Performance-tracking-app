from django.db import models

from asignatura import Asignatura
from cronograma import Cronograma

class TemaCronograma(models.Model):
    id_tema = models.AutoField(primary_key=True)
    id_cronograma = models.ForeignKey(Cronograma, on_delete=models.CASCADE, related_name='temas')
    descripcion = models.TextField()
    orden = models.IntegerField() # Guardara que orden tiene el cronograma en la lista de cronogramas
    tiempo_en_semanas = models.IntegerField()
    completado = models.BooleanField(default=False)
    semana_finalizacion_relativa_a_inicio = models.IntegerField(null=True)
    fecha_completado = models.DateField(null=True)

    def __str__(self):
        return self.id_tema
    