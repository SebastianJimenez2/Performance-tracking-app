from django.urls import path, include
from syncademic import views
from syncademic.views.seguimiento_api_view import SeguimientoMallaAPIView
from rest_framework.routers import DefaultRouter

from syncademic.views import (
    CronogramaAPIView,
    TemaCronogramaAPIView
)

router = DefaultRouter()
router.register(r'cronograma', CronogramaAPIView, basename='cronograma')
router.register(r'tema-cronograma', TemaCronogramaAPIView, basename='tema-cronograma')

'''
urlpatterns = [
    path("seguimiento/<str:asignatura_prerequisito>/<str:periodo_actual>/", SeguimientoMallaAPIView.as_view(), name='seguimiento-malla')
]
'''

urlpatterns = [
    path('', include(router.urls)),
]
