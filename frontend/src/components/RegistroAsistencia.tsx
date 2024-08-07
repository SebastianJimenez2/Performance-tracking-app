import React, { useState, useEffect } from 'react';
import { Dropdown, Button, Form, Alert } from 'react-bootstrap';
import '../styles/components/RegistroAsistencia.css';
import { Estudiante } from '../types/Asistencia';

type RegistroAsistenciaProps = {
  id: string;
};

interface Asistencia {
  id_estudiante: number;
  presente: boolean;
}

const RegistroAsistencia: React.FC<RegistroAsistenciaProps> = ({ id }) => {
  const [semana, setSemana] = useState<string | null>(null);
  const [horario, setHorario] = useState<string | null>(null);
  const [asistencias, setAsistencias] = useState<Asistencia[]>([]);
  const [mensaje, setMensaje] = useState<string | null>(null);
  const [mostrarSiguienteSemana, setMostrarSiguienteSemana] = useState<boolean>(false);
  const [registrosPorSemana, setRegistrosPorSemana] = useState<{ [key: string]: number }>({});

  const estudiantes: Estudiante[] = [
    { id_estudiante: 1, nombre_estudiante: "Joe Doe" },
    { id_estudiante: 2, nombre_estudiante: "Jill Doe" },
    { id_estudiante: 3, nombre_estudiante: "June Doe" },
    { id_estudiante: 4, nombre_estudiante: "Jiss Doe" }
  ];

  const horarios = [
    "11:00-13:00",
    "15:00-17:00"
  ];

  useEffect(() => {
    if (mensaje) {
      const timer = setTimeout(() => {
        setMensaje(null);
      }, 2000);
      return () => clearTimeout(timer);
    }
  }, [mensaje]);

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

  const handleRegistrarClick = () => {
    if (semana && horario) {
      const registro = {
        semana,
        horario,
        asistencias,
      };
      console.log('Asistencia registrada', registro);
      setMensaje('Registro exitoso de asistencia');

      // Limpiar asistencias y reiniciar selección de semana y horario
      setAsistencias([]);
      setSemana(null);
      setHorario(null);

      // Actualizar conteo de registros por semana
      setRegistrosPorSemana((prevRegistros) => {
        const count = prevRegistros[semana] || 0;
        return { ...prevRegistros, [semana]: count + 1 };
      });

      // Mostrar siguiente semana si la semana actual tenía ambos horarios registrados
      setMostrarSiguienteSemana(true);
    }
  };

  const isSemanaCompleta = semana ? (registrosPorSemana[semana] || 0) >= 2 : false;

  return (
    <div id={id} className="asistencia-contenedor">
      <h2>Registro de asistencia</h2>
      <br />
      {mensaje && <Alert variant="success">{mensaje}</Alert>}
      <div className='registrar-asistencia-contenedor'>
        <div className='izquierdo-ra-contenedor'></div>
        <div className="registro-asistencia-info-contenedor">
          <div className='semana-horario-contenedor'>
            <div className='izquierdo-contenedor'></div>
            <div className="semana-contenedor">
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
            </div>
            {semana && (
              <div className="horario-contenedor">
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
              </div>
            )}
            <div className='derecho-contenedor'></div>
          </div>
          <Form>
            <ul className="lista-estudiantes">
              {estudiantes.map((estudiante, index) => (
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
        <div className='derecho-ra-contenedor'></div>
      </div>
    </div>
  );
};

export default RegistroAsistencia;

