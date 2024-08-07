from django.db import models
from .estudiante import Estudiante
from .asignatura import Asignatura


class Asistencia(models.Model):
    id_asistencia = models.AutoField(primary_key=True)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)
    semana = models.IntegerField()  # Número de semana
    dia = models.CharField(max_length=10)  # Día de la semana ('Lunes', 'Martes', etc.)
    presente = models.BooleanField(default=False)

    class Meta:
        unique_together = ('estudiante', 'asignatura', 'semana', 'dia')

    def __str__(self):
        return f"{self.estudiante.nombre_estudiante} - {self.asignatura.nombre} - Semana {self.semana} - {self.dia}"