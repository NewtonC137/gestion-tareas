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
   git clone https://github.com/NewtonC137/gestion-tareas.git
   cd gestion-tareas
   
2. Instala las dependencias:
-`pip install streamlit sqlalchemy`

3. Inicia la aplicación:
-`streamlit run app.py`


## Uso

A continuación se muestra cómo utilizar el administrador de tareas:

### Agregar Tarea

1. Ingresa un título y una descripción para la nueva tarea.
2. Haz clic en "Agregar".

![Agregar](https://github.com/user-attachments/assets/847da0aa-87f0-406e-8ac9-7fd6dea8c4be)


### Listar Tareas

- Las tareas se mostrarán en la lista. Puedes filtrar por estado (todas, pendientes, completadas).

![Listar Tareas]([Imagenes/listar_tareas.png](https://github.com/NewtonC137/gestion-tareas/blob/main/Imagenes/Agregar.png?raw=true)](https://github.com/NewtonC137/gestion-tareas/blob/main/Imagenes/Listar.png?raw=true))

### Completar Tarea

- Haz clic en "Completada" para marcar una tarea como completada.

![Completar Tarea]([ruta/a/tu/imagen/completar_tarea.png](https://github.com/NewtonC137/gestion-tareas/blob/main/Imagenes/Completar.png?raw=true))

### Eliminar Tarea

- Haz clic en "Eliminar" para borrar una tarea específica.

![Eliminar Tarea]([ruta/a/tu/imagen/eliminar_tarea.png](https://github.com/NewtonC137/gestion-tareas/blob/main/Imagenes/Eliminar.png?raw=true))

### Eliminar Tareas Completadas

- Haz clic en "Eliminar tareas completadas" para borrar todas las tareas que ya han sido completadas.

![Eliminar Tareas Completadas]([ruta/a/tu/imagen/eliminar_tareas_completadas.png](https://github.com/NewtonC137/gestion-tareas/blob/main/Imagenes/Eliminar_completadas1.png?raw=true))(https://github.com/NewtonC137/gestion-tareas/blob/main/Imagenes/Eliminar_completadas2.png?raw=true)

### Exportar e Importar Tareas

- Usa los botones correspondientes para exportar las tareas a un archivo JSON o importar tareas desde un archivo JSON.

![Exportar e Importar Tareas]([ruta/a/tu/imagen/exportar_importar_tareas.png](https://github.com/NewtonC137/gestion-tareas/blob/main/Imagenes/Importar1.png?raw=true)https://github.com/NewtonC137/gestion-tareas/blob/main/Imagenes/Importar2.png?raw=true)
