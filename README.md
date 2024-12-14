# Gestión de Tareas

Esta es una aplicación de gestión de tareas desarrollada en Python utilizando Streamlit y SQLAlchemy. Permite a los usuarios agregar, listar, completar y eliminar tareas, así como importar y exportar tareas desde y hacia un archivo JSON.

## Estructura del Proyecto

El proyecto contiene los siguientes archivos:

- `app.py`: Archivo principal que contiene la lógica de la aplicación y la interfaz de usuario.
- `database.py`: Archivo que maneja la conexión a la base de datos SQLite y la creación de sesiones.
- `models.py`: Archivo que define el modelo de datos para las tareas utilizando SQLAlchemy.
- `Iniciar_app.bat`: Script para iniciar la aplicación con Streamlit.
- `tasks.db`: Base de datos SQLite donde se almacenan las tareas.
- `tasks.json`: Archivo JSON para importar y exportar tareas.

## Funcionalidades

- **Agregar Tarea**: Permite al usuario agregar una nueva tarea con un título y una descripción.
- **Listar Tareas**: Muestra todas las tareas, con la opción de filtrar por estado (pendientes o completadas).
- **Completar Tarea**: Permite marcar una tarea como completada.
- **Eliminar Tarea**: Permite eliminar una tarea específica.
- **Eliminar Tareas Completadas**: Permite eliminar todas las tareas que han sido completadas.
- **Exportar Tareas**: Exporta todas las tareas a un archivo JSON.
- **Importar Tareas**: Importa tareas desde un archivo JSON.

## Requisitos

- Python 3.x
- Streamlit
- SQLAlchemy

## Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/tu_usuario/gestion-tareas.git
   cd gestion-tareas
   
2. Instala las dependencias:
   -`pip install streamlit sqlalchemy`

3. Inicia la aplicación:
   -`streamlit run app.py`



