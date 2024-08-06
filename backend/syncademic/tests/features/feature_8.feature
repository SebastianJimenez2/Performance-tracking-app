# Creado por Grupo 4 el 28/07/2024
# language: es

Característica: Seguimiento de capacitaciones
  Como institución
  quiero llevar un seguimiento de la capacitación de los docentes
  para verificar que su enseñanza esté actualizada y en sintonía con las mejores prácticas educativas actuales.

Esquema del escenario: Puntuación de capacitaciones por area afín
  Dado que las áreas afines del docente son "<areas_afines>"
  Y la puntuación inicial del docente es "<puntuacion_inicial>"
  Cuando el docente registra una capacitación en el área de "<area>"
  Entonces su puntuación final será de <puntuacion_final>
  Ejemplos:
    | areas_afines               | puntuacion_inicial | area          | puntuacion_final |
    | ["Matemáticas", "Física"]  | 80                 | Matemáticas   | 85               |
    | ["Matemáticas", "Física"]  | 80                 | Historia      | 85               |

Esquema del escenario: Identificación de incumplimiento en el registro de capacitaciones
  Dado que el docente <confirmacion> al menos una capacitación
  Entonces se marca al registro del docente como <estado>
  Y la institución decide que <envia> un recordatorio al docente
  Ejemplos:
  | confirmacion     | estado     | envia    |
  | ha registrado    | completo   | no envia |
  | no ha registrado | incompleto | envia    |