from django.contrib import admin
from .models import asignatura, cronograma, docente, estudiante, notas, periodo

# Register your models here.
admin.site.register(asignatura)
admin.site.register(cronograma)
admin.site.register(docente)
admin.site.register(estudiante)
admin.site.register(notas)
admin.site.register(periodo)
