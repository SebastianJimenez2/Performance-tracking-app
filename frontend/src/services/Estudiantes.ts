import { Estudiante } from "../types/RegistroNotas";

export const obtenerEstudiantes = async (
  asignatura: number,
  periodo: number,
  curso: number
): Promise<Estudiante[]> => {
  const url = `https://syncademic-0-1.onrender.com/syncademic/control-notas/estudiantes/${asignatura}/${periodo}/${curso}//`;

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
