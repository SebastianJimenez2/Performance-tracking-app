import { SeguimientoMalla } from "../types/SeguimientoMalla";

export const obtenerSeguimientoMalla = async (): Promise<SeguimientoMalla[]> => {
        const url = 'https://syncademic-0-1.onrender.com/syncademic/seguimiento-malla/ProgramacionI/2024B/';

        return fetch(url, {
                method: "GET",
                headers: {
                        "Content-Type": "application/json",
                },
        })
                .then((response) => {
                        if (!response.ok) {
                                throw new Error("Network response was not ok");
                        }
                        return response.json();
                })
                .then((data) => {
                        return data;
                })
                .catch((error) => {
                        console.error("Fetch error:", error);
                        throw error;
                });
};