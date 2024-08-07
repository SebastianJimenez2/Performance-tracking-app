import { Table, Button } from 'react-bootstrap';
import { Profesor } from '../types/Capacitaciones';
import { useContextoGlobal } from '../ContextoGlobal'


function TablaProfesores() {

  const { setProfesor, setPaginaActual } = useContextoGlobal()

  const alHacerClicEnFila = (profesor: Profesor) => {
    setProfesor(profesor);
    setPaginaActual('Profesor');
  };

  const profesores: Profesor[] = [
    { id: 1, nombre: "David Torres Páez", email: "email1@123.com", carrera: "Sistemas", puntaje: 45, urlImagen: 'https://via.placeholder.com/150', encuestaCompletada: false },
    { id: 2, nombre: "David Torres Páez", email: "email1@123.com", carrera: "Sistemas", puntaje: 99, urlImagen: 'https://via.placeholder.com/150', encuestaCompletada: true },
    { id: 3, nombre: "David Torres Páez", email: "email1@123.com", carrera: "Sistemas", puntaje: 95, urlImagen: 'https://via.placeholder.com/150', encuestaCompletada: true },
  ];

  const enviarRecordatorioATodos = () => {
    console.log('Recordatorio enviado a todos.');
  };

  const enviarRecordatorioAIncompletos = () => {
    const profesoresIncompletos = profesores.filter(profesor => !profesor.encuestaCompletada);
    console.log('Recordatorio enviado a los siguientes profesores:', profesoresIncompletos);
  };

  return (
    <div style={{ width: '97%', height: '100%', margin: '20px 20px' }}>
      <Table striped bordered hover className="text-center">
        <thead>
          <tr>
            <th>Nombre</th>
            <th>Email</th>
            <th>Carrera</th>
            <th>Puntaje</th>
            <th>Estado Encuesta</th>
          </tr>
        </thead>
        <tbody>
          {profesores.map(profesor => (
            <tr key={profesor.id} onClick={() => alHacerClicEnFila(profesor)} style={{ cursor: 'pointer' }}>
              <td>
                <div style={{ display: 'flex', alignItems: 'center' }}>
                  <div style={{ marginRight: 8 }}>
                    <img src={profesor.urlImagen} alt="Usuario" style={{ width: 24, height: 24 }} />
                  </div>
                  <div>{profesor.nombre}</div>
                </div>
              </td>
              <td>{profesor.email}</td>
              <td>{profesor.carrera}</td>
              <td style={{ color: profesor.puntaje < 50 ? 'red' : 'green' }}>{profesor.puntaje}</td>
              <td>
                {profesor.encuestaCompletada ? (
                  <span style={{ color: 'green' }}>Completada</span>
                ) : (
                  <span style={{ color: 'red' }}>Pendiente</span>
                )}
              </td>
            </tr>
          ))}
        </tbody>
      </Table>
      
    </div>
  );
}

export default TablaProfesores;