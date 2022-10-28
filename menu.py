#Importa toda la clase donde esta el crud de contactos
from headCrud import createContact, editContact, showContacts, seekContact, deleteContact

#Importa módulos para ajustes de la consola
from console import Console

#Importa módulos para ajustes de un menu generico
from menugeneric import Menu

class MenuMain(Menu):
    def __init__(self, title, options):
        super(MenuMain, self).__init__(title, options)

    def _processOption(self):
        match int(self._option):
            case 1: createContact()
            case 2: editContact()
            case 3: showContacts()
            case 4: seekContact()
            case 5: deleteContact()
            case 6: Console.writeJumpLine("Gracias por utilizar el programa")

