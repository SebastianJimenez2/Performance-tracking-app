from django.db import models

from asignatura import Asignatura
from tipo_evaluacion import TipoEvaluacion
from docente import Docente


class Evaluacion(models.Model):
    tipo_evaluacion = models.IntegerField(choices=TipoEvaluacion.choices)
    calificacion = models.FloatField()
    asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)
    docente = models.ForeignKey(Docente, on_delete=models.CASCADE)