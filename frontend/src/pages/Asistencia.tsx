/**Feature1:Distinción de estudiantes propensos a abandonar la asignatura
 * Como docente
  Quiero identificar automáticamente aquellos estudiantes con posible tasa de abandono
  Para decidir si notificar a bienestar estudiantil sobre un posible abandono.
 * Integrantes:
  Anrrango Erika -> Desarrolladora FrontEnd
  Hernández Christian -> Desarrollador BackEnd
  Pillajo Edwin -> Documentación
 * https://www.figma.com/design/ihvX1EY7yVl6tCnNEyzsZQ/DCU?node-id=0-1&t=xo35RUXDQw3SNzwP-1
 * En el Wireframe
    Ver Asistencia
    Notificacion Propenso Abandono
 */

    import React, { useState } from "react";
    import { Button, Dropdown, Modal, Alert } from "react-bootstrap";
    import { useContextoGlobal } from "../ContextoGlobal";
    import '../styles/pages/Asistencia.css';
    
    // Definición de las propiedades del componente
    type AsistenciaProps = {
      id: string;
    };
    
    // Definición del tipo Asistencia para el estado de las asistencias de los estudiantes
    interface Asistencia {
      id_estudiante: number;
      asistencias: number[]; // 1 representa asistencia y 0 representa falta
    }
    
    // Componente funcional Asistencia
    const Asistencia: React.FC<AsistenciaProps> = ({ id }) => {
      const { listaEstudiantes } = useContextoGlobal(); // Obtiene la lista de estudiantes desde el contexto global
      const [mesSeleccionado, setMesSeleccionado] = useState<number | null>(null); // Estado para el mes seleccionado
      const [showModal, setShowModal] = useState<boolean>(false); // Estado para mostrar el modal
      const [estudianteNotificar, setEstudianteNotificar] = useState<string | null>(null); // Estado para el estudiante a notificar
      const [mensaje, setMensaje] = useState<string | null>(null); // Estado para el mensaje de notificación
    
      // Asistencias simuladas para 16 clases (4 meses)
      const estudiantes_asistencias: Asistencia[] = [
        { id_estudiante: 1, asistencias: [1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1] },
        { id_estudiante: 2, asistencias: [1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1] },
        { id_estudiante: 3, asistencias: [0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0] },
        { id_estudiante: 4, asistencias: [1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0] },
        { id_estudiante: 5, asistencias: [1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1] },
      ];
    
      // Calcula las asistencias mensuales de un estudiante
      const calcularAsistenciasMensuales = (id_estudiante: number, mes: number) => {
        const asistencia = estudiantes_asistencias.find(a => a.id_estudiante === id_estudiante);
        if (!asistencia) return 0;
        const semanasPorMes = 8; // Suponiendo 4 semanas por mes y 2 asistencias por semana
        const inicio = (mes - 1) * semanasPorMes;
        const fin = Math.min(mes * semanasPorMes, asistencia.asistencias.length);
        const asistenciasMes = asistencia.asistencias.slice(inicio, fin);
        return asistenciasMes.reduce((total, current) => total + current, 0);
      };
    
      // Filtra los estudiantes con riesgo de abandono
      const estudiantes_abandono = listaEstudiantes.filter(estudiante => {
        const mes = mesSeleccionado || 1;
        const asistenciasMes = calcularAsistenciasMensuales(estudiante.id_estudiante, mes);
        return asistenciasMes < 6 && asistenciasMes > 0;
      });
    
      // Maneja el click para notificar a bienestar estudiantil
      const handleNotificarClick = (nombre_estudiante: string) => {
        setEstudianteNotificar(nombre_estudiante);
        setShowModal(true);
      };
    
      // Cierra el modal
      const handleCloseModal = () => setShowModal(false);
    
      // Maneja la confirmación de notificación
      const handleNotificarSi = () => {
        setMensaje(`Se envió la notificación a bienestar estudiantil para ${estudianteNotificar}`);
        setShowModal(false);
      };
    
      // Lógica para registrar asistencia (a implementar)
      const handleRegistrarAsistencia = () => {
        // Lógica para registrar asistencia
      };
    
      return (
        <div className="asistencia-principal-contenedor">
          <div className="registrar-asistencia-contenedor">
            <Button className="registrar-asistencia" variant="outline-primary" onClick={handleRegistrarAsistencia}>
              Registrar Asistencia
            </Button>
          </div>
          <br />
          {mensaje && <Alert variant="success">{mensaje}</Alert>}
          <div className="estudiantes-abandono-contenedor">
            <div className="izquierdo-contenedor"></div>
            <div className="tasa-abandono-contenedor">
              <div className="tasa-abandono-info-contenedor">
                <h2>Estudiantes propensos a abandono</h2>
                <div className="selector-medida-mes">
                  <Dropdown id="seleccion-mes">
                    <Dropdown.Toggle variant="primary">
                      {mesSeleccionado ? `Mes ${mesSeleccionado}` : "Seleccione mes"}
                    </Dropdown.Toggle>
                    <Dropdown.Menu>
                      {Array.from({ length: 4 }, (_, i) => (
                        <Dropdown.Item
                          key={i}
                          id={`mes${i + 1}`}
                          onClick={() => setMesSeleccionado(i + 1)}
                        >
                          {i + 1}
                        </Dropdown.Item>
                      ))}
                    </Dropdown.Menu>
                  </Dropdown>
                </div>
              </div>
              <ul className="lista-estudiantes">
                {estudiantes_abandono.map((estudiante, index) => (
                  <li key={index} className="estudiante-item">
                    <span>{estudiante.nombre_estudiante}</span>
                    <span>{`Asistencias: ${calcularAsistenciasMensuales(estudiante.id_estudiante, mesSeleccionado || 1)}`}</span>
                    <Button
                      className="notificar-button"
                      variant="danger"
                      onClick={() => handleNotificarClick(estudiante.nombre_estudiante)}
                    >
                      Notificar
                    </Button>
                  </li>
                ))}
              </ul>
            </div>
            <div className="derecho-contenedor"></div>
          </div>
    
          <Modal show={showModal} onHide={handleCloseModal}>
            <Modal.Header closeButton>
              <Modal.Title>Notificación</Modal.Title>
            </Modal.Header>
            <Modal.Body>
              ¿Desea notificar a bienestar estudiantil del posible abandono de asignatura de {estudianteNotificar}?
            </Modal.Body>
            <Modal.Footer>
              <Button variant="secondary" onClick={handleCloseModal}>
                No
              </Button>
              <Button variant="primary" onClick={handleNotificarSi}>
                Sí
              </Button>
            </Modal.Footer>
          </Modal>
        </div>
      );
    };
    
    export default Asistencia;
    