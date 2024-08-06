# Creado por Grupo 4 el 28/07/2024
# language: es

# Feature 8
# Grupo 4: Sebastian Moyano, Luis De La Cruz, Christopher Zambrano

Característica: Seguimiento de capacitaciones
  Como institución
  quiero llevar un seguimiento de la capacitación de los docentes
  para verificar que su enseñanza esté actualizada y en sintonía con las mejores prácticas educativas actuales.

Esquema del escenario: Puntuación de capacitaciones por area afín
  Dado que un docente tiene como areas afines "<areas_afines>"
  Y tiene una puntuacion inicial de "<puntuacion_inicial>"
  Cuando el docente registra una capacitación en el área de "<area>"
  Entonces su puntuación final será de <puntuacion_final>
  Ejemplos:
    | areas_afines        | puntuacion_inicial | area          | puntuacion_final |
    | Matematicas,Fisica  | 80                 | Matematicas   | 85               |
    | Matematicas,Fisica  | 80                 | Historia      | 82               |

Esquema del escenario: Identificación de incumplimiento en el registro de capacitaciones
  Dado que el docente tiene "<capacitaciones>" registradas
  Entonces se marca al registro del docente como "<estado>"
  Y la institución decide que "<envia>" un recordatorio al docente
  Ejemplos:
  | capacitaciones  | estado     | envia    |
  | 1               | completo   | no envia |
  | 0               | incompleto | envia    |