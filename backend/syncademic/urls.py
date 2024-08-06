# syncademic/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from syncademic.views import DisparadorViewSet, SeguimientoMallaAPIView, ControlNotasAPIView
from syncademic.views import DisparadorViewSet, SeguimientoMallaAPIView, ControlNotasAPIView, CronogramaAPIView, TemaCronogramaAPIView

router = DefaultRouter()
router.register(r'auth', DisparadorViewSet, basename='disparador')
router.register(r'control-notas', ControlNotasAPIView, basename='control-notas')
router.register(r'cronograma', CronogramaAPIView, basename='cronograma')
router.register(r'tema-cronograma', TemaCronogramaAPIView, basename='tema-cronograma')

urlpatterns = [
    path("seguimiento/<str:asignatura_prerequisito>/<str:periodo_actual>/", SeguimientoMallaAPIView.as_view(), name='seguimiento-malla'),
    path('', include(router.urls)),
]