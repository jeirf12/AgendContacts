from console import Console
from abc import ABC, abstractmethod


class Menu(ABC):
    def __init__(self, title, options):
        self.__title = title
        self.__options = options
        self._option = 0
        self._isActiveReadKey = True
        self.__exitOption = len(options) + 1
        self.__repeatedMenu()


    def __repeatedMenu(self):
        while self._option != self.__exitOption:
            Console.clearScreen()
            self._isActiveReadKey = True
            self.__showMenu()
            self.__readOption()
            self._processOption()
            if self._isActiveReadKey: Console.readKey()
        Console.clearScreen()


    def __showMenu(self):
        Console.writeJumpLine(self.__title)
        Console.writeList(self.__options)
        Console.writeJumpLine(f"{self.__exitOption}. Para salir...")


    def __readOption(self):
        self._option = 0
        self._option = Console.readOption("Ingrese la opcion deseada: \r\n", self._option)
        if(self._option < 1 or self._option > self.__exitOption): Console.writeJumpLine("\r\n Opción no válida, intente de nuevo\r\n")


    @abstractmethod
    def _processOption(self): pass


