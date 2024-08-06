from django.db import models
from .docente import Docente


class Asignatura(models.Model):
    id_asignatura = models.AutoField(primary_key=True)
    docente = models.ForeignKey(Docente, on_delete=models.SET_NULL, null=True)
    prerequisito = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='anteriores')
    subsecuente = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='siguientes')
    nota_minima = models.DecimalField(max_digits=5, decimal_places=2)
    nombre = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    total_clases = models.IntegerField()
    total_inscritos = models.IntegerField()
    total_comprende = models.IntegerField()

    def __str__(self):
        return self.nombre
