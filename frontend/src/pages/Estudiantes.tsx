import Table from 'react-bootstrap/Table';
import { useEffect, useState } from 'react';
import { obtenerEstudiantes } from '../services/Estudiantes';

import 'bootstrap/dist/css/bootstrap.min.css';
import '../styles/pages/Estudiantes.css'
import { Estudiante } from '../types/RegistroNotas';

type EstudiantesProps = {
    id: string
}

function Estudiantes({ id }: EstudiantesProps) {
    
    const[estudiantes, setEstudiantes] = useState<Estudiante[]>([])

    useEffect(() => {
        const fetchEstudiantes = async () => {
            try {
                const estudiantesFetch = await obtenerEstudiantes(1, 5, 1)
                setEstudiantes(estudiantesFetch)
            } catch (error) {
                console.error('Error obteniendo estudiantes:', error)
            }
        }
        fetchEstudiantes()
    })
    
    return (
        <div id={id} className='estudiantes-contenedor'>
            <h1>Estudiantes</h1>
            <Table hover>
                <thead>
                    <tr>
                        <th>Nombre</th>
                        <th>Incidencias</th>
                        <th>Email</th>
                        <th>Promedio</th>
                    </tr>
                </thead>
                <tbody>
                    {estudiantes.map((estudiante) => (
                        <tr key={estudiante.nombre_estudiante}>
                            <td>{estudiante.numero_incidencias}</td>
                            <td>{estudiante.email}</td>
                            <td>{estudiante.promedio}</td>
                        </tr>
                    ))}
                </tbody>
            </Table>
        </div>
    )
}

export default Estudiantes
