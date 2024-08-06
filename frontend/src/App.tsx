import React from 'react';
import Asignatura from './components/Asignatura';
import Cursos from './pages/Cursos';
import Capacitaciones from './pages/Capacitaciones';
import Login from './pages/Login';
import RegistroNotas from './pages/RegistroNotas';
import Estudiantes from './pages/Estudiantes';
import { useContextoGlobal } from './ContextoGlobal';
import TablaProfesores from './components/TablaProfesores';
import PerfilProfesor from './pages/Profesor';
import { Profesor as TipoProfesor } from './types/Capacitaciones';

function App() {
  const { paginaActual, modoUsuario, profesor } = useContextoGlobal();

  const mostrarPagina = () => {
 main
    switch (paginaActual) {
      case 'Cursos':
        return <Cursos />
      case 'Capacitaciones':
        return <Capacitaciones />
      case 'Login':
        return <Login />
      default:
        return <Asignatura cerrarSemestre={() => console.log('Cerrando semestre')}>
                    <Estudiantes id="Estudiantes" />
                    <Componente3 id="tab número 3" />
                    <RegistroNotas id="Registro notas" />
                    <Componente3 id="tab número 4" />
               </Asignatura>

    if (modoUsuario === 'Admin') {
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
          return <Cursos />;
        case 'Capacitaciones':
          return <Capacitaciones />;
        case 'Login':
          return <Login />;
        default:
          return (
            <Asignatura cerrarSemestre={() => console.log('Cerrando semestre')}>
              <Componente2 id="tab número 2" />
              <Componente3 id="tab número 3" />
              <RegistroNotas id="Registro notas" />
              <Componente3 id="tab número 4" />
            </Asignatura>
          );
      }
 main
    }
  };

  return (
    <>
      {mostrarPagina()}
    </>
  );
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

 main

function Componente2({ id }: { id: string }) {
  return (
    <div id={id}>
      <h1>Componente 2</h1>
    </div>
  );
}

 main
function Componente3({ id }: { id: string }) {
  return (
    <div id={id}>
      <h1>Componente 3</h1>
    </div>
  );
}

export default App;
