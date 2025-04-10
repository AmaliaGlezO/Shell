# shell_v1.py - Versión básica
import os
import subprocess



def ejecutar_comando(lista_elementos):
    global trabajos, contador_trabajos

    if not lista_elementos:
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