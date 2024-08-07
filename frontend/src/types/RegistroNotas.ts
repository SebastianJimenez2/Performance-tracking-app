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
