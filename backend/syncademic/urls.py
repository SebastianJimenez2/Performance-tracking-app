# syncademic/urls.py

from syncademic.views import (
    ControlNotasAPIView
)
from syncademic.views import (
evaluacion_docente_api_view
)
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from syncademic.views import DisparadorViewSet, SeguimientoMallaAPIView, ControlNotasAPIView
from syncademic.views import DisparadorViewSet, SeguimientoMallaAPIView, ControlNotasAPIView, CronogramaAPIView, TemaCronogramaAPIView

router = DefaultRouter()
router.register(r'auth', DisparadorViewSet, basename='disparador')
router.register(r'control-notas', ControlNotasAPIView, basename='control-notas')
router.register(r'evaluacion-docente', evaluacion_docente_api_view, basename='evaluacion-docente')

urlpatterns = [
    path("seguimiento/<str:asignatura_prerequisito>/<str:periodo_actual>/", SeguimientoMallaAPIView.as_view(), name='seguimiento-malla')
]
router.register(r'seguimiento-malla', SeguimientoMallaAPIView, basename='seguimiento-malla')
router.register(r'cronograma', CronogramaAPIView, basename='cronograma')
router.register(r'tema-cronograma', TemaCronogramaAPIView, basename='tema-cronograma')

urlpatterns = [
    path('', include(router.urls)),
]