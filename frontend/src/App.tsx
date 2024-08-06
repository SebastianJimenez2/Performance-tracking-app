import Asignatura from './components/Asignatura';
import Cursos from './pages/Cursos';
import Capacitaciones from './pages/Capacitaciones';
import Login from './pages/Login';
import RegistroNotas from './pages/RegistroNotas';
import Estudiantes from './pages/Estudiantes';
import { useContextoGlobal } from './ContextoGlobal';

function App() {
  const { paginaActual } = useContextoGlobal()

  const mostrarPagina = () => {
    switch (paginaActual) {
      case 'Cursos':
        return <Cursos />
      case 'Capacitaciones':
        return <Capacitaciones />
      case 'Login':
        return <Login />
      case 'Asignatura':
        return <Asignatura cerrarSemestre={() => console.log('Cerrando semestre')}>
                    <Estudiantes id="Estudiantes" />
                    <Componente3 id="tab número 3" />
                    <RegistroNotas id="Registro notas" />
                    <Componente3 id="tab número 4" />
               </Asignatura>
    }
  }

  return (
    <>
      {mostrarPagina()}
    </>
  )
}

function Componente3({ id }: { id: string }) {
  return (
    <div id={id}>
      <h1>Componente 3</h1>
    </div>
  )
}

export default App
