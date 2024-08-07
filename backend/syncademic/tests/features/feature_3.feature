# Created by kevin at 24/7/24
# language: es

Característica: Identificación de temas no comprendidos
Como docente
quiero recibir una alerta sobre los temas que pudieron no haber sido comprendidos por los estudiantes y pudiesen representar complicaciones en la unidad entrante
para decidir si implemento actividades de refuerzo o no

Escenario: Alerta por umbral de comprensión inferior al 70% en un tema específico
  Dado que el docente de "Profesionalismo en Informática" ha finalizado la enseñanza del tema "Marca Personal"
  Y se han registrado las siguientes puntuaciones en las evaluaciones para determinar el umbral de comprensión
    | Tipo de evaluación            | Puntuación máxima | Puntuación obtenida |
    | Kahoot                        | 20                | 12                  |
    | Evaluación de sentimientos    | 5                 | 3                   |
    | Evaluaciones de la asignatura | 20                | 13                  |
  Cuando se calcula el umbral de comprensión promedio del tema y es inferior al 70%
  Entonces el docente debe recibir una alerta sugiriendo implementar refuerzo académico

Escenario: Indicar imposibilidad de identificar temas no comprendidos por falta de evaluaciones
  Dado que el docente de "Profesionalismo en informática" ha concluido la enseñanza del tema "Pirámide jurídica"
  Y el tema "Pirámide jurídica" no cuenta con todas las evaluaciones necesarias
  Cuando se intenta determinar el umbral de comprensión alcanzado por los estudiantes
  Entonces la fila correspondiente a "Pirámide jurídica" aparecerá destacada en blanco en el informe