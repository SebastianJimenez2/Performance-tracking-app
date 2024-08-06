from django.urls import path, include
from syncademic import views
from syncademic.views.seguimiento_api_view import SeguimientoMallaAPIView
from rest_framework.routers import DefaultRouter

from syncademic.views import (
    ControlNotasAPIView
)
from syncademic.views import (
evaluacion_docente_api_view
)

router = DefaultRouter()
router.register(r'control-notas', ControlNotasAPIView, basename='control-notas')
router.register(r'evaluacion-docente', evaluacion_docente_api_view, basename='evaluacion-docente')

urlpatterns = [
    path("seguimiento/<str:asignatura_prerequisito>/<str:periodo_actual>/", SeguimientoMallaAPIView.as_view(), name='seguimiento-malla')
]

urlpatterns = [
    path('', include(router.urls)),
]
