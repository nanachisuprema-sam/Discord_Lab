import datetime

def agregar_tarea(lista_tareas, descripcion):
    """
    agregar tarea a la lista al cumplir requisitos
    """
    if len(descripcion)< 3:
        return "error nmms"
    #crear formato para tarea
    fecha= datetime.datetime.now().strftime("%H:%M")
    nueva_tarea=f"{descripcion} - {fecha}"