import datetime

def obtener_saludo (nombre_bot):
    """
    retorna saludo
    """
    return f"hola, soy {nombre_bot} y quiero ayudarte"
def procesar_comando (comando):

    """
    valida y procesa la acción de recortar dato
    """
    if not comando:
        return "error: Faltar el nombre."
def calcular_uptime(hora_inicio):
    """
    Calcula el tiempo de actividad del agente
    """
    hora_actual = datetime.datetime.now()
    uptime = hora_actual - hora_inicio
    return f"Tiempo de actividad: {uptime}"
    print("")
def mostrar_ayuda():
    return(
        "comendos disponibles: \n"
        "saludo: Muestra un saludo \n"
        "recordar nombre: -El bot recordará el nombre proporcionado\n"
        "!uptime : Muestra el tiempo de actividad con bot\n"
        "!ayuda - muestra lista de comandos \n"
    )
def iniciar_agente():
     nombre_bot="Susanita"
     Prefijo= "!"
     hora_inicio=datetime.datetime.now()
     print(f"{obtener_saludo(nombre_bot)}")
     print("escribe !ayuda para ver los comandos disponibles.")

     ejecutando=True
     while ejecutando:
        entrada=input(f"{nombre_bot} Ingrese comando: ").strip()

        if not entrada.startswith(Prefijo):
            print("comando no reconocido.")
            continue

        partes= entrada[len(Prefijo):].split(maxsplit=1)
        comando= partes[0].lower()
        argumento=partes[1] if len(partes) > 1 else ""

        if comando =="saludo":
          print(obtener_saludo(nombre_bot))
        elif comando =="ayuda":
         print(mostrar_ayuda()) 
        elif comando== "salir":
            print("Hasta luego!")
            ejecutando= False
        elif comando == "uptime":
           print(calcular_uptime(hora_inicio))
        else:
         print("comando no reconocido")


def main():
    iniciar_agente()
if __name__=="__main__":
    main()