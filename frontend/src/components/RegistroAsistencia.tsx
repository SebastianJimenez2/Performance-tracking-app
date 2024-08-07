// Importa los hooks de React y componentes de React-Bootstrap
import React, { useState, useEffect } from 'react';
import { Dropdown, Button, Form, Alert } from 'react-bootstrap';
// Importa el contexto global y estilos
import { useContextoGlobal } from '../ContextoGlobal';
import '../styles/components/RegistroAsistencia.css';
// Importa el tipo de datos de estudiantes
import { Estudiante } from '../types/Estudiantes';

// Define las propiedades que recibe el componente
type RegistroAsistenciaProps = {
  id: string;
};

// Define la interfaz para el estado de asistencia
interface Asistencia {
  id_estudiante: number;
  presente: boolean;
}

// Define el componente funcional
const RegistroAsistencia: React.FC<RegistroAsistenciaProps> = ({ id }) => {
  // Extrae la lista de estudiantes del contexto global
  const { listaEstudiantes } = useContextoGlobal();
  // Define los estados locales
  const [semana, setSemana] = useState<string | null>(null);
  const [horario, setHorario] = useState<string | null>(null);
  const [asistencias, setAsistencias] = useState<Asistencia[]>([]);
  const [mensaje, setMensaje] = useState<string | null>(null);
  const [mostrarSiguienteSemana, setMostrarSiguienteSemana] = useState<boolean>(false);
  const [registrosPorSemana, setRegistrosPorSemana] = useState<{ [key: string]: number }>({});

  // Define los horarios disponibles
  const horarios = [
    "11:00-13:00",
    "15:00-17:00"
  ];

  // Efecto para limpiar el mensaje después de 2 segundos
  useEffect(() => {
    if (mensaje) {
      const timer = setTimeout(() => {
        setMensaje(null);
      }, 2000);
      return () => clearTimeout(timer);
    }
  }, [mensaje]);

  // Maneja el cambio de estado de las asistencias
  const handleCheckChange = (id_estudiante: number) => {
    setAsistencias((prevAsistencias) => {
      const index = prevAsistencias.findIndex(asistencia => asistencia.id_estudiante === id_estudiante);
      if (index !== -1) {
        const updatedAsistencias = [...prevAsistencias];
        updatedAsistencias[index].presente = !updatedAsistencias[index].presente;
        return updatedAsistencias;
      }
      return [...prevAsistencias, { id_estudiante, presente: true }];
    });
  };

  // Maneja el click en el botón de registrar
  const handleRegistrarClick = () => {
    if (semana && horario) {
      const registro = {
        semana,
        horario,
        asistencias,
      };
      console.log('Asistencia registrada', registro);
      setMensaje('Registro exitoso de asistencia');

      // Resetea los estados después de registrar
      setAsistencias([]);
      setSemana(null);
      setHorario(null);

      // Actualiza el contador de registros por semana
      setRegistrosPorSemana((prevRegistros) => {
        const count = prevRegistros[semana] || 0;
        return { ...prevRegistros, [semana]: count + 1 };
      });

      setMostrarSiguienteSemana(true);
    }
  };

  // Verifica si la semana está completa (dos registros)
  const isSemanaCompleta = semana ? (registrosPorSemana[semana] || 0) >= 2 : false;

  return (
    <div id={id} className="asistencia-contenedor">
      <h2>Registro de asistencia</h2>
      {mensaje && <Alert variant="success">{mensaje}</Alert>}
      <div className="registro-asistencia-info-contenedor">
        <div className="semana-horario-contenedor">
          <Dropdown className="semana-info">
            <Dropdown.Toggle variant="primary">
              {semana ? semana : "Seleccione semana"}
            </Dropdown.Toggle>
            <Dropdown.Menu>
              {Array.from({ length: 16 }, (_, i) => (
                (i === 0 || mostrarSiguienteSemana) && (
                  <Dropdown.Item
                    key={i}
                    onClick={() => {
                      setSemana(`Semana ${i + 1}`);
                      setMostrarSiguienteSemana(false);
                    }}
                  >
                    {`Semana ${i + 1}`}
                  </Dropdown.Item>
                )
              ))}
            </Dropdown.Menu>
          </Dropdown>
          {semana && (
            <Dropdown className="horario-info">
              <Dropdown.Toggle variant="primary">
                {horario ? horario : "Seleccione horario"}
              </Dropdown.Toggle>
              <Dropdown.Menu>
                {horarios.map((horarioOption, index) => (
                  <Dropdown.Item key={index} onClick={() => setHorario(horarioOption)}>
                    {horarioOption}
                  </Dropdown.Item>
                ))}
              </Dropdown.Menu>
            </Dropdown>
          )}
        </div>
        <Form>
          <ul className="lista-estudiantes">
            {listaEstudiantes.map((estudiante, index) => (
              <li key={index} className="estudiante-item">
                <span>{estudiante.nombre_estudiante}</span>
                <Form.Check
                  type="checkbox"
                  className="estudiante-checkbox"
                  onChange={() => handleCheckChange(estudiante.id_estudiante)}
                  checked={!!asistencias.find(asistencia => asistencia.id_estudiante === estudiante.id_estudiante && asistencia.presente)}
                  disabled={!semana || !horario || isSemanaCompleta}
                />
              </li>
            ))}
          </ul>
          <Button variant="outline-success" className="registrar-button" onClick={handleRegistrarClick} disabled={!semana || !horario || isSemanaCompleta}>
            Registrar
          </Button>
        </Form>
      </div>
    </div>
  );
};

export default RegistroAsistencia;
