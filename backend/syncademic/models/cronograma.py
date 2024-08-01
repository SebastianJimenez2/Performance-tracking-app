from django.db import models

class Cronograma(models.Model):
    id_cronograma = models.AutoField(primary_key=True)
    id_asignatura = models.ForeignKey('Asignatura', on_delete=models.CASCADE, related_name='cronogramas')
    # TODO: lógica para manejar los temas de este cronograma y cuales se han completado