export interface Asistencia {
    id_estudiante: number;
    asistencias: number[]; // 1 representa asistencia y 0 representa falta
  }
  
  export interface Estudiante {
    id_estudiante: number;
    nombre_estudiante: string;
  }
  
  export interface EstudiantesEnRiesgoResponse {
    estudiantes: Estudiante[];
    asistencias: Asistencia[];
  }
  