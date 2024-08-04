# syncademic/views/__init__.py

from .disparador_api_view import DisparadorViewSet
from .seguimiento_api_view import SeguimientoMallaAPIView

__all__ = [
    'DisparadorViewSet',
    'SeguimientoMallaAPIView',
]
