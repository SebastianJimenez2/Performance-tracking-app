from django.db import models


class Estudiante(models.Model):
    id_estudiante = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    numero_incidencias = models.IntegerField()

    def __str__(self):
        return self.nombre
