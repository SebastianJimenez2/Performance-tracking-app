import Table from 'react-bootstrap/Table';
import { useEffect, useState } from 'react';
import { obtenerEstudiantes } from '../services/Estudiantes';
import Modal from 'react-bootstrap/Modal';
import { Estudiante } from '../types/RegistroNotas';
import Button from 'react-bootstrap/Button';
import Badge from 'react-bootstrap/Badge';
import Alert from 'react-bootstrap/Alert';
import Dropdown from 'react-bootstrap/Dropdown';
import { useContextoGlobal } from '../ContextoGlobal';

import 'bootstrap/dist/css/bootstrap.min.css';
import '../styles/pages/Estudiantes.css'

type EstudiantesProps = {
    id: string
}

function Estudiantes({ id }: EstudiantesProps) {

    const [estudiantes, setEstudiantes] = useState<Estudiante[]>([])
    const [estudiantesVisibles, setEstudiantesVisibles] = useState<Estudiante[]>([])
    const [estudianteSeleccionado, setEstudianteSeleccionado] = useState<Estudiante | null>(null)
    const [estudianteCitado, setEstudianteCitado] = useState<boolean>(false)
    const [filtro, setFiltro] = useState<string>('Todos')
    const {setListaEstudiantes} = useContextoGlobal()

    useEffect(() => {
        console.log('Obteniendo estudiantes')
        const fetchEstudiantes = async () => {
            try {
                const estudiantesFetch = await obtenerEstudiantes(1, 5, 1)
                setEstudiantes(estudiantesFetch)
                setEstudiantesVisibles(estudiantesFetch)
                setListaEstudiantes(estudiantesFetch)
            } catch (error) {
                console.error('Error obteniendo estudiantes:', error)
            }
        }
        fetchEstudiantes()
    }, [setListaEstudiantes])

    const mostrarModalEstudiante = (estudiante: Estudiante) => {
        setEstudianteSeleccionado(estudiante)

    }

    const cerrarModalEstudiante = () => {
        setEstudianteSeleccionado(null)
    }

    const filtrarEstudiantes = (prioridad: string) => {
        if (prioridad === 'TODOS') {
            setEstudiantesVisibles(estudiantes)
        } else {
            const estudiantesFiltrados = estudiantes.filter(estudiante => estudiante.prioridad === prioridad)
            setEstudiantesVisibles(estudiantesFiltrados)
        }
        setFiltro(prioridad)
    }

    return (
        <div id={id} className='estudiantes-contenedor'>
            <h1>Estudiantes</h1>
            <Dropdown>
                <Dropdown.Toggle
                    variant={
                        filtro === 'TODOS' ? 'primary' :
                            filtro === 'RIESGO' ? 'secondary' :
                                filtro === 'MEDIA' ? 'warning' :
                                    filtro === 'ALTA' ? 'danger' : 'primary'
                    }
                    id="dropdown-basic"
                >
                    {filtro}
                </Dropdown.Toggle>

                <Dropdown.Menu>
                    <Dropdown.Item onClick={() => filtrarEstudiantes('TODOS')}>Todos</Dropdown.Item>
                    <Dropdown.Item onClick={() => filtrarEstudiantes('RIESGO')}>En riesgo</Dropdown.Item>
                    <Dropdown.Item onClick={() => filtrarEstudiantes('MEDIA')}>Prioridad media</Dropdown.Item>
                    <Dropdown.Item onClick={() => filtrarEstudiantes('ALTA')}>Prioridad alta</Dropdown.Item>
                </Dropdown.Menu>
            </Dropdown>
            <div className="contenedor-tabla">
                <Table hover>
                    <thead>
                        <tr>
                            <th className='celda-tabla'>Nombre</th>
                            <th className='celda-tabla'>Incidencias</th>
                            <th className='celda-tabla'>Email</th>
                            <th className='celda-tabla'>Promedio</th>
                        </tr>
                    </thead>
                    <tbody>
                        {estudiantesVisibles.map((estudiante) => (
                            <tr key={estudiante.id_estudiante} onClick={() => mostrarModalEstudiante(estudiante)}>
                                <td className={`celda-tabla ${estudiante.prioridad.toLowerCase()}`}>{estudiante.nombre_estudiante}</td>
                                <td className={`celda-tabla ${estudiante.prioridad.toLowerCase()}`}>{estudiante.numero_incidencias}</td>
                                <td className={`celda-tabla ${estudiante.prioridad.toLowerCase()}`}>{estudiante.email}</td>
                                <td className={`celda-tabla ${estudiante.prioridad.toLowerCase()}`}>{estudiante.promedio}</td>
                            </tr>
                        ))}
                    </tbody>
                </Table>
            </div>
            <Modal
                show={estudianteSeleccionado !== null}
                onHide={cerrarModalEstudiante}
                backdrop="static"
                keyboard={false}
                centered
            >
                <Modal.Header closeButton>
                    <Modal.Title>Estudiante: {estudianteSeleccionado?.nombre_estudiante}</Modal.Title>
                </Modal.Header>
                <Modal.Body>
                    <p><b>Incidencias</b> {estudianteSeleccionado?.numero_incidencias}</p>
                    <p><b>Email</b> {estudianteSeleccionado?.email}</p>
                    <p><b>Promedio</b> {estudianteSeleccionado?.promedio}</p>
                    <p><b>Prioridad de atención </b>
                        {(estudianteSeleccionado?.prioridad === 'ALTA') && <Badge bg="danger">Alta</Badge>}
                        {(estudianteSeleccionado?.prioridad === 'MEDIA') && <Badge bg="warning">Media</Badge>}
                        {(estudianteSeleccionado?.prioridad === 'RIESGO') && <Badge bg="secondary">En riesgo</Badge>}
                        {(estudianteSeleccionado?.prioridad === 'BAJA') && <Badge bg="success">Baja</Badge>}
                    </p>
                </Modal.Body>
                <Modal.Footer>
                    <Button variant="primary" onClick={() => { setEstudianteSeleccionado(null); setEstudianteCitado(true) }}>Citar alumno</Button>
                </Modal.Footer>
            </Modal>
            <div className="contenedor-notificacion">
                <Alert variant='primary' show={estudianteCitado} onClose={() => setEstudianteCitado(false)} dismissible>
                    Estudiante citado con éxito
                </Alert>
            </div>
        </div>
    )
}

export default Estudiantes
