#Importa la clase os
import os

#Importa un módulo para pause en linux
from getch import getch, pause


# Clase consola aplicando patron facade a funciones propias de python
class Console():
    __commandsExecuteForSystemOperative = {
        "linux" : [ lambda: pause(), "clear" ],
        "windows" : [ lambda: os.system("pause"), "cls" ],
    }

    # Escribir una linea sin salto de linea con un mensaje pasado por parametros
    @staticmethod
    def write(message): print(message, end = " ")


    # Escribir una linea con salto de linea con un mensaje pasado por parametros
    @staticmethod
    def writeJumpLine(message): print(message)


    # Escribir lineas a traves de una lista pasada por parametros
    @staticmethod
    def writeList(msgList):
        for index, value in enumerate(msgList): Console.writeJumpLine(f"{(index + 1)}. {value}")


    # Leer un mensaje a traves de la consola
    @staticmethod
    def read(message, variable):
        result = variable
        while variable == result:
            result = Console.readOption(message, variable)
            if result == variable: Console.writeJumpLine("\r\n Datos introducidos invalidos, intente de nuevo\r\n")
        return result


    # Leer una opcion a traves de la consola
    @staticmethod
    def readOption(message, variable):
        value = input(message)
        if Console.equalsSameType([variable, value], "numeric"):
            return float(value) if value.find(".") != -1 else int(value)
        elif Console.equalsSameType([variable, value], "string"): return value
        return variable


    @staticmethod
    def equalsSameType(values, validType = "numeric"):
        conditionForType = {
            "numeric" : [Console.isNumeric(value) for value in values],
            "string": [not Console.isNumeric(value) for value in values],
        }
        return all(conditionForType[validType])


    # Valida si un valor es numerico
    @staticmethod
    def isNumeric(value):
        return str(value).strip().isdigit()


    # Limpia la pantalla
    @staticmethod
    def clearScreen():
        os.system(Console.__commandsExecuteForSystemOperative[Console.__getNameOperatingSystem()][1])


    # Lee una tecla para quitar una pausa
    @staticmethod
    def readKey():
        Console.__commandsExecuteForSystemOperative[Console.__getNameOperatingSystem()][0]()


    @staticmethod
    def __getNameOperatingSystem():
        return "windows" if os.name in ["dos" , "ce" , "nt"] else "linux"


    # Retorna un valor formateado sin espacios y luego válida si es numerica
    @staticmethod
    def validateOptions(value):
        return int(value) if value.strip().isdigit() else 0


