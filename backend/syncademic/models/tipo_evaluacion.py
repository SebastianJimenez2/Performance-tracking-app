
from django.db import models

class TipoEvaluacion(models.IntegerChoices):
    HETEROEVALUACION = 1, 'Heteroevaluacion'
    AUTOEVALUACION = 2, 'Autoevaluacion'
    COEVALUACION = 3, 'Coevaluacion'
    TOTAL = 4, 'Total'
