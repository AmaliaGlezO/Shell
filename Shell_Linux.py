import os
import re
import subprocess

historial = {}
# Lista de trabajos en segundo plano
trabajos = []
contador_trabajos = 1  # Identificador incremental para trabajos

def reindexar_historial():
    """Reindexa el historial para que las claves sean consecutivas a partir del 1."""
    global historial
    comandos = list(historial.values())
    historial = {i+1: cmd for i, cmd in enumerate(comandos)}