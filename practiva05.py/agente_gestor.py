# nuevo_programa.py
from gestor_comandos import analizar_comando

def iniciar_interfaz():
    print("agente de comandos")

    while True:
        entrada = input("Usuario >> ")
        if entrada.lower().strip() in ["salir", "exit"]:
            print("Programa finalizado. ¡Hasta luego!")
            break

        # Reutilización de los comandos del archivo base
        respuesta = analizar_comando(entrada)
        print(f"Sistema >> {respuesta}\n")

if __name__ == "__main__":
    iniciar_interfaz()
