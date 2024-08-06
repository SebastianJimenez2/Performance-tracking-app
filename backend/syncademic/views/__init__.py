# syncademic/views/__init__.py

from .disparador_api_view import DisparadorViewSet
from .seguimiento_malla_api_view import SeguimientoMallaAPIView
from .notas_api_view import ControlNotasAPIView
from .asistencia_api_view import AsistenciaAPIView
from .evaluacion_view import EvaluacionViewSet

__all__ = [
    'DisparadorViewSet',
    'SeguimientoMallaAPIView',
    'ControlNotasAPIView',
    'AsistenciaAPIView',
]
