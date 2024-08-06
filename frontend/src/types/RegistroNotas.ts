export type Estudiante = {
    id_estudiante: number,
    nombre_estudiante: string,
    email: string,
    numero_incidencias: number,
    prioridad: string,
    promedio: number
}

export type Nota = {
    id_estudiante: number,
    nombre: string,
    nota: number,
    tema: string,
    tipo_actividad: number
}

export type RespuestaRegistroNotas = {
    en_riesgo: number,
    alerta_media: number,
    alerta_alta: number
}
