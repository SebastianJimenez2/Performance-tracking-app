from django.db import models


class Cronograma(models.Model):
    id_cronograma = models.AutoField(primary_key=True)
    tiempo_en_semanas = models.IntegerField()
    completado = models.BooleanField(default=False)
    fecha_completado = models.DateField(null=True)
    fecha_inicio = models.DateField()

    def __str__(self):
        return self.id_cronograma
    
