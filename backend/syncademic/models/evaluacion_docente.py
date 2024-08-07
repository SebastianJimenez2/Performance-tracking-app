from django.db import models

from ..models.asignatura import Asignatura
from ..models.tipo_evaluacion_docente import TipoEvaluacion
from ..models.docente import Docente


class Evaluacion(models.Model):
    tipo_evaluacion = models.IntegerField(choices=TipoEvaluacion.choices)
    calificacion = models.FloatField()
    asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)
    docente = models.ForeignKey(Docente, on_delete=models.CASCADE)
    periodo = models.CharField(max_length=5)