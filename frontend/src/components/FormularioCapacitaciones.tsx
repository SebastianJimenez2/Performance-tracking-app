import React, { useState } from 'react';
import { Form, Button, Container, Row, Col } from 'react-bootstrap';

function FormularioCapacitacion() {
  const areasIniciales = [
    { id: '1', nombre: 'Marketing' },
    { id: '2', nombre: 'Desarrollo' },
    { id: '3', nombre: 'Recursos Humanos' },
    { id: '4', nombre: 'Finanzas' }
  ];

  const [areaSeleccionada, setAreaSeleccionada] = useState("");

  const manejarCambioArea = (evento: React.ChangeEvent<HTMLSelectElement>) => {
    setAreaSeleccionada(evento.target.value);
  };

  return (
    <div style={{minWidth:'100%', maxHeight:'10%', padding: '20px 20px'}} >
      <Row className="justify-content-center" style={{minWidth:'100%', maxHeight:'20%', }}>
        <Col md={8} lg={6}>
          <h2 className="text-center">Registrar Capacitación</h2>
          <Form>
            <Form.Group className="mb-3" controlId="formCapacitacion">
              <Form.Label>Capacitación:</Form.Label>
              <Form.Control type="text" placeholder="Ingrese el nombre de la capacitación" />
            </Form.Group>

            <Form.Group className="mb-3" controlId="formArea">
              <Form.Label>Área:</Form.Label>
              <Form.Select value={areaSeleccionada} onChange={manejarCambioArea}>
                <option value="">Seleccione un área</option>
                {areasIniciales.map(area => (
                  <option key={area.id} value={area.id}>{area.nombre}</option>
                ))}
              </Form.Select>
            </Form.Group>

            <Form.Group className="mb-3" controlId="formDocumento">
              <Form.Label>Documento:</Form.Label>
              <Form.Control type="file" />
            </Form.Group>

            <div className="d-grid">
              <Button variant="primary" type="submit" style={{
                backgroundColor: '#715BDA'
              }}>
                Registrar
              </Button>
            </div>
          </Form>
        </Col>
      </Row>
    </div>
  );
}

export default FormularioCapacitacion;




