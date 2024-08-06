import { Nota, RespuestaRegistroNotas } from "../types/RegistroNotas.ts"
import NotaEstudiante from "../components/NotaEstudiante.tsx"
import { useState } from "react"
import Button from "react-bootstrap/Button"
import Dropdown from 'react-bootstrap/Dropdown';
import Alert from 'react-bootstrap/Alert';
import { useContextoGlobal } from "../ContextoGlobal.tsx";
import { registrarNotas } from "../services/RegistroNotas.ts"

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
    const { listaEstudiantes } = useContextoGlobal()

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

    const registrarNotasEstudiantes = async() => {
        if (listaNotas.some(nota => nota.nota === -1) || listaNotas.length !== listaEstudiantes.length || tema === '') {
            setMostrarAlertaError(true)
            return
        }
        console.log((await registrarNotas(1, 1, 1, listaNotas)).en_riesgo)
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
                <Button onClick={() => registrarNotasEstudiantes()} variant="success">Registrar</Button>
                <div className="contenedor-alertas">
                    {
                        mostrarAlertaError &&
                        <Alert variant="danger" onClose={() => setMostrarAlertaError(false)} dismissible>
                            <Alert.Heading>Error al registrar las notas</Alert.Heading>
                            <p>
                                Por favor, complete todos los campos para poder registrar las notas
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
