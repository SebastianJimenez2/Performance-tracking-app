export const actualizarEstadoTema = async (idTema: number, fechaActual: string, estado: string): Promise<void> => {
    const url = `https://syncademic-0-1.onrender.com/syncademic/tema-cronograma/${idTema}/check/`;
  
    return fetch(url, {
      method: "PUT",
      headers: {
        "Content-Type": "application/json",
        "Accept": "application/json"
      },
      body: JSON.stringify({ fecha_actual: fechaActual, estado: estado })
    })
      .then((response) => {
        if (!response.ok) {
          throw new Error("Network response was not ok");
        }
      })
      .catch((error) => {
        console.error("Fetch error:", error);
        throw error;
      });
  };
  