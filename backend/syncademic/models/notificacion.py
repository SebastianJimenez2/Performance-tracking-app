from django.db import models
from .aspecto import Aspecto


class Notificacion(models.Model):
    aspecto = models.ForeignKey(Aspecto, on_delete=models.CASCADE)
    estado = models.CharField(max_length=20, default="BAJO")
    fecha_notificacion = models.DateTimeField(auto_now_add=True)
    mensaje = models.JSONField(default=dict)

    def __str__(self):
        return f"Notificacion: {self.aspecto.nombre} - {self.estado}"

    def comportarse_segun(self, estado):
        enrutador_estado = {
            "CRITICO": self.comportarse_segun_critico,
            "INTENSO": self.comportarse_segun_intenso,
            "NORMAL": self.comportarse_segun_normal,
            "BAJO": self.comportarse_segun_bajo,
        }

        comportarse_funcion = enrutador_estado.get(estado, self.comportarse_segun_por_defecto)
        return comportarse_funcion()

    def comportarse_segun_critico(self):
        return True  # Notificaciones críticas se envían siempre

    def comportarse_segun_intenso(self):
        # Notificar diariamente
        return True

    def comportarse_segun_normal(self):
        # Notificar lunes, miércoles y viernes
        dia_semana = self.fecha_notificacion.weekday()
        return dia_semana in [0, 2, 4]  # 0: Lunes, 2: Miércoles, 4: Viernes

    def comportarse_segun_bajo(self):
        # Notificar los lunes
        dia_semana = self.fecha_notificacion.weekday()
        return dia_semana == 0  # 5: Sábado (cambiar a 0 para lunes)

    def comportarse_segun_por_defecto(self):
        return False
