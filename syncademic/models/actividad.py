from django.db import models


class Actividad(models.Model):
    id_actividad = models.AutoField(primary_key=True)

    # TODO: Relación asignatura - actividad
    id_asignatura = models.IntegerField()
    nota = models.DecimalField(max_digits=5, decimal_places=2)
    tipo_actividad = models.ForeignKey('TipoActividad',
                                       on_delete=models.CASCADE,
                                       related_name='actividades')

    # TODO: Crear modelo de temas-asignatura y relacionarlo aquí
    tema = models.TextField()

    def __str__(self):
        return self.nota


class TipoActividad(models.Model):
    id_tipo_actividad = models.AutoField(primary_key=True)
    nombre_tipo = models.CharField(max_length=50)

    # porcentaje de ponderación en el promedio
    peso = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.nombre_tipo
