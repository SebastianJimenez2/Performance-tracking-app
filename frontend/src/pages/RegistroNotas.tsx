import { Estudiante, Nota } from "../types/RegistroNotas.ts"
import NotaEstudiante from "../components/NotaEstudiante.tsx"
import { useState } from "react"
import Button from "react-bootstrap/Button"
import Dropdown from 'react-bootstrap/Dropdown';
import Alert from 'react-bootstrap/Alert';

import '../styles/pages/RegistroNotas.css'
import 'bootstrap/dist/css/bootstrap.min.css';

type RegistroNotasProps = {
    id: string
}

function RegistroNotas({ id }: RegistroNotasProps) {

    const [tema, setTema] = useState<string>('')
    const [tipoActividad, setTipoActividad] = useState<number>(1)
    const [listaNotas, setListaNotas] = useState<Nota[]>([])
    const [mostrarAlertaError, setMostrarAlertaError] = useState<boolean>(false)
    const [mostrarAlertaRiesgo, setMostrarAlertaRiesgo] = useState<boolean>(false)
    const [mostrarAlertaPrioridadMedia, setMostrarAlertaPrioridadMedia] = useState<boolean>(false)
    const [mostrarAlertaPrioridadAlta, setMostrarAlertaPrioridadAlta] = useState<boolean>(false)
    const [estudiantesRiesgo, setEstudiantesRiesgo] = useState<number>(0)
    const [estudiantesPrioridadMedia, setEstudiantesPrioridadMedia] = useState<number>(0)
    const [estudiantesPrioridadAlta, setEstudiantesPrioridadAlta] = useState<number>(0)
    const listaEstudiantes: Estudiante[] = [
        {
            id_estudiante: 1,
            nombre_estudiante: 'Juan',
            email: 'juan@gmail.com',
            numero_incidencias: 0,
            prioridad: 'BAJA',
            promedio: 0
        },
        {
            id_estudiante: 2,
            nombre_estudiante: 'Maria',
            email: 'maria@gmail.com',
            numero_incidencias: 0,
            prioridad: 'BAJA',
            promedio: 0
        },
        {
            id_estudiante: 3,
            nombre_estudiante: 'Pedro',
            email: 'pedro@gmail.com',
            numero_incidencias: 0,
            prioridad: 'BAJA',
            promedio: 0
        },
        {
            id_estudiante: 4,
            nombre_estudiante: "Ana",
            email: "ana@gmail.com",
            numero_incidencias: 1,
            prioridad: "MEDIA",
            promedio: 7.5
        },
        {
            id_estudiante: 5,
            nombre_estudiante: "Luis",
            email: "luis@gmail.com",
            numero_incidencias: 2,
            prioridad: "ALTA",
            promedio: 6.0
        },
        {
            id_estudiante: 6,
            nombre_estudiante: "Carmen",
            email: "carmen@gmail.com",
            numero_incidencias: 0,
            prioridad: "BAJA",
            promedio: 9.0
        },
        {
            id_estudiante: 7,
            nombre_estudiante: "Jose de los monteros",
            email: "jose@gmail.com",
            numero_incidencias: 3,
            prioridad: "ALTA",
            promedio: 5.5
        },
        {
            id_estudiante: 8,
            nombre_estudiante: "Laura",
            email: "laura@gmail.com",
            numero_incidencias: 1,
            prioridad: "MEDIA",
            promedio: 8.0
        },
        {
            id_estudiante: 9,
            nombre_estudiante: "Miguel",
            email: "miguel@gmail.com",
            numero_incidencias: 0,
            prioridad: "BAJA",
            promedio: 7.0
        },
        {
            id_estudiante: 10,
            nombre_estudiante: "Sara",
            email: "sara@gmail.com",
            numero_incidencias: 0,
            prioridad: "BAJA",
            promedio: 9.5
        }
    ]

    const onFocusNotaEstudiante = (idEstudiante: number, nombre: string) => {
        if (!listaNotas.some(nota => nota.id_estudiante === idEstudiante)) {
            setListaNotas([...listaNotas,
            {
                id_estudiante: idEstudiante,
                nombre: nombre,
                nota: -1,
                tema: tema,
                tipo_actividad: tipoActividad
            }])
        }
    }

    const onChangeNotaEstudiante = (idEstudiante: number, nota: number) => {
        const index = listaNotas.findIndex(nota => nota.id_estudiante === idEstudiante)
        if (index !== -1) {
            listaNotas[index].nota = nota
        }
    }

    const onChangeTema = (tema: string) => {
        setTema(tema)
        listaNotas.forEach(nota => {
            nota.tema = tema
        })
    }

    const onChangeTipoActividad = (tipoActividad: number) => {
        setTipoActividad(tipoActividad)
        listaNotas.forEach(nota => {
            nota.tipo_actividad = tipoActividad
        })
    }

    const registrarNotas = () => {
        if (listaNotas.some(nota => nota.nota === -1) || listaNotas.length !== listaEstudiantes.length) {
            setMostrarAlertaError(true)
            return
        }
    }

    return (
        <>
            <div id={id} className='registro-notas-contenedor'>
                <h2>Registro de Notas</h2>
                <div className="regitro-notas-contenido">
                    <div className='lista-notas'>
                        {listaEstudiantes.map(estudiante => (
                            <NotaEstudiante
                                key={estudiante.id_estudiante}
                                idEstudiante={estudiante.id_estudiante}
                                nombre={estudiante.nombre_estudiante}
                                onFocusNotaEstudiante={onFocusNotaEstudiante}
                                onChangeNotaEstudiante={onChangeNotaEstudiante}
                            />
                        ))}
                    </div>
                    <div className="parametros-generales">
                        <div className="tema-notas">
                            <label htmlFor="tema">Tema</label>
                            <input type="text" name="tema" id="tema" value={tema} onChange={e => onChangeTema(e.target.value)} />
                        </div>
                        <div className="tipo-nota">
                            <label htmlFor="tipo-nota">Tipo de nota</label>
                            <Dropdown id="tipo-nota">
                                <Dropdown.Toggle variant="primary">
                                    {tipoActividad === 1 ? 'Actividad' : 'Evaluación'}
                                </Dropdown.Toggle>
                                <Dropdown.Menu>
                                    <Dropdown.Item onClick={() => { onChangeTipoActividad(1) }}>Actividad</Dropdown.Item>
                                    <Dropdown.Item onClick={() => { onChangeTipoActividad(2) }}>Evaluación</Dropdown.Item>
                                </Dropdown.Menu>
                            </Dropdown>
                        </div>
                    </div>
                </div>
                <Button onClick={() => registrarNotas()} variant="success">Registrar</Button>
                <div className="contenedor-alertas">
                    {
                        mostrarAlertaError &&
                        <Alert variant="danger" onClose={() => setMostrarAlertaError(false)} dismissible>
                            <Alert.Heading>Error al registrar las notas</Alert.Heading>
                            <p>
                                Por favor, registre las notas de todos los estudiantes
                            </p>
                        </Alert>
                    }
                    {
                        mostrarAlertaRiesgo &&
                        <Alert variant="success" onClose={() => setMostrarAlertaRiesgo(false)} dismissible>
                            Existen {estudiantesRiesgo} estudiantes en riesgo de diminuir su promedio
                        </Alert>
                    }
                    {
                        mostrarAlertaPrioridadMedia &&
                        <Alert variant="success" onClose={() => setMostrarAlertaPrioridadMedia(false)} dismissible>
                            Existen {estudiantesPrioridadMedia} estudiantes que han bajado su promedio en hasta 2 ocasiones
                        </Alert>
                    }
                    {
                        mostrarAlertaPrioridadAlta &&
                        <Alert variant="success" onClose={() => setMostrarAlertaPrioridadAlta(false)} dismissible>
                            Existen {estudiantesPrioridadAlta} estudiantes que han bajado su promedio en 3 o más ocasiones
                        </Alert>
                    }
                </div>
            </div>
        </>
    )
}

export default RegistroNotas
