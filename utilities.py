#Importa la clase os
import os

#Importa un módulo para pause en linux
from getch import getch, pause

#Implementación del borrado de pantalla
def clearScreen():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system("cls")

#Implementación de leer tecla
def readkey():
    if os.name == "posix":
        pause()
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system("pause")

#válida cadenas numericas
def validateQuestions(value):
    value = value.strip()
    return int(value) if value.isdigit() else 0
