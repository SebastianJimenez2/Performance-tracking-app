import React, { useRef, useState } from 'react';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import NavDropdown from 'react-bootstrap/NavDropdown';
import Perfil from '../assets/perfil.svg';
import { useContextoGlobal } from '../ContextoGlobal';
import { BiBell } from 'react-icons/bi';
import CargaHorariaAtrasada from './CargaHorariaAtrasada';

import 'bootstrap/dist/css/bootstrap.min.css';
import '../styles/components/BarraNavegacion.css';

function BarraNavegacion() {
    const { paginaActual, setPaginaActual, setRol, setAsignatura, setCurso, setUsuario, rol } = useContextoGlobal();
    const notificacionesRef = useRef<any>(null);
    const [mostrarNotificaciones, setMostrarNotificaciones] = useState(false);

    const cambiarPagina = (pagina: string) => {
        setPaginaActual(pagina);
    };

    const cerrarSesion = () => {
        setRol('');
        setUsuario('');
        setAsignatura(0);
        setCurso(0);
        setPaginaActual('Login');
    };

    const handleBellClick = () => {
        setMostrarNotificaciones(true);
        if (notificacionesRef.current) {
            notificacionesRef.current.recargarNotificaciones();
        }
    };

    return (
        <nav>
            <Navbar className="nav-bar" data-bs-theme="dark">
                <Navbar.Brand>SYNCADEMIC</Navbar.Brand>
                <Navbar.Toggle aria-controls="basic-navbar-nav" />
                <Navbar.Collapse className="justify-content-end">
                    <Nav>
                        <img src={Perfil} width={15} alt="Perfil" />
                        <NavDropdown title={`Perfil ${rol}`} data-bs-theme="light">
                            <NavDropdown.Header>Perfil del {rol}</NavDropdown.Header>
                            {
                                rol === 'docente' &&
                                <>
                                    <NavDropdown.Item onClick={() => cambiarPagina('Cursos')}>Cursos</NavDropdown.Item>
                                    <NavDropdown.Item onClick={() => cambiarPagina('Capacitaciones')}>Capacitaciones</NavDropdown.Item>
                                </>
                            }
                            <NavDropdown.Divider />
                            <NavDropdown.Item onClick={() => cerrarSesion()}>Cerrar sesión</NavDropdown.Item>
                        </NavDropdown>
                        {paginaActual === 'Estudiantes' && (
                            <Nav.Item>
                                <Nav.Link onClick={handleBellClick}>
                                    <BiBell className='notification-icon' />
                                </Nav.Link>
                            </Nav.Item>
                        )}
                    </Nav>
                </Navbar.Collapse>
                {paginaActual === 'Estudiantes' && mostrarNotificaciones && <CargaHorariaAtrasada ref={notificacionesRef} />}
            </Navbar>            
        </nav>
    );
}

export default BarraNavegacion;