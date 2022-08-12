#Importa la clase os
import os

#Importa un módulo para pause en linux
from getch import getch, pause

class Console():
    @staticmethod
    def writeJumpLine(message):
        print(message)

    @staticmethod
    def writeList(msgList):
        for index,value in enumerate(msgList):
            Console.writeJumpLine(f"{(index + 1)}. {value}")

    @staticmethod
    def read(message, variable):
        result = variable
        while variable == result:
            result = Console.__readInput(message, variable)
            if result == variable: Console.writeJumpLine("\r\n Datos introducidos invalidos, intente de nuevo\r\n")
        return result

    @staticmethod
    def __readInput(message, variable):
        value = input(message)
        if Console.isNumeric(variable) and Console.isNumeric(value):
            if value.find(".") != -1: return float(value)
            else: return int(value)
        elif not Console.isNumeric(variable) and not Console.isNumeric(value): return value
        return variable

    @staticmethod
    def isNumeric(value):
        value = str(value).strip()
        return True if value.isdigit() else False

    @staticmethod
    def clearScreen():
        command = ""
        match os.name:
            case "posix": command = "clear"
            case "dos" | "ce" | "nt": command = "cls"
        os.system(command)

    @staticmethod
    def readKey():
        match os.name:
            case "posix": pause()
            case "dos" | "ce" | "nt": os.system("pause")
