from django.db import models


class Docente(models.Model):
    id_docente = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=150)
    correo = models.EmailField(max_length=150)
    estado_capacitacion = models.CharField(max_length=50)
    carrera = models.CharField(max_length=50)
    puntaje_actual = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.nombre + self.correo

# TODO: Relaciones de otras entidades con docente
