# syncademic/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from syncademic.views import DisparadorViewSet, SeguimientoMallaAPIView, ControlNotasAPIView, AsistenciaAPIView

router = DefaultRouter()
router.register(r'auth', DisparadorViewSet, basename='disparador')
router.register(r'control-notas', ControlNotasAPIView, basename='control-notas')
router.register(r'seguimiento-malla', SeguimientoMallaAPIView, basename='seguimiento-malla')
router.register(r'asistencia', AsistenciaAPIView, basename='asistencia')

urlpatterns = [
    path('', include(router.urls)),
]
