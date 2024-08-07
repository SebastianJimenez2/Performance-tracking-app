from django.db import models
from syncademic.models.estudiante import Estudiante
from syncademic.models.asignatura import Asignatura
from syncademic.models.periodo import Periodo


class HistorialNotas(models.Model):
    """ Modelo Historial Notas

        Utilizado para Feature 2
        Creado por Alejandra Colcha

        Attributes:
            id_nota (int),
            id_asignatura (int),
            id_estudiante (int),
            grupo (int),
            periodo(int),
            nota (float),
            tipo_actividad(int),
            tema (str)
    """

    id_nota = models.AutoField(primary_key=True)
    id_asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)
    id_estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, related_name='estudiantes')
    grupo = models.IntegerField()
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE)

    nota = models.DecimalField(max_digits=5, decimal_places=2)
    tipo_actividad = models.ForeignKey('TipoActividad',
                                       on_delete=models.CASCADE)

    # TODO: Crear modelo de temas-asignatura y relacionarlo aquí
    tema = models.TextField()

    def __str__(self):
        return f"Nota: {self.nota}"


class TipoActividad(models.Model):
    """ Modelo Tipo Actividad
        Utilizado en modelo Historial Notas para Feature 2
        Creado por Alejandra Colcha

        Atributos:
            id_tipo_actividad (int),
            nombre_tipo (str),
            peso (float)
    """
    id_tipo_actividad = models.AutoField(primary_key=True)
    nombre_tipo = models.CharField(max_length=50)

    # puntos en relación con la nota final
    peso = models.DecimalField(max_digits=4, decimal_places=1)

    def __str__(self):
        return self.nombre_tipo
