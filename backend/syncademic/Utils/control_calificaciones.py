# TODO: Funciones para el control de calificaciones

def verificar_riesgo(minimo_aceptable: float, cercania: float, promedio: float):
    return promedio - minimo_aceptable <= cercania


def definir_alerta(incidencias: int):
    if 0 < incidencias < 3:
        return "MEDIA"
    elif incidencias >= 3:
        return "ALTA"

    return None
