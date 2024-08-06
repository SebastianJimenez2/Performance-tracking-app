import { Card, Image, ListGroup } from 'react-bootstrap';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from 'recharts';
import { Profesor } from '../types/Capacitaciones';
import '../styles/components/PerfilProfesor.css';

const datos = [
  { semestre: '2022-A', puntaje: 40 },
  { semestre: '2022-B', puntaje: 45 },
  { semestre: '2023-A', puntaje: 50 },
  { semestre: '2023-B', puntaje: 55 },
  { semestre: '2024-A', puntaje: 60 }
];

function PerfilProfesor({ profesor }: { profesor: Profesor }) {
  return (
    <div className="contenedor-perfil">
      <div className="tarjeta-perfil">
        <Card className="card-profesor">
          <div className="imagen-profesor">
            <Image src={profesor.urlImagen || "https://via.placeholder.com/150"} />
          </div>
          <Card.Body className="body-profesor">
            <Card.Title>{profesor.nombre || "Nombre Desconocido"}</Card.Title>
            <Card.Subtitle className="mb-2 text-muted">{profesor.carrera || "Carrera Desconocida"}</Card.Subtitle>
            <ListGroup variant="flush">
              <ListGroup.Item>Email: {profesor.email || "email@desconocido.com"}</ListGroup.Item>
              <ListGroup.Item>Puntaje actual: {profesor.puntaje || 0}</ListGroup.Item>
            </ListGroup>
          </Card.Body>
        </Card>
        <div className="grafico-profesor">
          <ResponsiveContainer width="100%" height={300}>
            <LineChart data={datos} margin={{ top: 5, right: 20, left: 10, bottom: 5 }}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="semestre" />
              <YAxis />
              <Tooltip />
              <Line type="monotone" dataKey="puntaje" stroke="#8884d8" activeDot={{ r: 8 }} />
            </LineChart>
          </ResponsiveContainer>
        </div>
      </div>
    </div>
  );
}

export default PerfilProfesor;
