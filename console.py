#Importa la clase os
import os

#Importa un módulo para pause en linux
from getch import getch, pause


# Clase consola aplicando patron facade a funciones propias de python
class Console():

    # Escribir una linea sin salto de linea con un mensaje pasado por parametros
    @staticmethod
    def write(message): print(message, end=" ")


    # Escribir una linea con salto de linea con un mensaje pasado por parametros
    @staticmethod
    def writeJumpLine(message): print(message)


    # Escribir lineas a traves de una lista pasada por parametros
    @staticmethod
    def writeList(msgList):
        for index,value in enumerate(msgList): Console.writeJumpLine(f"{(index + 1)}. {value}")


    # Leer un mensaje a traves de la consola
    @staticmethod
    def read(message, variable):
        result = variable
        while variable == result:
            result = Console.__readInput(message, variable)
            if result == variable: Console.writeJumpLine("\r\n Datos introducidos invalidos, intente de nuevo\r\n")
        return result


    # Leer una opcion a traves de la consola
    @staticmethod
    def readOption(message, variable): return Console.__readInput(message, variable)


    # Leer un mensaje a traves de la consola validando su tipo de dato
    @staticmethod
    def __readInput(message, variable):
        value = input(message)
        if Console.isNumeric(variable) and Console.isNumeric(value):
            if value.find(".") != -1: return float(value)
            else: return int(value)
        elif not Console.isNumeric(variable) and not Console.isNumeric(value): return value
        return variable


    # Valida si un valor es numerico
    @staticmethod
    def isNumeric(value):
        value = str(value).strip()
        return True if value.isdigit() else False
        

    # Limpia la pantalla
    @staticmethod
    def clearScreen():
        command = ""
        match os.name:
            case "posix": command = "clear"
            case "dos" | "ce" | "nt": command = "cls"
        os.system(command)


    # Lee una tecla para quitar una pausa
    @staticmethod
    def readKey():
        match os.name:
            case "posix": pause()
            case "dos" | "ce" | "nt": os.system("pause")


    # Retorna un valor formateado sin espacios y luego válida si es numerica
    @staticmethod
    def validateQuestions(value):
        value = value.strip()
        return int(value) if value.isdigit() else 0

