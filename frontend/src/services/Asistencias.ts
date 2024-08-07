import { Asistencia, EstudiantesEnRiesgoResponse } from '../types/Asistencia';

const BASE_URL = 'https://syncademic-0-1.onrender.com/syncademic';

export const obtenerEstudiantesEnRiesgo = async ( mes: number): Promise<EstudiantesEnRiesgoResponse> => {
  const url = `${BASE_URL}/asistencia/estudiantes-en-riesgo/${mes}/`;
  const response = await fetch(url);
  
  if (!response.ok) {
    throw new Error('Error al obtener los datos');
  }
  
  const data: EstudiantesEnRiesgoResponse = await response.json();
  return data;
};