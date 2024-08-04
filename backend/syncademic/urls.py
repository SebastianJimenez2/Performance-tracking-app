# syncademic/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from syncademic.views import DisparadorViewSet, SeguimientoMallaAPIView

router = DefaultRouter()
router.register(r'auth', DisparadorViewSet, basename='disparador')

urlpatterns = [
    path("seguimiento/<str:asignatura_prerequisito>/<str:periodo_actual>/", SeguimientoMallaAPIView.as_view(), name='seguimiento-malla'),
    path('', include(router.urls)),
]
