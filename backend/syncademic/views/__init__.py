# syncademic/views/__init__.py

from .disparador_api_view import DisparadorViewSet
from .seguimiento_api_view import SeguimientoMallaAPIView
from .notas_api_view import ControlNotasAPIView
from .asistencia_api_view import AsistenciaAPIView
from .cronograma_api_view import CronogramaAPIView
from .tema_cronograma_api_view import TemaCronogramaAPIView


_all_ = [
    'DisparadorViewSet',
    'SeguimientoMallaAPIView',
    'ControlNotasAPIView',
    'AsistenciaAPIView',
    'CronogramaAPIView',
    'TemaCronogramaAPIView'
]
