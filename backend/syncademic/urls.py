# syncademic/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from syncademic.views import DisparadorViewSet, SeguimientoMallaAPIView, ControlNotasAPIView

router = DefaultRouter()
router.register(r'auth', DisparadorViewSet, basename='disparador')
router.register(r'control-notas', ControlNotasAPIView, basename='control-notas')

urlpatterns = [
    path("seguimiento/<str:asignatura_prerequisito>/<str:periodo_actual>/", SeguimientoMallaAPIView.as_view(), name='seguimiento-malla'),
    path('', include(router.urls)),
]
