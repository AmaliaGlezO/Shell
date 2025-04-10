# shell_v1.py - Versión básica
import os
import re
import subprocess

historial = {}
trabajos = []
contador_trabajos = 1

def reindexar_historial():
    global historial
    comandos = list(historial.values())
    historial = {i+1: cmd for i, cmd in enumerate(comandos)}

def agregar_comando_al_historial(comando):
    global historial
    # Eliminar si ya existe el comando
    claves_a_eliminar = [clave for clave, cmd in historial.items() if cmd == comando]
    for clave in claves_a_eliminar:
        del historial[clave]
    # Agregar el nuevo comando al final
    historial[len(historial)+1] = comando
    # Si se exceden los 50 comandos, eliminar el primero y reindexar
    if len(historial) > 50:
        del historial[min(historial.keys())]
        reindexar_historial()


def obtener_historial_como_lista():
    return list(historial.items())


def analizar_linea_comando(linea):
    elementos = re.findall(r'>>|[><|&]|[^ ><|&]+', linea)
    elementos = [elem.strip() for elem in elementos if elem.strip() != '']
    return elementos


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
    
    if lista_elementos[0] == 'jobs':
        for trabajo in trabajos:
            proceso = trabajo['proceso']
            if proceso.poll() is None:
                print(f"[{trabajo['id']}] {trabajo['comando']}")
        return
    
    if lista_elementos[0] == 'fg':
        if len(lista_elementos) > 1:
            try:
                id_trabajo = int(lista_elementos[1])
                trabajo = next((t for t in trabajos if t['id'] == id_trabajo), None)
                if trabajo:
                    proceso = trabajo['proceso']
                    print(f"Trayendo al primer plano el trabajo [{id_trabajo}]: {trabajo['comando']}")
                    proceso.wait()
                    trabajos.remove(trabajo)
                else:
                    print("fg: no existe ese trabajo")
            except ValueError:
                print("fg: id de trabajo inválido")
        else:
            if trabajos:
                trabajo = trabajos.pop()
                proceso = trabajo['proceso']
                print(f"Trayendo al primer plano el trabajo [{trabajo['id']}]: {trabajo['comando']}")
                proceso.wait()
            else:
                print("fg: no hay trabajos")
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