export type Cronograma = {
    id_cronograma: number;
    asignatura: number;
    estado: string;
    fecha_inicio: string;
  }
  
  export type TemaCronograma = {
    id_tema: number;
    descripcion: string;
    orden: number;
    tiempo_en_semanas: number;
    completado: boolean;
    semana_finalizacion_relativa_a_inicio: number;
    fecha_completado: string | null;
  }
  