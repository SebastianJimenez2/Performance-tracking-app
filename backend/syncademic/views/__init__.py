# syncademic/views/__init__.py

from .disparador_api_view import DisparadorViewSet
from .seguimiento_malla_api_view import SeguimientoMallaAPIView
from .notas_api_view import ControlNotasAPIView
from .asistencia_api_view import AsistenciaAPIView
from .cronograma_api_view import CronogramaAPIView
from .tema_cronograma_api_view import TemaCronogramaAPIView
from .evaluacion_docente_api_view import EvaluacionViewSet
from .asignatura_view import AsignaturaViewSet
from .docente_view import DocenteViewSet


_all_ = [
    'DisparadorViewSet',
    'SeguimientoMallaAPIView',
    'ControlNotasAPIView',
    'AsistenciaAPIView',
    'CronogramaAPIView',
    'TemaCronogramaAPIView'
]
