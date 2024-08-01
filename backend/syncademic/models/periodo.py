from django.db import models


class Periodo(models.Model):
    id_periodo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
