# Creado por Grupo 2 at 23/7/24
# language: es

Característica: Identificación de estudiantes con bajas calificaciones
  Como docente quiero saber quienes son los estudiantes con tendencia a
  tener un promedio por debajo del mínimo aceptable en base a su perfil e historial académico
  para comunicarme con ellos y agendar una cita de ser necesaria.

Esquema del escenario: Estudiante con promedio cerca del mínimo aceptable
    Cuando un estudiante tiene un promedio de "<promedio>"
    Y el profesor estableció un rango de advertencia de "<rango_advertencia>" para una nota mínima aceptable de "<minimo>"
    Entonces el profesor de la asignatura "<recibe>" recibe un mensaje de advertencia

    Ejemplos:
      | promedio |minimo| rango_advertencia  | recibe |
      |   7.1    |7.0     |0.3                 |SI   |
      |   8.0    |7.0     |0.5                 |NO   |
      |   7.3    |7.0     |0.4                 |SI  |
      |   7.7    |7.0    |0.3                 |NO  |

  Esquema del escenario: Estudiante con promedio debajo mínimo aceptable
    Dado un estudiante tiene un promedio de "<promedio>" que ha bajado del mínimo "<ocasiones>" ocasiones
    Cuando baje del mínimo aceptable de "<minimo>" nuevamente
    Entonces el profesor de la asignatura recibe un mensaje de alerta con una prioridad "<prioridad>"

    Ejemplos:
      | promedio |ocasiones|minimo| prioridad |
      |   4.8    |0        |7     |MEDIA      |
      |   6.5    |2        |7     |ALTA       |
      |   4.6    |1        |7     |MEDIA      |
      |   5.5    |2        |7     |ALTA       |
