from django.db import models

from .cronograma import Cronograma


class TemaCronograma(models.Model):
    """ Modelo TemaCronograma

            Utilizado para feature 5
            Creado por David Yanez

            Attributes:
            id_tema (int),
            descripcion (str),
            orden (int),
            tiempo_en_semanas (int),
            completado (bool),
            semana_finalizacion_relativa_a_inicio (int),
            fecha_completado (date)
    """
    id_tema = models.AutoField(primary_key=True)
    cronograma = models.ForeignKey(Cronograma, on_delete=models.CASCADE, related_name='temas')
    descripcion = models.TextField()
    orden = models.IntegerField()  # Guardara que orden tiene el cronograma en la lista de cronogramas, setear al crea un nuevo tema_cronograma
    tiempo_en_semanas = models.IntegerField()
    completado = models.BooleanField(default=False)
    semana_finalizacion_relativa_a_inicio = models.IntegerField(null=True)  # setear cuando se crea un tema
    fecha_completado = models.DateField(null=True)  # setear cuando se completa un tema

    def __str__(self):
        return self.id_tema
