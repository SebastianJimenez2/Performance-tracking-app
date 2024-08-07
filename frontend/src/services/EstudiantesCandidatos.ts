import { EstudianteCandidato } from "../types/EstudiantesCandidatos";

export const obtenerSeguimientoMalla = async (tituloCurso: string): Promise<EstudianteCandidato[] | { error: string }> => {
    const url = `https://syncademic-0-1.onrender.com/syncademic/seguimiento-malla/${quitarEspaciosYAcentos(tituloCurso)}/2024B/`;

    try {
        const response = await fetch(url, {
            method: "GET",
            headers: {
                "Content-Type": "application/json",
            },
        });

        if (!response.ok) {
            const errorData = await response.json();
            if (errorData.Error) {
                return { error: errorData.Error };
            }
            throw new Error("Network response was not ok");
        }

        const data = await response.json();
        return data;
    } catch (error) {
        console.error("Fetch error:", error);
        throw error;
    }
};

function quitarEspaciosYAcentos(text: string): string {
        // Mapeo de caracteres con tilde a caracteres sin tilde
        const accentsMap: { [key: string]: string } = {
            'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u',
            'Á': 'A', 'É': 'E', 'Í': 'I', 'Ó': 'O', 'Ú': 'U'
        };
    
        // Eliminar espacios y reemplazar caracteres con tilde
        return text
            .split('') // Convertir la cadena en un array de caracteres
            .map(char => accentsMap[char] || char) // Reemplazar caracteres con tilde
            .join('') // Unir los caracteres de nuevo en una cadena
            .replace(/\s+/g, ''); // Eliminar espacios
    }
