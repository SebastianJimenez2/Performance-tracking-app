import React, { useEffect, useState } from 'react';
import { Line } from 'react-chartjs-2';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
  ChartOptions,
  ChartData
} from 'chart.js';
import '../styles/components/SeguimientoSilabo.css';

ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
);

const data: ChartData<'line'> = {
  labels: ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo'],
  datasets: [
    {
      label: 'Progreso',
      data: [3, 2, 5, 4, 6],
      borderColor: 'rgba(75,192,192,1)',
      backgroundColor: 'rgba(75,192,192,0.2)',
      tension: 0.4,
    },
  ],
};

const options: ChartOptions<'line'> = {
  responsive: true,
  plugins: {
    legend: {
      position: 'top',
    },
    title: {
      display: true,
      text: 'Seguimiento de Sílabo',
    },
  },
};

function SeguimientoSilabo({ id, handlePageChange }: { id: string, handlePageChange: (page: string) => void }) {
  const [showNotification, setShowNotification] = useState(false);

  useEffect(() => {
    const params = new URLSearchParams(window.location.search);
    if (params.get('avanceGuardado') === 'true') {
      setShowNotification(true);
      setTimeout(() => setShowNotification(false), 3000);
    }
  }, []);

  const handleRegisterClick = () => {
    handlePageChange('RegistroAvance');
  };

  return (
    <div id={id} className="container">
      <h1 className="title">Seguimiento del sílabo</h1>
      <div className="chartContainer">
        <Line data={data} options={options} />
      </div>
      <div className="textContainer">
        <p className="text">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer nec odio. Praesent libero. Sed cursus ante dapibus diam.</p>
      </div>
      <button className="button" onClick={handleRegisterClick}>
        Registrar Avance
      </button>
      {showNotification && (
        <div className="notification">
          <p>Avance guardado con éxito.</p>
        </div>
      )}
    </div>
  );
}

export default SeguimientoSilabo;
