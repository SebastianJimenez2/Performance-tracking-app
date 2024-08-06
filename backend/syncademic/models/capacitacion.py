from django.db import models
from .docente import Docente
from .periodo import Periodo


class Capacitacion(models.Model):
    id_capacitacion = models.AutoField(primary_key=True)
    docente = models.ForeignKey(Docente, on_delete=models.SET_NULL, default=1)
    nombre_capacitacion = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    periodo = models.ForeignKey(Periodo, on_delete=models.SET_DEFAULT, default=1)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.nombre