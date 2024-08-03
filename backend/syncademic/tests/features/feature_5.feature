# language: es

Característica: Seguimiento del progreso del Sílabo de docentes
  Como docente
  Quiero saber si mi progreso en la asignatura sigue la proyección del sílabo
  Para adecuar el ritmo de enseñanza de los temas de mi materia.

  Esquema del escenario: Verificación del progreso académico del docente según el cronograma
    Cuando el docente visualiza su progreso de la semana <semana_actual> en base a que <temas_marcados>
    Entonces se visualiza un progreso <estado> respecto a la proyección ideal
    Ejemplos:
      |semana_actual  | estado      | temas_marcados                                          |
      |2              | normal      | Todos los temas hasta la semana actual están marcados   |
      |3              | atrasado    | Faltan temas por marcar en la semana actual             |
      |1              | adelantado  | Temas de semanas futuras están marcados                 |