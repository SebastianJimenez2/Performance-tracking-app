import { Cronograma, TemaCronograma } from "../types/Cronograma";

export const obtenerCronogramas = async (): Promise<Cronograma[]> => {
  const url = `https://syncademic-0-1.onrender.com/syncademic/cronograma/`;

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

export const obtenerTemasCronograma = async (idCronograma: number): Promise<TemaCronograma[]> => {
  const url = `https://syncademic-0-1.onrender.com/syncademic/cronograma/temas-cronograma/${idCronograma}/`;

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
      return data.temas;
    })
    .catch((error) => {
      console.error("Fetch error:", error);
      throw error;
    });
};
