import { useEffect, useState } from 'react';
import { obtenerSeguimientoMalla } from '../services/EstudiantesCandidatos';
import { SeguimientoMalla } from '../types/SeguimientoMalla';

import '../styles/pages/Estudiantes.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Button, Table } from 'react-bootstrap';

type EstudiantesCandidatosProps = {
        id: string;
};

function EstudiantesCandidatos({ id }: EstudiantesCandidatosProps) {
        const [data, setData] = useState<SeguimientoMalla[]>([]);
        const [error, setError] = useState<string | null>(null);
        const [sortDirection, setSortDirection] = useState<'asc' | 'desc'>('asc');
        const [sortColumn, setSortColumn] = useState<string | null>(null);
        const [selectedRows, setSelectedRows] = useState<Set<number>>(new Set());

        useEffect(() => {
                const getData = async () => {
                        try {
                                const result = await obtenerSeguimientoMalla();
                                setData(result);
                        } catch (err) {
                                setError('Error fetching data');
                        } finally {
                                setLoading(false);
                        }
                };

                getData();
        }, []);

        const handleSort = (column: string) => {
                const newDirection = sortColumn === column && sortDirection === 'asc' ? 'desc' : 'asc';
                setSortDirection(newDirection);
                setSortColumn(column);
                const sortedData = [...data].sort((a, b) => {
                        if (a[column] < b[column]) return newDirection === 'asc' ? -1 : 1;
                        if (a[column] > b[column]) return newDirection === 'asc' ? 1 : -1;
                        return 0;
                });
                setData(sortedData);
        };

        const handleRowSelect = (id: number) => {
                const newSelectedRows = new Set(selectedRows);
                if (newSelectedRows.has(id)) {
                        newSelectedRows.delete(id);
                } else {
                        newSelectedRows.add(id);
                }
                setSelectedRows(newSelectedRows);
        };

        const handleSelectAll = () => {
                if (selectedRows.size === data.length) {
                        setSelectedRows(new Set());
                } else {
                        setSelectedRows(new Set(data.map(item => item.id_estudiante)));
                }
        };

        const handleNotify = () => {
                if (selectedRows.size > 0) {
                        alert(`Se ha notificado ha bienestar estudiantil sobre ${selectedRows.size} estudiantes seleccionado(s)`);
                } else {
                        alert('Se ha notificado a bienestar estudiantil todos los estudiantes');
                }
        };

        if (error) return <p>{error}</p>;

        return (
                <div id={id} className='estudiantes-contenedor'>
                        <h1>Estudiantes Candidatos</h1>

                        <Button variant="primary" onClick={handleNotify} >
                                {selectedRows.size > 0 ? `Notificar ${selectedRows.size} seleccionado(s)` : 'Notificar todos'}
                        </Button>

                        <div className="contenedor-tabla">
                                <Table hover>
                                        <thead>
                                                <tr>
                                                        <th className='celda-tabla'>
                                                                <input
                                                                        type="checkbox"
                                                                        checked={selectedRows.size === data.length}
                                                                        onChange={handleSelectAll}
                                                                />
                                                        </th>
                                                        <th className='celda-tabla' onClick={() => handleSort('nombre_estudiante')}>
                                                                Nombre Estudiante {sortColumn === 'nombre_estudiante' && (sortDirection === 'asc' ? '↑' : '↓')}
                                                        </th>
                                                        <th className='celda-tabla' onClick={() => handleSort('email')}>
                                                                Email {sortColumn === 'email' && (sortDirection === 'asc' ? '↑' : '↓')}
                                                        </th>
                                                        <th className='celda-tabla' onClick={() => handleSort('promedio_notas')}>
                                                                Promedio Notas {sortColumn === 'promedio_notas' && (sortDirection === 'asc' ? '↑' : '↓')}
                                                        </th>
                                                </tr>
                                        </thead>
                                        <tbody>
                                                {data.map(item => (
                                                        <tr key={item.id_estudiante} onClick={() => handleRowSelect(item.id_estudiante)}>
                                                                <td className='celda-tabla'>
                                                                        <input
                                                                                type="checkbox"
                                                                                checked={selectedRows.has(item.id_estudiante)}
                                                                                onChange={() => handleRowSelect(item.id_estudiante)}
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
