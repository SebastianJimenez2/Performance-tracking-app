import { Card, Image, ListGroup } from 'react-bootstrap';
import { Line } from 'react-chartjs-2';
import { Chart, CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend } from 'chart.js';
import { Profesor } from '../types/Capacitaciones';
import '../styles/components/PerfilProfesor.css';

// Registrar los componentes de Chart.js
Chart.register(CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend);

const datos = {
  labels: ['2022-A', '2022-B', '2023-A', '2023-B', '2024-A'],
  datasets: [
    {
      label: 'Puntaje',
      data: [40, 45, 50, 55, 60],
      fill: false,
      backgroundColor: '#8884d8',
      borderColor: '#8884d8',
      tension: 0.1
    }
  ]
};

const opciones = {
  responsive: true,
  plugins: {
    legend: {
      display: false
    }
  }
};

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
          <Line data={datos} options={opciones} />
        </div>
      </div>
    </div>
  );
}

export default PerfilProfesor;