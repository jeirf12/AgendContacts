#Importa toda la clase donde esta el crud de contactos
from controller import Agend

#Importa módulos para ajustes de la consola
from console import Console

#Importa módulos para ajustes de un menu generico
from menugeneric import Menu


class MenuMain(Menu):
    def __init__(self, title, options):
        self.agend = Agend()
        super(MenuMain, self).__init__(title, options)


    def _processOption(self):
        match int(self._option):
            case 1: self.agend.createContact()
            case 2: self.agend.editContact()
            case 3: self.agend.showContacts()
            case 4: self.agend.seekContact()
            case 5: self.agend.deleteContact()
            case 6: Console.writeJumpLine("Gracias por utilizar el programa")


