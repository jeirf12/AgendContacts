# Importa del módulo contacto todos los métodos
from model import *

# Importa módulos que no tiene nada que ver con el modelo
from console import Console

# Importa del módulo archivo todos los métodos
from archive import Archive

# Importa módulos para ajustes de un menu generico
from menugeneric import Menu


class MenuEdit(Menu):
    def __init__(self, title, options, editFunction, nameArchive):
        self.__editFunction = editFunction
        self.__nameArchive = nameArchive
        super(MenuEdit, self).__init__(title, options)


    def _processOption(self):
        match int(self._option):
            case 1: self.__nameArchive = self.__editFunction(self.__nameArchive, "name")
            case 2: self.__nameArchive = self.__editFunction(self.__nameArchive, "tag")
            case 3: self.__nameArchive = self.__editFunction(self.__nameArchive, "category")
            case 4: self.__nameArchive = self.__editFunction(self.__nameArchive, "number")
            case 5: self.__nameArchive = self.__editFunction(self.__nameArchive, "phone")
            case 6: self._isActiveReadKey = False


class Agend:
    def __init__(self):
        self.archive = Archive()
        self.archive.create()


    # Crea un contacto en la carpeta con su respectiva información
    def createContact(self):
        print('Escribe los datos para agregar el nuevo contacto')
        name = Console.read('Dígite el nombre del contacto nuevo: \r\n', "")
        nameArchive, exist = self.__existContact(name)
        if not exist:
            phones = self.__createPhones()
            category = Console.read('Dígite la categoría del contacto: \r\n', "")
            contact = Contact(name, category)
            for phone in phones: contact.setPhones(phone)
            self.__writeInArchive(nameArchive, contact)
            print(f'\r\n Contacto creado correctamente!\r\n')
        else: print('\r\n El contacto ya existe para crearlo\r\n')


    def __createPhones(self):
        phones = []
        otherPhone = 0
        while (otherPhone <= 1):
            tag = Console.read(f'Dígite la etiqueta del número: \r\n', "")
            phoneContact = self.__addPhone()
            phones.append(Phone(tag, phoneContact))
            otherPhone = self.__getValidCreateOtherPhone()
        return phones


    def __getValidCreateOtherPhone(self):
        optionPhone = 0
        while (optionPhone < 1 or optionPhone > 2):
            messageQuestion = '¿Desea agregar otro número?\n1. Si\n2. No\n'
            optionPhone = input(messageQuestion)
            optionPhone = Console.validateOptions(optionPhone)
        return optionPhone


    # Edita un contacto creado dentro de la carpeta
    def editContact(self):
        print('Escribe los datos del contacto a editar')
        name = input('Dígite el nombre o el número del contacto que desea editar: \r\n')
        nameArchive, exist = self.__existContact(name)
        if exist: self.__editMenu(nameArchive)
        else: print('\r\n El contacto para editar no existe \r\n')


    # Muestra todos los contactos que hay en la carpeta, y abre solo archivos con extensión .txt
    def showContacts(self):
        files = self.archive.getFiles()
        print('\r\n Información de los contactos \r\n')
        if len(files) > 0:
            for file in files: self.archive.showFile(file)
        else: print('\r\n No hay contactos para mostrar\r\n')


    # Busca un contacto por su nombre o número
    def seekContact(self):
        name = input('Dígite el nombre o número del contacto a buscar:\r\n')
        nameArchive, exist = self.__existContact(name)
        print('\r\n Información del Contacto: \r\n')
        if exist: self.archive.showFile(nameArchive)
        else: print('\r\n El contacto no se encuentra en la base de datos\r\n')


    # Elimina un contacto por su nombre
    def deleteContact(self):
        name = input('Dígite el nombre o el número del contacto a eliminar:\r\n')
        nameArchive, exist = self.__existContact(name)
        if exist:
            self.__deleteMenu(nameArchive)
            print('\r\n Contacto eliminado correctamente!\r\n')
        else: print('\r\n El contacto a eliminar no existe\r\n')


    def __existContact(self, nameContact):
        nameArchive = self.__getNameContact(nameContact.strip())
        exist = self.archive.existArchive(nameArchive)
        return nameArchive, exist


    def __editMenu(self, nameArchive):
        title = "Menu Editar Contacto"
        options = [
            'Desea editar el nombre',
            'Desea editar una etiqueta',
            'Desea editar una categoria',
            'Desea editar un número',
            'Desea agregar un nuevo número'
        ]
        MenuEdit(title, options, self.__editData, nameArchive)


    # Válida que el número se escriba correctamente
    def __addPhone(self, messagePhone = 'el teléfono'):
        phoneContact = ''
        while not phoneContact.isdigit() or len(phoneContact) < 10:
            if phoneContact == '': phoneContact = input(f'Dígite {messagePhone} del contacto: \r\n')
            elif (len(phoneContact) < 10): phoneContact = input(f'Dígite {messagePhone} del contacto correctamente (No se permite menos de 10 digitos): \r\n')
            else: phoneContact = input(f'Dígite {messagePhone} del contacto correctamente\n(No se pemite letras): \r\n')
            phoneContact = phoneContact.strip()
        return phoneContact


    def __deleteMenu(self, nameArchive):
        option = 0
        while option < 1 or option > 2:
            self.__deleteOptions()
            option = input('Elija una opción: ')
            option = Console.validateOptions(option.strip())
        self.__questionDelete(nameArchive, option)


    # Obtiene el nombre del contacto y agrega directorio preestablecido
    def __getNameContact(self, content):
        if content.isdigit() and len(content) == 10: nameArchive = self.archive.searchContent(content)
        else: nameArchive = self.archive.getNameArchive(content)
        return nameArchive


    def __writeInArchive(self, nameArchive, contact):
        content = f'Nombre: {contact.getName()}\r\n'
        for i, phone in enumerate(contact.getPhones(), 1):
            content += f'Etiqueta del telefono {i}: {phone.getTag()}\r\nTelefono {i}: {phone.getNumber()}\r\n'
        content += f'Categoria: {contact.getCategory()}\r\n'
        self.archive.writeFile(nameArchive, content)


    def __deleteOptions(self):
        print('1. Desea eliminar todo el contacto')
        print('2. Desea eliminar un número')


    def __questionDelete(self, nameArchive, option):
        if option == 1: self.archive.deleteArchive(nameArchive)
        else: self.__deleteNumber(nameArchive)


    def __deleteNumber(self, nameArchive):
        contact, option = self.__showDataAvalaible(nameArchive, 'number', 'delete')
        if len(contact.getPhones()) < 2: self.archive.deleteArchive(nameArchive)
        else:
            contact.getPhones().pop(option - 1)
            self.__writeInArchive(nameArchive, contact)


    def __editData(self, nameArchive, optionProperty):
        contact, option = self.__showDataAvalaible(nameArchive, optionProperty)
        match optionProperty:
            case "name": contact, nameArchive = self.__editName(contact)

            case "tag": contact = self.__editTag(contact, option)

            case "category": contact = self.__editCategory(contact)

            case "number": contact = self.__editNumber(contact, option)

            case "phone": contact = self.__editPhone(contact)

        self.__writeInArchive(nameArchive, contact)
        print(f'\r\n Contacto editado correctamente!\r\n')
        return nameArchive


    def __editName(self, contact):
        nameArchiveNew = self.archive.getNameArchive(contact.getName().strip())
        nameContact = input(f"Digite el nuevo nombre del contacto \"{contact.getName()}\" (si quiere dejar el mismo solo de enter): \n")
        if nameContact.strip() != "":
            nameArchiveOld, nameArchiveNew = nameArchiveNew, self.archive.getNameArchive(nameContact.strip())
            self.archive.renameArchive(nameArchiveOld, nameArchiveNew)
            contact.setName(nameContact)
        return contact, nameArchiveNew


    def __editTag(self, contact, option):
        tagContact = input(f"Digite la nueva etiqueta, la anterior es \"{contact.getPhones()[option - 1].getTag()}\" (si quiere dejar la etiqueta por defecto, debe dar enter):\n")
        if tagContact.strip() != "": contact.getPhones()[option - 1].setTag(tagContact)
        return contact


    def __editCategory(self, contact):
        categoryContact = input(f"Digite la nueva categoria, la anterior es \"{contact.getCategory()}\" (si quiere dejar el por defecto de enter): \n")
        contact.setCategory(contact.getCategory() if categoryContact.strip() == "" else categoryContact)
        return contact


    def __editNumber(self, contact, option):
        numberEdit = self.__addPhone('el nuevo teléfono')
        contact.getPhones()[option - 1].setNumber(numberEdit)
        return contact


    def __editPhone(self, contact):
        newTag = Console.read('Digite la nueva etiqueta para el nuevo numero: \n', "")
        newPhone = self.__addPhone('el nuevo teléfono')
        newPhoneContact = Phone(newTag, newPhone)
        contact.setPhones(newPhoneContact)
        return contact


    def __showDataAvalaible(self, nameArchive, nameProperty, method = 'edit'):
        contactContents = self.archive.getContentFile(nameArchive)
        contact = self.__getContact(contactContents)
        option = 0
        counter = 0
        while option < 1 or option > counter:
            counter = 0
            if not nameProperty in ['name', 'category', 'phone']:
                nameMessages = self.__getMessages(nameProperty)
                method = self.__getMessages('edit' if method == 'editar' else method)
                print(f'{nameMessages} a {method} son: ')
                for phone in contact.getPhones():
                    print(f'{counter + 1}. {phone.getNumber() if nameProperty == "number" else phone.getTag()}')
                    counter += 1
            elif counter == 0:
                break
            option = input('Elija una opción: ')
            option = Console.validateOptions(option)
        return contact, option


    def __getMessages(self, method):
        messages = {
            'number': 'Los números',
            'tag': 'Las etiquetas',
            'edit': 'editar',
            'delete': 'eliminar',
        }
        return messages[method]


    def __getContact(self, contacts):
        if len(contacts) <= 0: return Contact()
        contact = Contact(contacts[0], contacts[-1])
        for index, data in enumerate(contacts):
            if data.isnumeric(): contact.setPhones(Phone(contacts[index - 1], data))
        return contact


