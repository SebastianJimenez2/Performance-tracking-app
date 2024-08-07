from django.db import models
from datetime import datetime
from .docente import Docente


class Aspecto(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    docente = models.ForeignKey(Docente, on_delete=models.CASCADE)
    subaspectos = models.JSONField()

    def calcular_tiempo_transcurrido(self):
        total_dias = (self.fecha_fin - self.fecha_inicio).days
        dias_transcurridos = (datetime.now().date() - self.fecha_inicio).days
        return (dias_transcurridos * 100) / total_dias

    def calcular_progreso_actual(self):
        progreso_total = sum(subaspecto['progreso'] for subaspecto in self.subaspectos)
        progreso_general = (progreso_total / len(self.subaspectos))
        return progreso_general

    def determinar_estado_notificacion(self, tiempo_transcurrido, progreso_actual):
        reglas = [
            {"estado": "CRITICO", "condicion": lambda t, p: t > 90 and p <= 50},
            {"estado": "INTENSO", "condicion": lambda t, p: 80 < t <= 90 and p <= 50},
            {"estado": "NORMAL", "condicion": lambda t, p: 50 < t <= 80 and p < 50},
            {"estado": "BAJO", "condicion": lambda t, p: t <= 50 and p < 20},
            {"estado": "BAJO", "condicion": lambda t, p: True},  # Estado por defecto
        ]

        for regla in reglas:
            if regla["condicion"](tiempo_transcurrido, progreso_actual):
                return regla["estado"]
        return "BAJO"  # Valor por defecto si ninguna condición es cumplida
