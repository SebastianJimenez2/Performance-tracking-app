import { Nota, RespuestaRegistroNotas } from "../types/RegistroNotas";

export const registrarNotas = async (
  asignatura: number,
  periodo: number,
  curso: number,
  listaNotas: Nota[]
): Promise<RespuestaRegistroNotas> => {
  const url = `https://syncademic-0-1.onrender.com/syncademic/control-notas/${asignatura}/${periodo}/${curso}//`;

  return await fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(listaNotas),
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
