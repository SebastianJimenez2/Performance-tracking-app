from django.db import models


class Cronograma(models.Model):
    id_cronograma = models.AutoField(primary_key=True)
    tiempo_en_semanas = models.IntegerField()
    completado = models.BooleanField(default=False)
    fecha_inicio = models.DateField()

    # TODO: lógica para manejar los temas de este cronograma y cuales se han completado
