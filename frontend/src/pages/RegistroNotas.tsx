import { Estudiante, Nota } from "../types/RegistroNotas.ts"
import NotaEstudiante from "../components/NotaEstudiante.tsx"
import { useState } from "react"
import Button from "react-bootstrap/Button"

import '../styles/pages/RegistroNotas.css'

type RegistroNotasProps = {
    id: string
}

function RegistroNotas({ id }: RegistroNotasProps) {

    const [tema, setTema] = useState<string>('')
    const [tipoActividad, setTipoActividad] = useState<number>(0)
    const listaNotas: Nota[] = []
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
            nombre_estudiante: "Jose",
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
            listaNotas.push({
                id_estudiante: idEstudiante,
                nombre: nombre,
                nota: -1,
                tema: tema,
                tipo_actividad: tipoActividad
            })
        }
    }

    const onChangeNotaEstudiante = (idEstudiante: number, nota: number) => {
        const index = listaNotas.findIndex(nota => nota.id_estudiante === idEstudiante)
        if (index !== -1) {
            listaNotas[index].nota = nota
        }
    }

    return (
        <>
            <div id={id} className='registro-notas-container'>
                <h2>Registro de Notas</h2>
                <div className='registro-notas-lista'>
                    {listaEstudiantes.map(estudiante => (
                        <NotaEstudiante
                            key={estudiante.id_estudiante}
                            idEstudiante={estudiante.id_estudiante}
                            nombre={estudiante.nombre_estudiante}
                            onFocus={onFocusNotaEstudiante}
                            onChange={onChangeNotaEstudiante}
                        />
                    ))}
                </div>
                <Button onClick={() => console.log(listaNotas)} variant="success">Success</Button>
            </div>
        </>
    )
}

export default RegistroNotas
