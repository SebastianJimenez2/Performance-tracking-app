import { useState } from 'react';
import { Table, Button, Form } from 'react-bootstrap';
import file from '../assets/file.svg';

function TablaCapacitaciones() {
  const cursos = [
    { id: 1, nombre: "Curso 1", area: "Mecánica", semestre: "2024-A", urlDocumento: "url-to-download-document-1.pdf" },
    { id: 2, nombre: "Curso 2", area: "Economía", semestre: "2023-B", urlDocumento: "url-to-download-document-2.pdf" },
    { id: 3, nombre: "Curso 3", area: "Sistemas", semestre: "2024-A", urlDocumento: "url-to-download-document-3.pdf" }
  ];

  const [semestreSeleccionado, setSemestreSeleccionado] = useState('2024-A'); // Estado para el semestre seleccionado

  const manejarDescarga = (url: string): void => {
    const enlace = document.createElement('a');
    enlace.href = url;
    enlace.setAttribute('download', '');
    document.body.appendChild(enlace);
    enlace.click();
    document.body.removeChild(enlace);
  };

  const cursosFiltrados = cursos.filter(curso => curso.semestre === semestreSeleccionado);

  return (
    <div style={{ maxWidth: '80%', margin: '2rem auto' }}>
      <Form.Select
        aria-label="Selecciona un semestre"
        value={semestreSeleccionado}
        onChange={e => setSemestreSeleccionado(e.target.value)}
        style={{ marginBottom: '20px', width: '15%', justifyContent: 'center' }}
      >
        <option value="2024-A">2024-A</option>
        <option value="2023-B">2023-B</option>
      </Form.Select>
      <Table striped bordered hover className="text-center">
        <thead>
          <tr>
            <th>Capacitación</th>
            <th>Área</th>
            <th>Semestre</th>
            <th>Documento</th>
          </tr>
        </thead>
        <tbody>
          {cursosFiltrados.map(curso => (
            <tr key={curso.id}>
              <td>{curso.nombre}</td>
              <td>{curso.area}</td>
              <td>{curso.semestre}</td>
              <td>
                <Button variant="link" onClick={() => manejarDescarga(curso.urlDocumento)}>
                  <img src={file} alt="Descargar" style={{ width: 24, height: 24 }} />
                </Button>
              </td>
            </tr>
          ))}
        </tbody>
      </Table>
    </div>
  );
}

export default TablaCapacitaciones;
