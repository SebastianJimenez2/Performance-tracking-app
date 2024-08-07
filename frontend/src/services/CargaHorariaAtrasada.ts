/**
 * Creado por: David Torres
 */
/**
 * Interfaz para representar un mensaje dentro de una notificación.
 */
export interface Mensaje {
    estado_aspecto: string; // Estado del aspecto (por ejemplo, "Activo", "Inactivo")
    nombre_aspecto: string; // Nombre del aspecto (por ejemplo, "Entrega de tareas")
    fecha_fin: string; // Fecha de fin del aspecto
    estado_notificacion: string; // Estado de la notificación (por ejemplo, "BAJO", "INTENSO")
    progreso_general_porcentaje: number; // Porcentaje de progreso general del aspecto
    tiempo_transcurrido_porcentaje: number; // Porcentaje de tiempo transcurrido
    subaspectos: Array<{ nombre: string; progreso: number }>; // Lista de subaspectos con sus respectivos progresos
}

/**
 * Interfaz para representar una notificación.
 */
export interface Notificacion {
    nombre_aspecto: string; // Nombre del aspecto relacionado con la notificación
    estado_notificacion: string; // Estado de la notificación (por ejemplo, "BAJO", "INTENSO")
    notificaciones_disponibles: boolean; // Indica si hay notificaciones disponibles
    mensaje: Mensaje; // Detalles del mensaje asociado con la notificación
}

/**
 * Interfaz para representar la respuesta de la API que contiene notificaciones.
 */
export interface NotificacionesResponse {
    nombre_docente: string; // Nombre del docente al que pertenecen las notificaciones
    notificaciones: Notificacion[]; // Lista de notificaciones
}

/**
 * Función para obtener notificaciones desde el servidor.
 * @param id_docente - ID del docente para obtener sus notificaciones
 * @returns Una promesa que resuelve con la respuesta de notificaciones
 */
export const obtenerNotificaciones = async (id_docente: number): Promise<NotificacionesResponse> => {
    const url = `https://syncademic-0-1.onrender.com/syncademic/auth/${id_docente}/`;

    return fetch(url, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
        },
    })
        .then((response) => {
            if (!response.ok) {
                throw new Error('Network response was not ok'); // Lanzar un error si la respuesta no es OK
            }
            return response.json(); // Parsear la respuesta JSON
        })
        .then((data) => {
            return data; // Retornar los datos parseados
        })
        .catch((error) => {
            console.error('Fetch error:', error); // Loguear errores de la petición
            throw error; // Lanzar el error para ser manejado por el llamador
        });
};