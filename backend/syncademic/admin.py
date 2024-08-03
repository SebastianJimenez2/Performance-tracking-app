from django.contrib import admin
from .models.asignatura import Asignatura
from .models.cronograma import Cronograma
from .models.docente import Docente
from .models.estudiante import Estudiante
from .models.evaluacion import Evaluacion
from .models.notas import HistorialNotas,TipoActividad
from .models.periodo import Periodo

# Register your models here.
admin.site.register(Asignatura)
admin.site.register(Cronograma)
admin.site.register(Docente)
admin.site.register(Estudiante)
admin.site.register(Evaluacion)
admin.site.register(HistorialNotas)
admin.site.register(TipoActividad)
admin.site.register(Periodo)



