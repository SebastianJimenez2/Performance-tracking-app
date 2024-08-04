from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import datetime
from syncademic.models import Docente, Aspecto, Notificacion

class DisparadorAPIView(APIView):
    def get(self, request, id_docente):
        try:
            docente = Docente.objects.get(id_docente=id_docente)
            nombre = docente.nombre
            fecha_actual = datetime.now().date()
            aspectos = Aspecto.objects.filter(docente=docente)
            aspectos_info = []

            for aspecto in aspectos:
                if fecha_actual >= aspecto.fecha_inicio:
                    estado_notificacion = aspecto.determinar_estado_notificacion(
                        aspecto.calcular_tiempo_transcurrido(),
                        aspecto.calcular_progreso_actual()
                    )

                    # Construir mensaje según el estado de la notificación
                    mensaje = {
                        'estado_aspecto': 'Activo',
                        'nombre_aspecto': aspecto.nombre,
                        'fecha_fin': aspecto.fecha_fin.isoformat(),
                        'estado_notificacion': estado_notificacion,
                        'progreso_general_porcentaje': aspecto.calcular_progreso_actual(),
                        'tiempo_transcurrido_porcentaje': aspecto.calcular_tiempo_transcurrido()
                    }

                    if estado_notificacion in ["CRITICO", "INTENSO"]:
                        # Agregar información detallada de los subaspectos
                        mensaje['subaspectos'] = aspecto.subaspectos

                    notificacion = Notificacion.objects.create(
                        aspecto=aspecto,
                        estado=estado_notificacion,
                        mensaje=mensaje
                    )

                    es_dia_notificacion = notificacion.comportarse_segun(estado_notificacion)

                    aspectos_info.append({
                        'nombre_aspecto': aspecto.nombre,
                        'estado_notificacion': estado_notificacion,
                        'notificaciones_disponibles': es_dia_notificacion,
                        'mensaje': mensaje if es_dia_notificacion else {}
                    })

                else:
                    aspectos_info.append({
                        'nombre_aspecto': aspecto.nombre,
                        'estado_notificacion': "INACTIVO",
                        'notificaciones_disponibles': False,
                        'mensaje': {
                            'estado_aspecto': 'Inactivo',
                            'nombre_aspecto': aspecto.nombre,
                            'fecha_inicio': aspecto.fecha_inicio.isoformat(),
                            'fecha_fin': aspecto.fecha_fin.isoformat()
                        }
                    })

            response_data = {
                'nombre_docente': nombre,
                'notificaciones': aspectos_info
            }
            return Response(response_data)
        except Docente.DoesNotExist:
            return Response({'error': 'Docente no encontrado'}, status=404)
