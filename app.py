import streamlit as st
from database import get_session
from models import Task
import json

# Función para agregar una tarea
def add_task(title, description):
    session = get_session()
    try:
        new_task = Task(title=title, description=description)
        session.add(new_task)
        session.commit()
    except Exception as e:
        st.error(f"Error al agregar tarea: {e}")
    finally:
        session.close()

# Función para listar tareas
def list_tasks(filter_option=None):
    session = get_session()
    if filter_option == "Pendientes":
        tasks = session.query(Task).filter(Task.completed == False).all()
    elif filter_option == "Completadas":
        tasks = session.query(Task).filter(Task.completed == True).all()
    else:
        tasks = session.query(Task).all()
    session.close()
    return tasks

# Función para marcar una tarea como completada
def complete_task(task_id):
    session = get_session()
    task = session.query(Task).filter(Task.id == task_id).first()
    if task:
        task.completed = True
        session.commit()
    session.close()

# Función para eliminar una tarea específica
def delete_task(task_id):
    session = get_session()
    try:
        task = session.query(Task).filter(Task.id == task_id).first()
        if task:
            session.delete(task)
            session.commit()
    except Exception as e:
        st.error(f"Error al eliminar tarea: {e}")
    finally:
        session.close()

# Función para eliminar tareas completadas
def delete_completed_tasks():
    session = get_session()
    session.query(Task).filter(Task.completed == True).delete()
    session.commit()
    session.close()

# Función para exportar tareas a un archivo JSON
def export_tasks():
    session = get_session()
    tasks = session.query(Task).all()
    tasks_to_export = [
        {
            "id": task.id,
            "title": task.title,
            "description": task.description,
            "completed": task.completed
        }
        for task in tasks
    ]
    with open('tasks.json', 'w') as f:
        json.dump(tasks_to_export, f)
    session.close()

# Función para importar tareas desde un archivo JSON
def import_tasks():
    session = get_session()
    try:
        with open('tasks.json', 'r') as f:
            tasks = json.load(f)
            for task_data in tasks:
                task = Task(
                    title=task_data['title'],
                    description=task_data['description'],
                    completed=task_data['completed']
                )
                session.add(task)
            session.commit()
    except FileNotFoundError:
        st.error("El archivo tasks.json no se encontró.")
    except Exception as e:
        st.error(f"Error al importar tareas: {e}")
    finally:
        session.close()

# Interfaz de usuario con Streamlit
st.title("Gestión de Tareas")

# Agregar tarea
st.header("Agregar Tarea")
title = st.text_input("Título")
description = st.text_area("Descripción")
if st.button("Agregar"):
    if title.strip() == "":
        st.error("El título no puede estar vacío.")
    else:
        add_task(title, description)
        st.success("Tarea agregada exitosamente!")

# Filtrar tareas
filter_option = st.selectbox("Filtrar tareas por estado", ["Todas", "Pendientes", "Completadas"])
tasks = list_tasks(filter_option)

# Listar tareas
st.header("Lista de Tareas")
for task in tasks:
    st.markdown("---")  # Separador entre tareas
    col1, col2 = st.columns([3, 2])
    with col1:
        status = "Completada" if task.completed else "Pendiente"
        st.write(f"**{task.title}** ({status})")
        st.write(task.description)
    with col2:
        btn1, btn2 = st.columns(2)  # Botones lado a lado
        with btn1:
            if not task.completed:
                if st.button("Completada", key=f"complete_{task.id}"):
                    complete_task(task.id)
                    st.rerun()
        with btn2:
            if st.button("Eliminar", key=f"delete_{task.id}"):
                delete_task(task.id)
                st.rerun()

# Botones para eliminar tareas completadas, exportar e importar tareas
st.markdown("---")  
col5, col6 = st.columns([2, 2])
with col5:
    if st.button("Eliminar tareas completadas"):
        delete_completed_tasks()
        st.rerun()
with col6:
    col7, col8 = st.columns(2)
    with col7:
        if st.button("Exportar tareas"):
            export_tasks()
            st.rerun()
    with col8:
        if st.button("Importar tareas"):
            import_tasks()
            st.rerun()

# Fin de la aplicación
