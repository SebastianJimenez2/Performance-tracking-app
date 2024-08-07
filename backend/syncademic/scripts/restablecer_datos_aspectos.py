from datetime import datetime
from syncademic.models.aspecto import Aspecto, Docente


def run():
    # Obtener el docente Ana Marciana o crear uno si no existe
    docente, created = Docente.objects.get_or_create(
        id_docente=3
    )

    if not created:
        print(f"El docente {docente_ana.nombre} ya existe. Actualizando aspectos...")

    # Subaspectos para Docencia - Estado CRÍTICO
    subaspectos_docencia_ana = [
        {'nombre': 'Registro_clase', 'progreso': 10},
        {'nombre': 'Tutoría', 'progreso': 20},
        {'nombre': 'Planificación', 'progreso': 30}
    ]

    # Crear el aspecto de Docencia
    Aspecto.objects.create(
        nombre="Docencia",
        fecha_inicio=datetime(2024, 6, 1),
        fecha_fin=datetime(2024, 8, 7),
        subaspectos=subaspectos_docencia_ana,
        docente=docente_ana
    )

    # Subaspectos para Gestión - Estado INTENSO
    subaspectos_gestion_ana = [
        {'nombre': 'Administración', 'progreso': 10},
        {'nombre': 'Comité', 'progreso': 15},
        {'nombre': 'Capacitación', 'progreso': 5}
    ]

    # Crear el aspecto de Gestión
    Aspecto.objects.create(
        nombre="Gestión",
        fecha_inicio=datetime(2024, 6, 1),
        fecha_fin=datetime(2024, 9, 10),
        subaspectos=subaspectos_gestion_ana,
        docente=docente_ana
    )

    # Subaspectos para Investigación - Estado BAJO (Inactivo)
    subaspectos_investigacion_ana = [
        {'nombre': 'TIC', 'progreso': 0},
        {'nombre': 'Conferencias', 'progreso': 0},
        {'nombre': 'Publicaciones', 'progreso': 0}
    ]

    # Crear el aspecto de Investigación
    Aspecto.objects.create(
        nombre="Investigación",
        fecha_inicio=datetime(2024, 9, 30),
        fecha_fin=datetime(2024, 12, 1),
        subaspectos=subaspectos_investigacion_ana,
        docente=docente_ana
    )

    # Docente Fedelobo
    docente_fedelobo, created = Docente.objects.get_or_create(
        id_docente=1,
        defaults={'nombre': 'Fedelobo', 'correo': 'profesor_a@example.com', 'estado': 'activo'}
    )

    if not created:
        print(f"El docente {docente_fedelobo.nombre} ya existe. Actualizando aspectos...")

    # Subaspectos para Docencia - Estado NORMAL
    subaspectos_docencia_fedelobo = [
        {'nombre': 'Registro_clase', 'progreso': 60},
        {'nombre': 'Tutoría', 'progreso': 60},
        {'nombre': 'Planificación', 'progreso': 60}
    ]

    # Crear el aspecto de Docencia
    Aspecto.objects.create(
        nombre="Docencia",
        fecha_inicio=datetime(2024, 6, 1),
        fecha_fin=datetime(2024, 9, 1),
        subaspectos=subaspectos_docencia_fedelobo,
        docente=docente_fedelobo
    )

    # Subaspectos para Gestión - Estado INTENSO
    subaspectos_gestion_fedelobo = [
        {'nombre': 'Administración', 'progreso': 10},
        {'nombre': 'Comité', 'progreso': 15},
        {'nombre': 'Capacitación', 'progreso': 5}
    ]

    # Crear el aspecto de Gestión
    Aspecto.objects.create(
        nombre="Gestión",
        fecha_inicio=datetime(2024, 6, 1),
        fecha_fin=datetime(2024, 9, 10),
        subaspectos=subaspectos_gestion_fedelobo,
        docente=docente_fedelobo
    )

    # Subaspectos para Investigación - Estado BAJO
    subaspectos_investigacion_fedelobo = [
        {'nombre': 'TIC', 'progreso': 0},
        {'nombre': 'Conferencias', 'progreso': 0},
        {'nombre': 'Publicaciones', 'progreso': 0}
    ]

    # Crear el aspecto de Investigación
    Aspecto.objects.create(
        nombre="Investigación",
        fecha_inicio=datetime(2024, 6, 1),
        fecha_fin=datetime(2024, 12, 1),
        subaspectos=subaspectos_investigacion_fedelobo,
        docente=docente_fedelobo
    )

    print("Datos de prueba creados o actualizados con éxito.")
