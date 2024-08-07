import React, { useState } from 'react';
import { Modal, Button } from 'react-bootstrap';
import '../styles/components/RegistroAvance.css';

function RegistroAvance({ id, handlePageChange }: { id: string, handlePageChange: (page: string) => void }) {
  const [showModal, setShowModal] = useState(false);

  const handleSave = () => {
    setShowModal(true);
  };

  const confirmSave = () => {
    setShowModal(false);
    handlePageChange('SeguimientoSilabo');
  };

  return (
    <div id={id} className="container">
      <h1 className="title">Registro de avance</h1>
      <div className="tableContainer">
        <table className="table">
          <thead>
            <tr>
              <th>Tema</th>
              <th>Semana</th>
              <th>Completado</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Tema 1</td>
              <td>Semana 1</td>
              <td><input type="checkbox" /></td>
            </tr>
            <tr>
              <td>Tema 2</td>
              <td>Semana 2</td>
              <td><input type="checkbox" /></td>
            </tr>
            <tr>
              <td>Tema 3</td>
              <td>Semana 3</td>
              <td><input type="checkbox" /></td>
            </tr>
          </tbody>
        </table>
      </div>
      <button className="button" onClick={handleSave}>
        Guardar Avance
      </button>

      <Modal show={showModal} onHide={() => setShowModal(false)}>
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
          <Button variant="secondary" onClick={() => setShowModal(false)} className="modal-button">
            No
          </Button>
        </Modal.Footer>
      </Modal>
    </div>
  );
}

export default RegistroAvance;
