import datetime

@staticmethod
# Llamar a este metodo cada vez que se ingrese un nuevo tema_cronograma y insertar el resultado en cronograma.estado
def obtener_estado_cronograma(temas_completados, temas_esperados):
    if temas_completados == temas_esperados:
        return "normal"
    elif temas_esperados < temas_completados:
        return "adelantado"
    
    return "atrasado"

@staticmethod
def obtener_progreso(temas_completados, temas_esperados):
    if temas_completados == temas_esperados:
        return "Todos los temas hasta la semana actual están marcados"
    elif temas_esperados < temas_completados:
        return "Temas de semanas futuras están marcados"
    
    return "Faltan temas por marcar en la semana actual "

@staticmethod
def sumar_semanas(fecha, semanas):
    fecha_resultado = fecha + datetime.timedelta(weeks=semanas)
    return fecha_resultado

@staticmethod
# get semana actual a partir de una fecha
def calcular_semana_relativa(fecha_inicio_str, fecha_dada_str):
    """
    Calcula la cantidad de semanas completas entre la fecha de inicio y una fecha dada.
    
    Parámetros:
    - fecha_inicio_str (str): Fecha de inicio en formato 'dd-mm-aa'.
    - fecha_dada_str (str): Fecha dada en formato 'dd-mm-aa'.
    
    Retorna:
    - int: Número de semanas completas desde la fecha de inicio hasta la fecha dada.
    """
    # Convertir las cadenas de fecha en objetos datetime
    fecha_formato = "%d-%m-%y"  # Definir el formato de fecha
    fecha_inicio = datetime.strptime(fecha_inicio_str, fecha_formato)
    fecha_dada = datetime.strptime(fecha_dada_str, fecha_formato)
    
    # Calcular la diferencia en días entre las dos fechas
    diferencia_dias = (fecha_dada - fecha_inicio).days
    
    # Convertir la diferencia de días en semanas completas
    semanas_completas = diferencia_dias // 7  # Usar división entera para obtener semanas completas
    
    return semanas_completas