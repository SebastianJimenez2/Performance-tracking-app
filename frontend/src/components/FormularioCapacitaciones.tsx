import React, { useState } from 'react';
import { Form, Button, Container, Row, Col } from 'react-bootstrap';

function TrainingRegistration() {
  const initialAreas = [
    { id: '1', name: 'Marketing' },
    { id: '2', name: 'Desarrollo' },
    { id: '3', name: 'Recursos Humanos' },
    { id: '4', name: 'Finanzas' }
  ];

  const [selectedArea, setSelectedArea] = useState("");

  const handleAreaChange = (event: React.ChangeEvent<HTMLSelectElement>) => {
    setSelectedArea(event.target.value);
  };

  return (
    <Container className="mt-5" >
      <Row className="justify-content-center">
        <Col md={8} lg={6}>
          <h2 className="text-center">Registrar Capacitación</h2>
          <Form>
            <Form.Group className="mb-3" controlId="formTraining">
              <Form.Label>Capacitación:</Form.Label>
              <Form.Control type="text" placeholder="Ingrese el nombre de la capacitación" />
            </Form.Group>

            <Form.Group className="mb-3" controlId="formArea">
              <Form.Label>Área:</Form.Label>
              <Form.Select value={selectedArea} onChange={handleAreaChange}>
                <option value="">Seleccione un área</option>
                {initialAreas.map(area => (
                  <option key={area.id} value={area.id}>{area.name}</option>
                ))}
              </Form.Select>
            </Form.Group>

            <Form.Group className="mb-3" controlId="formFile">
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
    </Container>
  );
}

export default TrainingRegistration;



