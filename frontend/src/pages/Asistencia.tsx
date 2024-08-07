import React, { useState } from "react";
import { Button, Dropdown, Modal, Alert } from "react-bootstrap";
import { Estudiante } from "../types/Asistencia";
import '../styles/pages/Asistencia.css';

type AsistenciaProps = {
  id: string;
};

interface Asistencia {
  id_estudiante: number;
  asistencias: number[];
}

const Asistencia: React.FC<AsistenciaProps> = ({ id }) => {
  const [mesSeleccionado, setMesSeleccionado] = useState<number | null>(null);
  const [showModal, setShowModal] = useState<boolean>(false);
  const [estudianteNotificar, setEstudianteNotificar] = useState<string | null>(null);
  const [mensaje, setMensaje] = useState<string | null>(null);

  const estudiantes: Estudiante[] = [
    { id_estudiante: 1, nombre_estudiante: "Joe Doe" },
    { id_estudiante: 2, nombre_estudiante: "Jill Doe" },
    { id_estudiante: 3, nombre_estudiante: "June Doe" },
    { id_estudiante: 4, nombre_estudiante: "Jiss Doe" }
  ];

  // Asistencias simuladas para 8 semanas (2 meses)
  const estudiantes_asistencias: Asistencia[] = [
    { id_estudiante: 1, asistencias: [1, 1, 0, 1, 0, 1, 0, 0] },
    { id_estudiante: 2, asistencias: [1, 1, 1, 1, 1, 1, 0, 0] },
    { id_estudiante: 3, asistencias: [0, 1, 1, 0, 0, 1, 0, 1] },
    { id_estudiante: 4, asistencias: [1, 0, 0, 0, 1, 0, 0, 0] }
  ];

  const calcularAsistenciasMensuales = (id_estudiante: number, mes: number) => {
    const asistencia = estudiantes_asistencias.find(a => a.id_estudiante === id_estudiante);
    if (!asistencia) return 0;
    const asistenciasMes = asistencia.asistencias.slice((mes - 1) * 4, mes * 4);
    return asistenciasMes.reduce((total, current) => total + current, 0);
  };

  const estudiantes_abandono = estudiantes.filter(estudiante => {
    const asistenciasMes = calcularAsistenciasMensuales(estudiante.id_estudiante, mesSeleccionado || 1);
    return asistenciasMes < 6;
  });

  const handleNotificarClick = (nombre_estudiante: string) => {
    setEstudianteNotificar(nombre_estudiante);
    setShowModal(true);
  };

  const handleCloseModal = () => setShowModal(false);

  const handleNotificarSi = () => {
    setMensaje(`Se envió la notificación a bienestar estudiantil para ${estudianteNotificar}`);
    setShowModal(false);
  };
  const handleRegistrarAsistencia = () => {

  };

  return (
    <div className="asistencia-principal-contenedor">
      <div className="registrar-asistencia-contenedor">
        <Button className="registrar-asistencia" variant="outline-primary" size="lg" onClick={handleRegistrarAsistencia}>
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


