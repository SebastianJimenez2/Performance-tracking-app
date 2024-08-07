/*
Feature a la que responde este componente:
    F6: Control de Carga Horaria Atrasada

    Como institución quiero que se notifique automáticamente el estado de la 
	carga horaria atrasada de cada docente para prevenir el incumplimiento 
	de sus respectivos horas de docencia.

Grupo encargado: Grupo 5
    - David Averos (Backend)
    - Gary Campaña (Documentación)
    - David Torres (Frontend)

Documentación asociada:
    Mapa navegacional y wireframe: https://www.figma.com/design/ihvX1EY7yVl6tCnNEyzsZQ/DCU?node-id=0-1
    Tokens de diseño: https://www.figma.com/design/ihvX1EY7yVl6tCnNEyzsZQ/DCU?node-id=116-2

Entidades backend involucradas: Docente, Aspecto, Notificacion.

Sección de la feature abordada en este componente:
    Alertas de tipo notificacion para avisar al docente el retraso del registro de su carga horaria en diferentes aspectos.
*/
/**
 * Creado por: David Torres
 */

import React, { useState, useEffect, useImperativeHandle, forwardRef } from 'react';
import Toast from 'react-bootstrap/Toast';
import ToastContainer from 'react-bootstrap/ToastContainer';
import Button from 'react-bootstrap/Button';
import Modal from 'react-bootstrap/Modal';
import { useContextoGlobal } from '../ContextoGlobal';
import { obtenerNotificaciones, Notificacion } from '../services/CargaHorariaAtrasada';

import 'bootstrap/dist/css/bootstrap.min.css';
import '../styles/components/CargaHorariaAtrasada.css';

/**
 * Componente `CargaHorariaAtrasada`
 * Este componente muestra notificaciones periódicas sobre carga horaria atrasada utilizando `Toast` de React Bootstrap.
 * Incluye un modal para mostrar detalles adicionales de cada notificación.
 */
const CargaHorariaAtrasada = forwardRef((_, ref) => {
    const [notificaciones, setNotificaciones] = useState<Notificacion[]>([]);
    const [showModal, setShowModal] = useState(false);
    const [notificacionSeleccionada, setNotificacionSeleccionada] = useState<Notificacion | null>(null);
    const { setPaginaActual } = useContextoGlobal();
    const id_docente = 3;

    // Exponer una función para recargar notificaciones a través de la referencia
    useImperativeHandle(ref, () => ({
        recargarNotificaciones: fetchNotificaciones,
    }));

    useEffect(() => {
        // Función para obtener las notificaciones iniciales
        const fetchInitialNotificaciones = async () => {
            await fetchNotificaciones();
        };
        fetchInitialNotificaciones();

        // Configurar un intervalo para obtener notificaciones cada 5 minutos
        const timer = setInterval(fetchNotificaciones, 300000); // Cada 5 minutos

        // Limpiar el intervalo cuando el componente se desmonte
        return () => clearInterval(timer);
    }, [id_docente]);

    /**
     * Función para obtener las notificaciones desde el servicio `obtenerNotificaciones`
     */
    const fetchNotificaciones = async () => {
        try {
            const data = await obtenerNotificaciones(id_docente);

            // Filtrar las notificaciones activas
            const notificacionesActivas = data.notificaciones.filter(
                (n) => n.notificaciones_disponibles && n.mensaje.estado_aspecto === 'Activo'
            );

            setNotificaciones(notificacionesActivas);
        } catch (error) {
            console.error('Error fetching notifications:', error);
        }
    };

    /**
     * Función para obtener el color de fondo del `Toast` según el estado de la notificación
     */
    const getToastColor = (estado: string) => {
        switch (estado) {
            case 'BAJO':
            case 'NORMAL':
                return 'lightblue';
            case 'INTENSO':
                return 'orange';
            case 'CRITICO':
                return 'red';
            default:
                return 'white';
        }
    };

    /**
     * Función para manejar el cierre de un `Toast`
     */
    const handleClose = (index: number) => {
        setNotificaciones((prevNotificaciones) => prevNotificaciones.filter((_, i) => i !== index));
    };

    /**
     * Función para manejar la visualización de más detalles de una notificación en el modal
     */
    const handleViewMore = (notificacion: Notificacion) => {
        setNotificacionSeleccionada(notificacion);
        setShowModal(true);
    };

    /**
     * Función para manejar el cierre del modal
     */
    const handleCloseModal = () => {
        setShowModal(false);
        setNotificacionSeleccionada(null);
    };

    return (
        <>
            {/* Contenedor de notificaciones (Toast) */}
            <ToastContainer position="top-end" className="p-3" style={{ zIndex: 1050, position: 'fixed', top: '120px' }}>
                {notificaciones.map((notificacion, index) => (
                    <Toast
                        key={index}
                        onClose={() => handleClose(index)}
                        delay={10000}
                        autohide
                        style={{ backgroundColor: getToastColor(notificacion.mensaje.estado_notificacion) }}
                    >
                        <Toast.Header closeButton>
                            <strong className="me-auto">Notificación</strong>
                        </Toast.Header>
                        <Toast.Body>
                            <strong>
                                {notificacion.mensaje.nombre_aspecto} - {notificacion.mensaje.estado_notificacion}
                            </strong>
                            <div className="mt-2">
                                <Button
                                    variant="link"
                                    style={{ padding: 0 }}
                                    onClick={() => handleViewMore(notificacion)}
                                >
                                    <strong>Ver más</strong>
                                </Button>
                            </div>
                        </Toast.Body>
                    </Toast>
                ))}
            </ToastContainer>

            {/* Modal para mostrar detalles de la notificación */}
            {notificacionSeleccionada && (
                <Modal show={showModal} onHide={handleCloseModal} centered>
                    <Modal.Header closeButton>
                        <Modal.Title>Detalles de la <noscript></noscript>notificación</Modal.Title>
                    </Modal.Header>
                    <Modal.Body>
                        <h5><strong>Retraso de horas en: </strong> {notificacionSeleccionada.mensaje.nombre_aspecto}</h5>
                        <p><strong>Fecha de fin: </strong> {notificacionSeleccionada.mensaje.fecha_fin}</p>
                        <p><strong>Progreso actual: </strong> {notificacionSeleccionada.mensaje.progreso_general_porcentaje}%</p>
                    </Modal.Body>
                    <Modal.Footer>
                        <Button variant="secondary" onClick={handleCloseModal}>
                            Cerrar
                        </Button>
                    </Modal.Footer>
                </Modal>
            )}
        </>
    );
});

export default CargaHorariaAtrasada;