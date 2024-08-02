from django.db import models

from .asignatura import Asignatura
from ..models.periodo import Periodo


class Estudiante(models.Model):
    id_estudiante = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    email = models.CharField(max_length=150, blank=True, null=True)
    numero_incidencias = models.IntegerField()
    periodo_cursando = models.ForeignKey(Periodo, on_delete=models.SET_DEFAULT, default=1)

    asignaturas = models.ManyToManyField(Asignatura,
                                         related_name='asignaturas')

    grupo_actual = models.IntegerField(null=False, default=1)

    prioridad = models.CharField(max_length=5, default="BAJA")

    def __str__(self):
        return self.nombre
