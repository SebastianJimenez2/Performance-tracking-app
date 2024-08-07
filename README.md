<p align="center">
  <img src="frontend/src/assets/Logo.png" alt="Logo de SYNCADEMIC" width="700px"/>
</p>

¡Bienvenido a SYNCADEMIC! 🎓🚀

SYNCADEMIC es una innovadora aplicación web diseñada para la gestión académica, desarrollada con una robusta arquitectura de frontend y backend.

## Descripción

SYNCADEMIC es una aplicación orientada al seguimiento del rendimiendo tanto de estudiantes como de docentes permitiendo realizar actividades como:
- 🌞Identificar estudiantes que necesiten un curso de verano🌞
- 📖Identificar estudiantes con bajas calificaciones📖
- 🕥Notificar la carga horaria atrasada de un docente🕥
- 🖊️Realizar sugerencias para la planificación, tomando en consideración docentes con mayor afinidad a una asignatura🖊️
- 🏃Identificar aquellos estudiantes con posible tasa de abandono en base a su asistencia🏃
- ¡y más!

## Nuestro equipo de desarrollo
<p align="center">
  <img src="frontend/src/assets/EquipoDeDesarrollo.png" alt="Equipo de desarrollo" width="500px"/>
</p>

## Tecnologías Utilizadas

### Backend
- Python ![Python](https://img.shields.io/badge/Python-3.10-blue.svg)
- Django ![Django](https://img.shields.io/badge/Django-4.2-green.svg)
- Django REST Framework ![DRF](https://img.shields.io/badge/Django%20REST-3.14-blue.svg)
- Behave ![Behave](https://img.shields.io/badge/Behave-1.2.7-orange.svg)
- Gherkin ![Gherkin](https://img.shields.io/badge/Gherkin-6.0.0-green.svg)
- Faker ![Faker](https://img.shields.io/badge/Faker-14.1.1-yellow.svg)
- Docker ![Docker](https://img.shields.io/badge/Docker-24.0.2-blue.svg)

### Frontend
- Node.js ![Node.js](https://img.shields.io/badge/Node.js-18.17.1-green.svg)
- pnpm ![pnpm](https://img.shields.io/badge/pnpm-8.6.7-orange.svg)
- Vite ![Vite](https://img.shields.io/badge/Vite-4.3.9-yellow.svg)
- React ![React](https://img.shields.io/badge/React-18.2.0-blue.svg)
- TypeScript ![TypeScript](https://img.shields.io/badge/TypeScript-5.1.6-blue.svg)
- React Bootstrap ![React Bootstrap](https://img.shields.io/badge/React%20Bootstrap-2.8.0-blue.svg)
- ESLint ![ESLint](https://img.shields.io/badge/ESLint-8.45.0-purple.svg)

---

## Instalación y Ejecución del Proyecto

### Requisitos Previos

1. **Node.js y pnpm**
   - Asegúrate de tener Node.js instalado. Puedes descargarlo desde [aquí](https://nodejs.org/).
   - Instala pnpm (un gestor de paquetes rápido y eficiente) globalmente:
     ```sh
     npm install -g pnpm
     ```
   - Activar pnpm (ejecutar terminal como administrador)
     ```sh
     corepack enable pnpm
     ```


2. **Python y Django**
   - Asegúrate de tener Python instalado. Puedes descargarlo desde [aquí](https://www.python.org/).
   - Instala un IDE de confianza, sugerimos Pycharm (publicidad no pagada)

### Configuración del Frontend

1. Clona el repositorio:
```sh
git clone https://github.com/tu-usuario/syncademic.git
```

2. Navega al directorio del frontend:

```sh
cd /frontend
```

3. Instala las dependencias:

```sh
pnpm install
```

4. Ejecuta el proyecto en modo de desarrollo:

```sh
pnpm run dev
```

### Configuración del Backend

1. Clona el repositorio:
```sh
git clone https://github.com/tu-usuario/syncademic.git
```

2. Navega al directorio del backend:

```sh
cd /backend
```

3. Instala las dependencias:

```sh
pip install -r requirements.txt
```

4. Realiza las migraciones:

```sh
python manage.py makemigrations
python manage.py migrate
```

5. Ejecuta el servidor:

```sh
python manage.py runserver
```

## Contribuir
¡Las contribuciones son bienvenidas! Si deseas mejorar SYNCADEMIC, por favor sigue estos pasos:

1. Haz un fork del proyecto.
2. Crea una nueva rama 
```sh
git checkout -b feature/nueva-funcionalidad
```
3. Realiza tus cambios y haz commit 
```sh
git commit -m 'feat: agrega nueva funcionalidad'
```
4. Haz push a la rama 
```sh
git push origin feature/nueva-funcionalidad
```
5. Crea un nuevo Pull Request.

## Contribuidores

<img style="width:100%;" src="https://contrib.rocks/image?repo=SebastianJimenez2/Performance-tracking-app">

---

¡Gracias por usar SYNCADEMIC! Si tienes alguna pregunta o sugerencia, no dudes en abrir un issue o contactar a los mantenedores del proyecto.