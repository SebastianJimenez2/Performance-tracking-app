# Created by Grupo01 at 27/7/2024
# language: es


Característica: Identificar estudiantes
  Como docente
  quiero identificar estudiantes que se encuentren entre el promedio histórico de estudiantes con problemas
  en la asignatura pre-requisito y el mínimo establecido por la institución.
  para decidir si notificar a bienestar estudiantil sobre una asignación a un curso de verano.


  Escenario: Identificar a los estudiantes con problemas en aquellas asignaturas que tienen una asignatura prerequisito.
    Dado que el docente desea conocer el promedio histórico con las siguientes notas finales de los estudiantes que cursaron "Programacion1" en el periodo "2024A", y obtuvieron una nota final menor a "6.0" en "Programacion2" en el periodo "2024B"
      | estudiante        | nota_materia_subsecuente_periodo_actual | nota_materia_prerequisito_periodo_anterior |
      | Chris Suarez      | 5                                       | 6.8                                        |
      | Juan Piedra       | 8                                       | 8                                          |
      | Pedro Lissan      | 9                                       | 9                                          |
      | Iván Maerno       | 4.3                                     | 6                                          |
    Cuando las siguientes notas finales de los estudiantes que actualmente están cursando la asignatura prerequisito se encuentren dentro del rango entre "6.0" y el promedio histórico
      | estudiante        | nota_final_materia_prerequisito |
      | Jaime Lotoya      | 6                               |
      | Sebastian Jipila  | 7                               |
      | Cristobal Flores  | 6.02                            |
      | Joseph Chance     | 6.02                            |
    Entonces se listarán los siguientes estudiantes candidatos a tomar un curso vacacional de bienestar estudiantil
      | estudiante        |
      | Jaime Lotoya      |
      | Sebastian Jipila  |
      | Joseph Chance     |

  Escenario: Manifestar la imposibilidad de identificar a los estudiantes con problemas en aquellas asignaturas que no tienen una asignatura subsecuente.
    Dado que el docente desea saber el promedio histórico de notas finales de los estudiantes de la materia "Comunicacion" en el periodo actual "2024B"
    Cuando se determine que no es posible identificar a los estudiantes con problemas debido a que la asignatura indicada no tiene una asignatura subsecuente
    Entonces se emitirá un mensaje manifestando la imposibilidad



