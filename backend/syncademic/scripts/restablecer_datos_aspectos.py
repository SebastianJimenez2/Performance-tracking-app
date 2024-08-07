from datetime import datetime
from syncademic.models.aspecto import Aspecto, Docente

def run():
    # Obtener el docente Ana Marciana o crear uno si no existe
    docente, created = Docente.objects.get_or_create(
        id_docente=3,
        defaults={'nombre': 'Ana Marciana', 'correo': 'profesor_c@example.com', 'estado': 'activo'}
    )

    if not created:
        print(f"El docente {docente.nombre} ya existe. Actualizando aspectos...")

    # Borrar todos los aspectos existentes de este docente
    Aspecto.objects.filter(docente=docente).delete()

    # Subaspectos para Docencia - Estado CRÍTICO
    subaspectos_docencia = [
        {'nombre': 'Registro_clase', 'progreso': 10},
        {'nombre': 'Tutoría', 'progreso': 20},
        {'nombre': 'Planificación', 'progreso': 30}
    ]

    # Crear el aspecto de Docencia
    aspecto_docencia = Aspecto.objects.create(
        nombre="Docencia",
        fecha_inicio=datetime(2024, 6, 1),
        fecha_fin=datetime(2024, 8, 7),
        subaspectos=subaspectos_docencia,
        docente=docente
    )

    # Subaspectos para Gestión - Estado INTENSO
    subaspectos_gestion = [
        {'nombre': 'Administración', 'progreso': 10},
        {'nombre': 'Comité', 'progreso': 15},
        {'nombre': 'Capacitación', 'progreso': 5}
    ]

    # Crear el aspecto de Gestión
    aspecto_gestion = Aspecto.objects.create(
        nombre="Gestión",
        fecha_inicio=datetime(2024, 6, 1),
        fecha_fin=datetime(2024, 9, 10),
        subaspectos=subaspectos_gestion,
        docente=docente
    )

    # Subaspectos para Investigación - Estado BAJO (Inactivo)
    subaspectos_investigacion = [
        {'nombre': 'TIC', 'progreso': 0},
        {'nombre': 'Conferencias', 'progreso': 0},
        {'nombre': 'Publicaciones', 'progreso': 0}
    ]

    # Crear el aspecto de Investigación
    aspecto_investigacion = Aspecto.objects.create(
        nombre="Investigación",
        fecha_inicio=datetime(2024, 9, 30),
        fecha_fin=datetime(2024, 12, 1),
        subaspectos=subaspectos_investigacion,
        docente=docente
    )

    print("Datos de prueba creados o actualizados con éxito.")
