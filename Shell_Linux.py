# shell_v1.py - Versión básica
import os
import subprocess

historial = {}

def reindexar_historial():
    global historial
    comandos = list(historial.values())
    historial = {i+1: cmd for i, cmd in enumerate(comandos)}

def obtener_historial_como_lista():
    return list(historial.items())

def ejecutar_comando(lista_elementos):
    global trabajos, contador_trabajos

    if not lista_elementos:
        return
    
    # Comandos internos
    if lista_elementos[0] == 'cd':
        try:
            destino = lista_elementos[1] if len(lista_elementos) > 1 else os.path.expanduser("~")
            os.chdir(destino)
        except Exception as err:
            print("cd:", err)
        return
    
    if lista_elementos[0] == 'history':
        for clave, cmd in obtener_historial_como_lista():
            print(f"{clave}  {cmd}")
        return
    


def principal():
    global historial
    while True:
        try:
            linea_comando = input("$ ")
        except EOFError:
            print()
            break

        if not linea_comando.strip():
            continue

if __name__ == "__main__":
    principal()