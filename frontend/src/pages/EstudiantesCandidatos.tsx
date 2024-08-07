/*
Feature 4: Identifiación de estudiantes candidatos a curso de verano
Como docente
quiero identificar estudiantes que se encuentren entre el promedio histórico de estudiantes con problemas
en la asignatura pre-requisito y el mínimo establecido por la institución.
para decidir si notificar a bienestar estudiantil sobre una asignación a un curso de verano.

Feature asiganara a GRUPO 1:
- Jiménez Alejandro
- Rosillo Bryan
- Segovia Jorge

Link figma: https://www.figma.com/design/ihvX1EY7yVl6tCnNEyzsZQ/DCU?node-id=116-2&t=GrxFJqH8GlzzswaU-1
        - Wireframe asociado: Lista de estudiantes dentro del rango - F4

Modelos relacionados:
- Asignatura
- Periodo
- Estudiante 
- HistorialNotas
*/

import { useEffect, useState } from 'react';
import { obtenerSeguimientoMalla } from '../services/EstudiantesCandidatos';
import { EstudianteCandidato } from '../types/EstudiantesCandidatos';

import '../styles/pages/Estudiantes.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Button, Table } from 'react-bootstrap';

type EstudiantesCandidatosProps = {
        id: string;
};

function EstudiantesCandidatos({ id }: EstudiantesCandidatosProps) {
        // Variables de estado
        /* 
        La primera variable cumple con la identificación de estudiantes que se encuentran entre el rango histórico
        (obtenido en el backend de la aplicación) y el mínimo establecido
        */
        const [datos, setDatos] = useState<EstudianteCandidato[]>([]);                    // Datos recibidos por parte del backend
        const [error, setError] = useState<string | null>(null);
        const [direccionDeOrdenamiento, setDireccionDeOrdenamiento] = useState<'asc' | 'desc'>('asc');
        const [ordenarColumna, setOrdenarColumna] = useState<string | null>(null);
        const [filasSeleccionadas, setFilasSeleccionadas] = useState<Set<number>>(new Set());

        useEffect(() => {
                const obtenerDatos = async () => {
                        try {
                                const resultados = await obtenerSeguimientoMalla();
                                setDatos(resultados);
                        } catch (err) {
                                setError('Error fetching datos');
                        }
                };

                obtenerDatos();
        }, []);

        // Método usado para ordenar la tabla al presionar cualquier header de ésta.
        const manejadorOrdenamiento = (columna: string) => {
                const nuevaDireccion = ordenarColumna === columna && direccionDeOrdenamiento === 'asc' ? 'desc' : 'asc';
                setDireccionDeOrdenamiento(nuevaDireccion);
                setOrdenarColumna(columna);
                const datosOrdenados = [...datos].sort((a, b) => {
                        if (a[columna] < b[columna]) return nuevaDireccion === 'asc' ? -1 : 1;
                        if (a[columna] > b[columna]) return nuevaDireccion === 'asc' ? 1 : -1;
                        return 0;
                });
                setDatos(datosOrdenados);
        };

        // Método usado para seleccionar una fila de la tabla
        const manejadorDeFilaSeleccionada = (id: number) => {
                const nuevaFilaSeleccionada = new Set(filasSeleccionadas);
                if (nuevaFilaSeleccionada.has(id)) {
                        nuevaFilaSeleccionada.delete(id);
                } else {
                        nuevaFilaSeleccionada.add(id);
                }
                setFilasSeleccionadas(nuevaFilaSeleccionada);
        };

        // Método usado para seleccionar una o más filas de la tabla
        const manejadorDeTodasLasFilasSeleccionadas = () => {
                if (filasSeleccionadas.size === datos.length) {
                        setFilasSeleccionadas(new Set());
                } else {
                        setFilasSeleccionadas(new Set(datos.map(item => item.id_estudiante)));
                }
        };

        // Método usado para simular la notificación a bienestar estudiantil sobre los estudiantes seleccionados
        const manejadorDeNotificaciones = () => {
                if (filasSeleccionadas.size > 0) {
                        alert(`Se ha notificado ha bienestar estudiantil sobre ${filasSeleccionadas.size} estudiantes seleccionado(s)`);
                        const nuevosDatos = datos.filter(item => !filasSeleccionadas.has(item.id_estudiante));
                        setDatos(nuevosDatos);
                        setFilasSeleccionadas(new Set());
                } else {
                        alert('Se ha notificado a bienestar estudiantil todos los estudiantes');
                        setDatos([]);
                        setFilasSeleccionadas(new Set());
                }
        };

        // Control de error al renderizar los datos por parte del endpoint de la API
        if (error) return <p>{error}</p>;

        return (
                <div id={id} className='estudiantes-contenedor'>
                        <h1>Estudiantes Candidatos</h1>
                        {/* 
                        En esta parte, se define al botón que cumple con la parte de la decisión de la notificación a bienestar 
                        estudiantil sobre un posible curso de verano al estudiante seleccionado o a todos los estudiantes.
                        */}
                        <Button variant="primary" onClick={manejadorDeNotificaciones} >
                                {filasSeleccionadas.size > 0 ? `Notificar ${filasSeleccionadas.size} seleccionado(s)` : 'Notificar todos'}
                        </Button>

                        {/* 
                        Tabla que muestra los datos enviados por parte del back end, en donde se muestra el nombre del estudiante,
                        su email y su promedio de notas. Además, se incluye un checkbox para seleccionar a los estudiantes que se
                        encuentran dentro del rango histórico y el mínimo establecido por la institución.
                        */}
                        <div className="contenedor-tabla">
                                <Table hover>
                                        <thead>
                                                <tr>
                                                        <th className='celda-tabla'>
                                                                <input
                                                                        type="checkbox"
                                                                        checked={filasSeleccionadas.size === datos.length}
                                                                        onChange={manejadorDeTodasLasFilasSeleccionadas}
                                                                />
                                                        </th>
                                                        <th className='celda-tabla' onClick={() => manejadorOrdenamiento('nombre_estudiante')}>
                                                                Nombre Estudiante {ordenarColumna === 'nombre_estudiante' && (direccionDeOrdenamiento === 'asc' ? '↑' : '↓')}
                                                        </th>
                                                        <th className='celda-tabla' onClick={() => manejadorOrdenamiento('email')}>
                                                                Email {ordenarColumna === 'email' && (direccionDeOrdenamiento === 'asc' ? '↑' : '↓')}
                                                        </th>
                                                        <th className='celda-tabla' onClick={() => manejadorOrdenamiento('promedio_notas')}>
                                                                Promedio Notas {ordenarColumna === 'promedio_notas' && (direccionDeOrdenamiento === 'asc' ? '↑' : '↓')}
                                                        </th>
                                                </tr>
                                        </thead>
                                        <tbody>
                                                {datos.map(item => (
                                                        <tr key={item.id_estudiante} onClick={() => manejadorDeFilaSeleccionada(item.id_estudiante)}>
                                                                <td className='celda-tabla'>
                                                                        <input
                                                                                type="checkbox"
                                                                                checked={filasSeleccionadas.has(item.id_estudiante)}
                                                                                onChange={() => manejadorDeFilaSeleccionada(item.id_estudiante)}
                                                                        />
                                                                </td>
                                                                <td className='celda-tabla'>{item.nombre_estudiante}</td>
                                                                <td className='celda-tabla'>{item.email}</td>
                                                                <td className='celda-tabla'>{item.promedio_notas}</td>
                                                        </tr>
                                                ))}
                                        </tbody>
                                </Table>
                        </div>


                </div>
        );
}

export default EstudiantesCandidatos;
