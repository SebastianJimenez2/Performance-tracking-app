import React, { useState, useEffect } from 'react';
import { Modal, Button, Alert } from 'react-bootstrap';
import '../styles/components/RegistroAvance.css';
import { useContextoGlobal } from '../ContextoGlobal';
import { obtenerTemasCronograma, obtenerCronogramas } from '../services/Cronograma';
import { actualizarEstadoTema } from '../services/TemasCronograma';
import { TemaCronograma } from '../types/Cronograma';

function RegistroAvance({ id, handlePageChange }: { id: string, handlePageChange: (page: string) => void }) {
  const { asignatura } = useContextoGlobal();
  const [temas, setTemas] = useState<TemaCronograma[]>([]);
  const [selectedTemas, setSelectedTemas] = useState<{ [key: number]: boolean }>({});
  const [showModal, setShowModal] = useState(false);
  const [showAlert, setShowAlert] = useState(false);

  useEffect(() => {
    const fetchTemas = async () => {
      try {
        const cronogramas = await obtenerCronogramas();
        const cronograma = cronogramas.find(c => c.asignatura === asignatura);
        if (cronograma) {
          const temas = await obtenerTemasCronograma(cronograma.id_cronograma);
          setTemas(temas.filter(t => !t.completado));
        }
      } catch (error) {
        console.error("Error fetching temas:", error);
      }
    };

    fetchTemas();
  }, [asignatura]);

  const handleCheckChange = (idTema: number, index: number) => {
    const prevTema = temas[index - 1];
    if (index > 0 && !selectedTemas[prevTema.id_tema]) {
      setShowAlert(true);
    } else {
      setSelectedTemas(prev => ({
        ...prev,
        [idTema]: !prev[idTema]
      }));
      setShowAlert(false);
    }
  };

  const handleSave = () => {
    const temasMarcados = Object.values(selectedTemas).some(value => value);
    if (temasMarcados) {
      setShowModal(true);
    } else {
      handlePageChange('SeguimientoSilabo');
    }
  };

  const confirmSave = async () => {
    try {
      const currentDate = new Date().toISOString().split('T')[0];
      const cronogramas = await obtenerCronogramas();
      const cronograma = cronogramas.find(c => c.asignatura === asignatura);

      if (cronograma) {
        await Promise.all(
          Object.keys(selectedTemas).map(idTema => {
            if (selectedTemas[+idTema]) {
              const tema = temas.find(t => t.id_tema === +idTema);
              if (tema) {
                const weeksCurrent = Math.floor((new Date(currentDate).getTime() - new Date(cronograma.fecha_inicio).getTime()) / (1000 * 60 * 60 * 24 * 7));
                const estado = weeksCurrent < tema.semana_finalizacion_relativa_a_inicio
                  ? 'adelantado'
                  : weeksCurrent > tema.semana_finalizacion_relativa_a_inicio
                  ? 'atrasado'
                  : 'normal';
                return actualizarEstadoTema(+idTema, currentDate, estado);
              }
            }
            return Promise.resolve();
          })
        );
      }

      setShowModal(false);
      handlePageChange('SeguimientoSilabo');
    } catch (error) {
      console.error("Error saving temas:", error);
    }
  };

  const cancelSave = () => {
    setShowModal(false);
    handlePageChange('SeguimientoSilabo');
  };

  return (
    <div id={id} className="container">
      <h1 className="title">Registro de Avance</h1>
      {showAlert && <Alert variant="warning">Por favor registra tu avance en orden</Alert>}
      <div className="tableContainer">
        <table className="table">
          <thead>
            <tr>
              <th>Tema</th>
              <th>Semana de Finalización</th>
              <th>Completado</th>
            </tr>
          </thead>
          <tbody>
            {temas.map((tema, index) => (
              <tr key={tema.id_tema}>
                <td>{tema.descripcion}</td>
                <td>{tema.semana_finalizacion_relativa_a_inicio}</td>
                <td>
                  <input
                    type="checkbox"
                    checked={selectedTemas[tema.id_tema] || false}
                    onChange={() => handleCheckChange(tema.id_tema, index)}
                  />
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
      <button className="button" onClick={handleSave}>
        Guardar Avance
      </button>

      <Modal show={showModal} onHide={cancelSave}>
        <Modal.Header closeButton>
          <Modal.Title>Confirmación</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          ¿Estás seguro de que deseas guardar los cambios?
        </Modal.Body>
        <Modal.Footer className="modal-footer-custom">
          <Button variant="primary" onClick={confirmSave} className="modal-button">
            Sí
          </Button>
          <Button variant="secondary" onClick={cancelSave} className="modal-button">
            No
          </Button>
        </Modal.Footer>
      </Modal>
    </div>
  );
}

export default RegistroAvance;
