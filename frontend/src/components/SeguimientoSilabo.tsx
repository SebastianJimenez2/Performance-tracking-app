/* 

Feature 5: Como docente Quiero saber si mi progreso en la asignatura sigue la proyección del sílab 
  Para adecuar el ritmo de enseñanza de los temas de mi materia.

Grupo 7: 
Joel Delgado (documentación)
David Yánez (backend)
Sebastián Sánchez (frontend)

Documentación asociada:
Mapa navegacional: https://www.figma.com/design/ihvX1EY7yVl6tCnNEyzsZQ/DCU?node-id=0-1&t=qrWYCvKbCMV9MwSR-1

Entidades backend asociadas: docente, cronograma, tema_cronograma, asignatura

Sección de la feature abordada en esta pantalla:
Visualización del seguimiento del sílabo de la asignatura
*/

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
import { useContextoGlobal } from '../ContextoGlobal';
import { obtenerCronogramas, obtenerTemasCronograma } from '../services/Cronograma';
import { TemaCronograma } from '../types/Cronograma';

ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
);

const options: ChartOptions<'line'> = {
  responsive: true,
  plugins: {
    legend: {
      position: 'top',
    },
    title: {
      display: true,
      text: 'Seguimiento del sílabo',
    },
  },
  scales: {
    x: {
      title: {
        display: true,
        text: 'Temas',
      },
    },
    y: {
      title: {
        display: true,
        text: 'Tiempo en semanas',
      },
      ticks: {
        stepSize: 1,
      },
    },
  },
};

const calculateWeeksBetweenDates = (startDate: string, endDate: string): number => {
  const start = new Date(startDate);
  const end = new Date(endDate);
  const diffTime = Math.abs(end.getTime() - start.getTime());
  return Math.ceil(diffTime / (1000 * 60 * 60 * 24 * 7));
};

function SeguimientoSilabo({ id, handlePageChange, showNotification }: { id: string, handlePageChange: (page: string) => void, showNotification: boolean }) {
  const { asignatura } = useContextoGlobal();
  const [data, setData] = useState<ChartData<'line'>>({ labels: [], datasets: [] });
  const [estado, setEstado] = useState<string>('normal');

  useEffect(() => {
    const fetchData = async () => {
      try {
        const cronogramas = await obtenerCronogramas();
        const cronograma = cronogramas.find(c => c.asignatura === asignatura);
        if (cronograma) {
          let estadoGeneral = 'normal';
          const temas = await obtenerTemasCronograma(cronograma.id_cronograma);

          const labels = temas.map(t => t.descripcion);
          const proyeccionIdeal = temas.map(t => t.semana_finalizacion_relativa_a_inicio);
          const avanceReal = temas
            .filter(t => t.completado && t.fecha_completado !== null)
            .map(t => {
              const weeks = calculateWeeksBetweenDates(cronograma.fecha_inicio, t.fecha_completado!);
              if (weeks < t.semana_finalizacion_relativa_a_inicio) {
                estadoGeneral = 'adelantado';
              } else if (weeks > t.semana_finalizacion_relativa_a_inicio) {
                estadoGeneral = 'atrasado';
              }
              return weeks;
            });

          setEstado(estadoGeneral);

          setData({
            labels,
            datasets: [
              {
                label: 'Proyección ideal',
                data: proyeccionIdeal,
                borderColor: 'rgba(75,192,192,1)',
                backgroundColor: 'rgba(75,192,192,0.2)',
                tension: 0.4,
              },
              {
                label: 'Avance real',
                data: avanceReal,
                borderColor: 'rgba(192,75,192,1)',
                backgroundColor: 'rgba(192,75,192,0.2)',
                tension: 0.4,
              },
            ],
          });
        }
      } catch (error) {
        console.error("Error fetching data:", error);
      }
    };

    fetchData();
  }, [asignatura]);

  const handleRegisterClick = () => {
    handlePageChange('RegistroAvance');
  };

  const mensajeEstado = {
    atrasado: "Parece que estás un poco por detrás de lo esperado, recomendamos apresurar el paso con los siguientes temas",
    adelantado: "Todo está en orden, sigue así"
  };

  return (
    <div id={id} className="container">
      <h1 className="title">Seguimiento del sílabo</h1>
      <div className="chartContainer">
        <Line data={data} options={options} />
      </div>
      <div className="textContainer">
        <p className="text">{mensajeEstado[estado]}</p>
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
