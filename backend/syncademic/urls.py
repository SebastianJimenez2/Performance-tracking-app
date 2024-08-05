from django.urls import path, include
from rest_framework.routers import DefaultRouter

from syncademic.views import (
    ControlNotasAPIView,
    SeguimientoMallaAPIView
)

router = DefaultRouter()
router.register(r'control-notas', ControlNotasAPIView, basename='control-notas')
router.register(r'seguimiento-malla', SeguimientoMallaAPIView, basename='seguimiento-malla')

urlpatterns = [
    path('', include(router.urls)),
]
