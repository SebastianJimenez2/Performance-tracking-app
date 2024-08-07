import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import NavDropdown from 'react-bootstrap/NavDropdown';
import Perfil from '../assets/perfil.svg'
import { useContextoGlobal } from '../ContextoGlobal';

import 'bootstrap/dist/css/bootstrap.min.css';
import '../styles/components/BarraNavegacion.css';


function BarraNavegacion() {
    const { setPaginaActual } = useContextoGlobal()

    const cambiarPagina = (pagina: string) => {
        setPaginaActual(pagina)
    }

    return (
        <nav>
            <Navbar className="nav-bar" data-bs-theme="dark">
                <Navbar.Brand>SYNCADEMIC</Navbar.Brand>
                <Navbar.Toggle aria-controls="basic-navbar-nav" />
                <Navbar.Collapse className="justify-content-end">
                    <Nav>
                        <img src={Perfil} width={15}></img>
                        <NavDropdown title="Perfil docente" data-bs-theme="light">
                            <NavDropdown.Header>Perfil del docente</NavDropdown.Header>
                            <NavDropdown.Item onClick={() => cambiarPagina('Cursos')}>Cursos</NavDropdown.Item>
                            <NavDropdown.Item onClick={() => cambiarPagina('Capacitaciones')}>Capacitaciones</NavDropdown.Item>
                            <NavDropdown.Divider />
                            <NavDropdown.Item onClick={() => cambiarPagina('Login')}>Cerrar sesión</NavDropdown.Item>
                        </NavDropdown>
                    </Nav>
                </Navbar.Collapse>
            </Navbar>
        </nav>
    )
}

export default BarraNavegacion
