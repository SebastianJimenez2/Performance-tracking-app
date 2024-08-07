from django.urls import path, include
from rest_framework.routers import DefaultRouter

from syncademic.views import DisparadorViewSet, SeguimientoMallaAPIView, ControlNotasAPIView, CronogramaAPIView, \
    TemaCronogramaAPIView, AsistenciaAPIView, EvaluacionViewSet, AsignaturaViewSet, DocenteViewSet, CapacitacionAPIView, SilaboAPIView

router = DefaultRouter()
router.register(r'auth', DisparadorViewSet, basename='disparador')
router.register(r'control-notas', ControlNotasAPIView, basename='control-notas')
router.register(r'evaluacion-docente', EvaluacionViewSet, basename='evaluacion-docente')
router.register(r'seguimiento-malla', SeguimientoMallaAPIView, basename='seguimiento-malla')
router.register(r'cronograma', CronogramaAPIView, basename='cronograma')
router.register(r'tema-cronograma', TemaCronogramaAPIView, basename='tema-cronograma')
router.register(r'asistencia', AsistenciaAPIView, basename='asistencia')
router.register(r'asignatura', AsignaturaViewSet, basename='asignatura')
router.register(r'docente', DocenteViewSet, basename='docente')
router.register(r'capacitacion', CapacitacionAPIView, basename='capacitacion')
router.register(r'silabo', SilaboAPIView, basename='silabo')


urlpatterns = [
    path('', include(router.urls)),
]
