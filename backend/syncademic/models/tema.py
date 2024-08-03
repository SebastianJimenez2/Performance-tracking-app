from django.db import models

from asignatura import Asignatura
from cronograma import Cronograma

class Tema(models.Model):
    id_tema = models.AutoField(primary_key=True)
    id_asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE, related_name='temas')
    id_cronograma = models.ForeignKey(Cronograma, on_delete=models.CASCADE, related_name='temas')
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    total_clases = models.IntegerField()
    total_inscritos = models.IntegerField()
    total_comprende = models.IntegerField()

    def __str__(self):
        return self.nombre
    