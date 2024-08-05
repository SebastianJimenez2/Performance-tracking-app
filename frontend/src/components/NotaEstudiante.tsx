import { useState } from 'react'
import '../styles/components/NotaEstudiante.css'

type NotaEstudianteProps = {
    idEstudiante: number,
    nombre: string,
    onFocus: (idEstudiante: number, nombre: string) => void,
    onChange: (idEstudiante: number, nota: number) => void,
}

function NotaEstudiante({ idEstudiante, nombre, onFocus, onChange }: NotaEstudianteProps) {

    const [nota, setNota] = useState<number>(-1)

    return (
        <div className='nota-estudiante-container'>
            <span>{nombre}</span>
            <input
                type="text"
                value={nota === -1 || isNaN(nota) ? '' : nota}
                onFocus={() => onFocus(idEstudiante, nombre)}
                onChange={(e) => { 
                    setNota(parseFloat(e.target.value || '-1'))
                    onChange(idEstudiante, parseFloat(e.target.value || '-1'))
                }}
            />
        </div>
    )

}

export default NotaEstudiante
