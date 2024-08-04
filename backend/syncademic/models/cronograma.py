from django.db import models
from asignatura import Asignatura


class Cronograma(models.Model):
    id_cronograma = models.AutoField(primary_key=True)
    id_asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE, related_name='cronogramas')
    estado = models.CharField(max_length=20, null=True)
    fecha_inicio = models.DateField()

    def __str__(self):
        return self.id_cronograma
    
