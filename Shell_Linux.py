# shell_v1.py - Versión básica
import os
import subprocess

def main():
    while True:
        comando = input("$ ").strip()
        if comando == "exit":
            break
        os.system(comando)

if __name__ == "__main__":
    main()


def ejecutar_comando(lista_elementos):
    subprocess.run(lista_elementos, shell=True)