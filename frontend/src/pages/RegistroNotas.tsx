/*
Feature a la que responde esta pantalla:
    F2: Identificación de estudiantes con bajas calificaciones

    Como docente quiero saber quienes son los estudiantes con tendencia a tener un promedio por 
    debajo del mínimo aceptable en base a su perfil e historial académico para comunicarme con ellos
    y agendar una cita de ser necesaria.

Grupo encargado: Grupo 2
    - Alejandra Colcha (Backend)
    - Darío Charro (Documentación)
    - Martín Mendieta (Frontend)

Documentación asociada:
    Mapa navegacional y wireframe (pantalla Registro notas): https://www.figma.com/design/ihvX1EY7yVl6tCnNEyzsZQ/DCU?node-id=0-1
    Tokens de diseño: https://www.figma.com/design/ihvX1EY7yVl6tCnNEyzsZQ/DCU?node-id=116-2

Entidades backend involucradas: Estudiante, Asignatura, Notas

Sección de la feature abordada en esta pantalla:
    Registro de notas de para actualizar el perfil e historial académico de un estudiante y así poder detectar
    se tendencia a tener un promedio por debajo del mínimo aceptable. Notificar al docente.
*/

import { Nota } from "../types/RegistroNotas.ts"
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
    
    // Variables de estado
        // Tema relacionado a las notas a registrar
    const [tema, setTema] = useState<string>('')

        // Tipo de actividad a registrar: Actividad o Evaluación
    const [tipoActividad, setTipoActividad] = useState<number>(1)
        
        // Lista de notas a registrar de tipo Nota -> {id_estudiante, nombre, nota, tema, tipo_actividad}
    const [listaNotas, setListaNotas] = useState<Nota[]>([])
    
        // Variables para mostrar alertas de estudiante en riesgo, prioridad media y prioridad alta
    const [mostrarAlertaError, setMostrarAlertaError] = useState<boolean>(false)
    const [mostrarAlertaRiesgo, setMostrarAlertaRiesgo] = useState<boolean>(false)
    const [mostrarAlertaPrioridadMedia, setMostrarAlertaPrioridadMedia] = useState<boolean>(false)
    const [mostrarAlertaPrioridadAlta, setMostrarAlertaPrioridadAlta] = useState<boolean>(false)
    const [estudiantesRiesgo, setEstudiantesRiesgo] = useState<number>(0)
    const [estudiantesPrioridadMedia, setEstudiantesPrioridadMedia] = useState<number>(0)
    const [estudiantesPrioridadAlta, setEstudiantesPrioridadAlta] = useState<number>(0)
    
        // Lista de estudiantes obtenida del contexto global
    const { listaEstudiantes } = useContextoGlobal()

    // Funciones
        // Función que se ejecuta cuando se enfoca un input de nota de un estudiante
        // Si el estudiante no tiene una nota registrada, se agrega a la lista de notas
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

        // Función que se ejecuta cuando se cambia la nota de un estudiante
        // Se busca la nota del estudiante y se actualiza su nota 
    const onChangeNotaEstudiante = (idEstudiante: number, nota: number) => {
        const index = listaNotas.findIndex(nota => nota.id_estudiante === idEstudiante)
        if (index !== -1) {
            listaNotas[index].nota = nota
        }
    }

        // Función que se ejecuta cuando se cambia el tema de las notas
        // Se actualiza el tema de todas las notas
    const onChangeTema = (tema: string) => {
        setTema(tema)
        listaNotas.forEach(nota => {
            nota.tema = tema
        })
    }

        // Función que se ejecuta cuando se cambia el tipo de actividad de las notas
        // Se actualiza el tipo de actividad de todas las notas
    const onChangeTipoActividad = (tipoActividad: number) => {
        setTipoActividad(tipoActividad)
        listaNotas.forEach(nota => {
            nota.tipo_actividad = tipoActividad
        })
    }

        // Función que se ejecuta cuando se presiona el botón de registrar notas
        // Se valida que todas las notas estén registradas y que el tema no esté vacío
        // Se registra las notas y se obtiene el conteo de prioridades
        // Si hay estudiantes en riesgo, prioridad media o prioridad alta, se muestra una alerta
    const registrarNotasEstudiantes = async () => {
        if (listaNotas.some(nota => nota.nota === -1) || listaNotas.length !== listaEstudiantes.length || tema === '') {
            setMostrarAlertaError(true)
            return
        }
        const conteoPrioridades = await registrarNotas(1, 6, 1, listaNotas)
        if (conteoPrioridades.en_riesgo > 0) {
            setEstudiantesRiesgo(conteoPrioridades.en_riesgo)
            setMostrarAlertaRiesgo(true)
        }
        if (conteoPrioridades.alerta_media > 0) {
            setEstudiantesPrioridadMedia(conteoPrioridades.alerta_media)
            setMostrarAlertaPrioridadMedia(true)
        }
        if (conteoPrioridades.alerta_alta > 0) {
            setEstudiantesPrioridadAlta(conteoPrioridades.alerta_alta)
            setMostrarAlertaPrioridadAlta(true)
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
                            <span>Tema</span>
                            <input type="text" value={tema} onChange={e => onChangeTema(e.target.value)} />
                        </div>
                        <div className="tipo-nota">
                            <span>Tipo de nota</span>
                            <Dropdown id="tipo-nota">
                                <Dropdown.Toggle variant="light">
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
                <Button onClick={() => registrarNotasEstudiantes()} size="lg" variant="primary">Registrar</Button>
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
                        <Alert variant="secondary" onClose={() => setMostrarAlertaRiesgo(false)} dismissible>
                            {
                                estudiantesRiesgo === 1 ?
                                    <span><b>1</b> nuevo estudiante en riesgo de disminuir su promedio detectado</span>
                                    :
                                    <span><b>{estudiantesRiesgo}</b> nuevos estudiantes en riesgo de disminuir su promedio detectados</span>
                            }
                            <hr />
                            Por favor, revise la lista de estudiantes
                        </Alert>
                    }
                    {
                        mostrarAlertaPrioridadMedia &&
                        <Alert variant="warning" onClose={() => setMostrarAlertaPrioridadMedia(false)} dismissible>
                            {
                                estudiantesPrioridadMedia === 1 ?
                                    <span><b>1</b> nuevo estudiante que ha bajado su promedio en hasta 2 ocasiones detectado</span>
                                    :
                                    <span><b>{estudiantesPrioridadMedia}</b> nuevos estudiantes que han bajado su promedio en hasta 2 ocasiones detectados</span>
                            }
                            <hr />
                            Por favor, revise la lista de estudiantes
                        </Alert>
                    }
                    {
                        mostrarAlertaPrioridadAlta &&
                        <Alert variant="danger" onClose={() => setMostrarAlertaPrioridadAlta(false)} dismissible>
                            {
                                estudiantesPrioridadAlta === 1 ?
                                    <span><b>1</b> nuevo estudiante que ha bajado su promedio en 3 o más ocasiones detectado</span>
                                    :
                                    <span><b>{estudiantesPrioridadMedia}</b> nuevos estudiantes que han bajado su promedio en 3 o más ocasiones detectados</span>
                            }
                            <hr />
                            Por favor, revise la lista de estudiantes
                        </Alert>
                    }
                </div>
            </div>
        </>
    )
    
}

export default RegistroNotas
