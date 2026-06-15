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
    lista_tareas.append(nueva_tarea)
    return f"tarea agregada co exito"
def listar_tareas(lista_tareas):
    """
    formatea la lista de tareas para su vixualización
    """
    if not lista_tareas:
        return "no hay tareas"
    #agregar variable llamada resultado
    resultado="listado de areas: \n"
    #alterar l lista de tareas y formatea la salida
    for i, tarea in enumerate(lista_tareas, start=1):
        resultado += f"{i}. {tarea}\n"
    return resultado
def eliminar_tarea(lista_tareas, indice):
    """
    eliminar tarea por su numero de indice
    """
    if not indice.isdigit():
        return "Error: Debe ser número"
    indice= int(indice)-1
    #agregamos logica para preguntar
    # 
    #si el elemento en la lista y eliminarlo
    if 0 <= indice < len(listar_tareas):
        tarea_eliminada=lista_tareas.pop(indice)
    else:
        return "error: no existe la tarea"
    return f"tarea eliminada {tarea_eliminada}"
def main():
    tareas= []
    prefijo="!"

    print("Bienvenido al gestor de tareas")
    activa= True
    while activa:
        entrada= input(">>>"). strip()
        if not entrada.startswith(prefijo):
            print("error:comndo no reconocido")
            continue
        #procediiento de la entrada
        cuerpo= entrada[len(prefijo):].split(maxsplit=1)
        comando= cuerpo[0].lower()
        argumento= cuerpo[1] if len(cuerpo)> 1 else ""

        #seleccion d accion
        if comando=="add":
            resultado=agregar_tarea(tareas, argumento)
            print