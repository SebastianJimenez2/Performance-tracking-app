# Created by USER at 27/7/2024
# language: es


Característica: Identificar estudiantes
  Como docente
  quiero identificar estudiantes que se encuentren entre el promedio histórico de estudiantes con problemas
  en la asignatura pre-requisito y el mínimo establecido por la institución.
  para decidir si notificar a bienestar estudiantil sobre una asignación a un curso de verano.

  Escenario: Identificar estudiantes con problemas en asignaturas subsecuentes
    Dado  que el docente desea conocer el promedio histórico con las siguientes notas finales de los estudiantes que cursaron "Programación 1" en el periodo "2024A", y obtuvieron una nota final menor a "7.0" en "Programación 2" en el periodo "2024B"
      | estudiante | nota_materia_subsecuente_periodo_actual | nota_materia_prerequisito_periodo_anterior |
      | Chris      | 5                                       | 6.8                                        |
      | Juan       | 8                                       | 8                                          |
      | Pedro      | 9                                       | 9                                          |
      | Iván       | 4.3                                     | 6                                          |
    Cuando las siguientes notas finales de los estudiante que actualmente están cursando "<asignatura_prerequisito>" se encuentre dentro del rango entre "6.0" y el promedio histórico
      | estudiante | nota_final_materia_prerequisito |
      | Jaime      | 6                               |
      | Sebastian  | 7                               |
      | Cristobal  | 6.02                            |
      | Joseph     | 6.02                            |
      Entonces se listarán los siguientes estudiantes candidatos a tomar un curso vacacional de bienestar estudiantil
        | estudiante |
        | Jaime      |
        | Cristobal  |
        | Joseph     |