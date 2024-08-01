from django.db import models


class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
