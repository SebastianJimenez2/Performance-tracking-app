# Creado por Grupo 1 at 23/7/24
# language: es

# FEATURE  2
# Creado por: Erika Anrrango, Christian Hernández, Edwin Pillajo


Característica: Distinción de estudiantes propensos a abandonar la asignatura
  Como docente
  Quiero identificar automáticamente aquellos estudiantes con posible tasa de abandono
  Para decidir si notificar a bienestar estudiantil sobre un posible abandono.

  Esquema del escenario: Distinción del riesgo de abandono del estudiante según la asistencia
    Dado un estudiante con tasa de asistencia <tasa_asistencia> % mensual
    Cuando la tasa de asistencia se encuentre entre <minimo> % y <maximo> %
    Entonces se marca al estudiante en riesgo <riesgo> de abandono alertando al docente
    Y él decide <posible_notificacion> notificar a bienestar estudiantil.

    Ejemplos:
      | tasa_asistencia | minimo | maximo | riesgo | posible_notificacion |
      | 50              | 0      | 70     | alto   | si                   |
      | 75              | 71     | 100    | bajo   | no                   |