import datetime

# Llamar a este metodo cada vez que se ingrese un nuevo tema_cronograma y insertar el resultado en cronograma.estado
def obtener_estado_cronograma(temas_completados, temas_esperados):
    if temas_completados == temas_esperados:
        return "normal"
    elif temas_esperados < temas_completados:
        return "adelantado"
    
    return "atrasado"

def obtener_progreso(temas_completados, temas_esperados):
    if temas_completados == temas_esperados:
        return "Todos los temas hasta la semana actual están marcados"
    elif temas_esperados < temas_completados:
        return "Temas de semanas futuras están marcados"
    
    return "Faltan temas por marcar en la semana actual "

def sumar_semanas(fecha, semanas):
    fecha_resultado = fecha + datetime.timedelta(weeks=semanas)
    return fecha_resultado