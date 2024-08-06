# Created by xavic at 22/7/2024
#language: es


Característica: Identificación afinidad de un docente para dictar una asignatura
  Como institución
  quiero identificar aquellos docentes con mayor promedio en las evaluaciones
  integrales de una asignatura particular durante toda su carrera profesional en la institución
  para decidir cuáles tienen mayor afinidad en la asignatura



  #Planificación general de asignaturas

  Esquema del escenario: Identificación de docentes con mayor afinidad a una asignatura
    Dado que existen al menos dos docentes que han impartido la asignatura "<nombre_asignatura>"
    Cuando se solicita identificar el docente con mayor calificación promedio en "<tipo_evaluacion>"
    Entonces se presenta el listado de docentes en orden de mayor a menor con respecto a su calificación
    Ejemplos:
      | nombre_asignatura | tipo_evaluacion |
      | Comunicación      | Heteroevaluacion|
      | Física            | Autoevaluacion  |
      | Química           | Coevaluacion    |
      | Geometría         | Total           |


  Escenario: Sugerencia de docentes con excelente desempeño en su carrera profesional
    Dado que existe uno o ningún docente que ha impartido la asignatura "<nombre_asignatura>"
    Cuando se solicita identificar docentes afines a la asignatura
    Entonces se presenta un listado de sugerencias de docentes con mayor calificación promedio total"







