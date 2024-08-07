import { EstudianteCandidato } from "../types/EstudiantesCandidatos";

export const obtenerSeguimientoMalla = async (tituloCurso: string): Promise<EstudianteCandidato[] | { error: string }> => {
    const url = `https://syncademic-0-1.onrender.com/syncademic/seguimiento-malla/${tituloCurso}/2024B/`;

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
