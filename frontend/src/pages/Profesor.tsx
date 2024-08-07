import { useState } from 'react';
import PerfilProfesor from '../components/PerfilProfesor';
import { useContextoGlobal } from '../ContextoGlobal';
import TablaCapacitaciones from "../components/TablaCapacitaciones";
import { Button } from 'react-bootstrap';
import type { Profesor as TipoProfesor } from '../types/Capacitaciones'; 
import BarraNavegacion from "../components/BarraNavegacion";


const datosIniciales: TipoProfesor = {
  id: 1,
  nombre: "David Torres",
  email: "David@epn.edu.ec",
  carrera: "Sistemas",
  puntaje: 45,
  encuestaCompletada: true,
  urlImagen: "https://via.placeholder.com/150"
};

function Profesor({ profesor }: { profesor: TipoProfesor }) {
  const { setPaginaActual } = useContextoGlobal();

  const volverAListaProfesores = () => {
    setPaginaActual('Profesores');
  };

  const [profesorData, setProfesor] = useState<TipoProfesor | null>(datosIniciales);

  return (
    <div>
      <BarraNavegacion />
      {profesorData && <PerfilProfesor profesor={profesorData} />}
      <TablaCapacitaciones />
      <div style={{ display: 'flex', justifyContent: 'center', marginTop: '20px' }}>
        <Button variant="primary" onClick={volverAListaProfesores}>Regresar a la Lista de Profesores</Button>
      </div>
    </div>
  );
}

export default Profesor;


