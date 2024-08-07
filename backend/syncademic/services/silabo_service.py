from syncademic.models.silabo import Tema
from syncademic.exceptions.not_found import ObjectNotFound

class SilaboService:

    @staticmethod
    def obtener_evaluaciones_tema(id_tema):
        """
        Obtiene las evaluaciones de un tema específico dentro de un sílabo.

        Args:
            id_tema (int): El ID del tema del cual obtener las evaluaciones.

        Returns:
            dict: Un diccionario con las evaluaciones kahoot, sentimientos y tema, o una alerta si alguna es faltante.

        Raises:
            ObjectNotFound: Si no se encuentra el tema.
        """
        try:
            tema = Tema.objects.get(pk=id_tema)
            evaluaciones = {
                'prueba_kahoot': tema.prueba_kahoot,
                'prueba_sentimientos': tema.prueba_sentimientos,
                'prueba_tema': tema.prueba_tema
            }
            # Verificar si alguna evaluación es None
            if None in evaluaciones.values():
                return {'alerta': 'No es posible calcular el umbral debido a que no existen todas las calificaciones.'}
            return evaluaciones
        except Tema.DoesNotExist:
            raise ObjectNotFound('Tema', f'No se encontró un tema con el id {id_tema}')
