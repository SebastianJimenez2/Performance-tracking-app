from django.db import models


class Docente(models.Model):
    id_docente = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=150)
    correo = models.EmailField(max_length=150)
    estado = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre + self.correo


# TODO: Relaciones de otras entidades con docente
