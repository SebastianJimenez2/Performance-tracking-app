from django.urls import path, include
from syncademic import views
from syncademic.views.seguimiento_api_view import SeguimientoMallaAPIView
from rest_framework.routers import DefaultRouter

from syncademic.views import (
    ControlNotasAPIView
)

router = DefaultRouter()
router.register(r'control-notas', ControlNotasAPIView, basename='control-notas')

urlpatterns = [
    path("seguimiento/<str:asignatura_prerequisito>/<str:periodo_actual>/", SeguimientoMallaAPIView.as_view(), name='seguimiento-malla')
]

urlpatterns = [
    path('', include(router.urls)),
]
