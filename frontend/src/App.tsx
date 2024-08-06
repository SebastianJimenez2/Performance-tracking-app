import { useState } from 'react';

import Asignatura from './components/Asignatura';
import Cursos from './pages/Cursos';
import Capacitaciones from './pages/Capacitaciones';
import Login from './pages/Login';
import RegistroNotas from './pages/RegistroNotas';
import Estudiantes from './pages/Estudiantes';
import EstudiantesCandidatos from './pages/EstudiantesCandidatos';
import { useContextoGlobal } from './ContextoGlobal';
import PerfilProfesor from './pages/Profesor';
import { Profesor as TipoProfesor } from './types/Capacitaciones';
import TablaProfesores from './components/TablaProfesores';



function App() {
  const { paginaActual, rol, profesor, setRol } = useContextoGlobal()
  const [isSemesterClosed, setIsSemesterClosed] = useState<boolean>(false);
  const handleSemesterToggle = (isClosed: boolean) => {
    console.log('Semestre cerrado:', isClosed);
    setIsSemesterClosed(isClosed);
  };

  const renderAsignaturaChildren = (): React.ReactNode[] => {
    if (isSemesterClosed) {
      return [
        <Estudiantes key={'Estudiantes'} id="Estudiantes" />,
        <Componente3 key={'tab número 3'} id="tab número 3" />,
        <EstudiantesCandidatos key={'Estudiantes candidatos'} id="Estudiantes candidatos" />,
        <Componente3 key={'tab número 4'} id="tab número 4" />
      ];
    } else {
      return [
        <Estudiantes key={'Estudiantes'} id="Estudiantes" />,
        <Componente3 key={'tab número 3'} id="tab número 3" />,
        <RegistroNotas key={'Registro notas'} id="Registro notas" />,
        <Componente3 key={'tab número 4'} id="tab número 4" />
      ];
    }
  };

  const mostrarPagina = () => {
    //setRol('Admin')
    if (rol === 'Admin') {
      switch (paginaActual) {
        case 'Profesor':
          return profesor ? <PerfilProfesor profesor={profesor} /> : <div>No se ha seleccionado ningún profesor</div>;
        default:
          return (
            <>
              <Asignatura cerrarSemestre={() => console.log('Cerrando semestre')}>
                <Componente_profesor id="Profesores" />
                <Componente_asignatura id="Asignaturas" />
              </Asignatura>
            </>
          );
      }
    } else {

    switch (paginaActual) {
      case 'Cursos':
        return <Cursos />
      case 'Capacitaciones':
        return <Capacitaciones />
      case 'Login':
        return <Login />
      default:
        return (
          <Asignatura cerrarSemestre={handleSemesterToggle}>
            {renderAsignaturaChildren()}
          </Asignatura>
        );
    }
  }
  }

  return (
    <>
      {mostrarPagina()}
    </>
  )
}

function Componente_profesor({ id }: { id: string }) {
  const { setPaginaActual, setProfesor } = useContextoGlobal();

  const handleRowClick = (profesor: TipoProfesor) => {
    setProfesor(profesor);
    setPaginaActual('Profesor');
  };

  return <TablaProfesores alHacerClicEnFila={handleRowClick} />;
}

function Componente_asignatura({ id }: { id: string }) {
  return (
    <div id={id}>
      <h1>Componente Asignatura</h1>
    </div>
  );
}

function Componente3({ id }: { id: string }) {
  return (
    <div id={id}>
      <h1>Componente 3</h1>
    </div>
  )
}

export default App
