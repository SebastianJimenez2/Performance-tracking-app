from datetime import datetime
from syncademic.models import Docente, Aspecto


def run():
    # Borrar todos los datos existentes
    Docente.objects.all().delete()
    Aspecto.objects.all().delete()

    # Crear el docente Carlos
    docente_carlos = Docente.objects.create(id_docente=500, nombre="Carlos", correo="carlos@example.com",
                                            estado="Activo")

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
        fecha_fin=datetime(2024, 8, 10),
        subaspectos=subaspectos_docencia,
        docente=docente_carlos
    )

    # Subaspectos para Gestión - Estado NORMAL
    subaspectos_gestion = [
        {'nombre': 'Administración', 'progreso': 10},
        {'nombre': 'Comité', 'progreso': 15},
        {'nombre': 'Capacitación', 'progreso': 5}
    ]

    # Crear el aspecto de Gestión
    aspecto_gestion = Aspecto.objects.create(
        nombre="Gestión",
        fecha_inicio=datetime(2024, 7, 1),
        fecha_fin=datetime(2024, 9, 10),
        subaspectos=subaspectos_gestion,
        docente=docente_carlos
    )

    # Subaspectos para Investigación - Estado INTENSO
    subaspectos_investigacion = [
        {'nombre': 'TIC', 'progreso': 20},
        {'nombre': 'Conferencias', 'progreso': 30},
        {'nombre': 'Publicaciones', 'progreso': 10}
    ]

    # Crear el aspecto de Investigación
    aspecto_investigacion = Aspecto.objects.create(
        nombre="Investigación",
        fecha_inicio=datetime(2024, 6, 1),
        fecha_fin=datetime(2024, 9, 1),
        subaspectos=subaspectos_investigacion,
        docente=docente_carlos
    )

    print("Datos de prueba creados con éxito.")
