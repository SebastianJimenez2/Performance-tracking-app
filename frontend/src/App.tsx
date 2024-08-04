import Asignatura from './components/Asignatura';
import Cursos from './pages/Cursos';
import Capacitaciones from './pages/Capacitaciones';
import Login from './pages/Login';
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
      default:
        return <Asignatura>
                    <Componente1 id="tab numero 1" />
                    <Componente2 id="tab número 2" />
                    <Componente3 id="tab número 3" />
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

function Componente1({ id }: { id: string }) {
  return (
    <div id={id}>
      <h1>Componente 1</h1>
    </div>
  )
}

function Componente2({ id }: { id: string }) {
  return (
    <div id={id}>
      <h1>Componente 2</h1>
    </div>
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
