from django.db import models

class Silabo(models.Model):
    asignatura = models.CharField(max_length=100, help_text="Nombre de la asignatura")

    def __str__(self):
        return f"Silabo de {self.asignatura}"

class Tema(models.Model):
    silabo = models.ForeignKey(Silabo, on_delete=models.CASCADE, related_name='temas')
    titulo = models.CharField(max_length=100, help_text="Título del tema")
    prueba_kahoot = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    prueba_sentimientos = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    prueba_tema = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.titulo

    def calcular_promedio(self):
        evaluaciones = [self.prueba_kahoot, self.prueba_sentimientos, self.prueba_tema]
        evaluaciones = [e for e in evaluaciones if e is not None]  # Filtrar None
        if evaluaciones:
            return sum(evaluaciones) / len(evaluaciones)
        return None
