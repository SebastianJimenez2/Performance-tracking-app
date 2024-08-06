import { useState } from 'react'
import '../styles/components/NotaEstudiante.css'

type NotaEstudianteProps = {
    idEstudiante: number,
    nombre: string,
    onFocusNotaEstudiante: (idEstudiante: number, nombre: string) => void,
    onChangeNotaEstudiante: (idEstudiante: number, nota: number) => void,
}

function NotaEstudiante({ idEstudiante, nombre, onFocusNotaEstudiante, onChangeNotaEstudiante }: NotaEstudianteProps) {

    const [nota, setNota] = useState<string>('')

    return (
        <div className='nota-estudiante-container'>
            <span>{nombre}</span>
            <input
                type="text"
                value={nota}
                onFocus={() => onFocusNotaEstudiante(idEstudiante, nombre)}
                onChange={(e) => { 
                    setNota(e.target.value)
                }}
                onBlur={(e) => {
                    const valorNota = parseFloat(e.target.value)
                    if(isNaN(valorNota) || valorNota < 0 || valorNota > 10) {
                        setNota('')
                        onChangeNotaEstudiante(idEstudiante, -1)
                    } else {
                        setNota(valorNota.toString())
                        onChangeNotaEstudiante(idEstudiante, valorNota)
                    }
                }}
            />
        </div>
    )

}

export default NotaEstudiante
