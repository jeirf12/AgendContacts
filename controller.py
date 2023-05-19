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
        self.editFunction = editFunction
        self.nameArchive = nameArchive
        super(MenuEdit, self).__init__(title, options)


    def _processOption(self):
        match int(self._option):
            case 1: self.editFunction(self.nameArchive, "name")
            case 2: self.editFunction(self.nameArchive, "tag")
            case 3: self.editFunction(self.nameArchive, "category")
            case 4: self.editFunction(self.nameArchive, "number")
            case 5: self.editFunction(self.nameArchive, "phone")
            case 6: self._isActiveReadKey = True


class Agend:
    def __init__(self): 
        self.archive = Archive()
        self.archive.create()


    # Crea un contacto en la carpeta con su respectiva información
    def createContact(self):
        print('Escribe los datos para agregar el nuevo contacto')
        self.__saveDatArchive()


    # Edita un contacto creado dentro de la carpeta
    def editContact(self):
        print('Escribe los datos del contacto a editar')
        self.__saveDatArchive('edit')


    # Muestra todos los contactos que hay en la carpeta, y abre solo archivos con extensión .txt
    def showContacts(self): self.archive.showDirectorys()


    # Busca un contacto por su nombre o número
    def seekContact(self):
        nameArchive, exist, name = self.__existContact('Dígite el nombre o número del contacto a buscar:\r\n')
        if exist:
            contact = self.archive.getArchive(nameArchive)
            print('\r\n Información del Contacto: \r\n')
            for line in contact:
                if len(line) > 1:
                    print(f'\r {line.rstrip()}')
            print('\r\n')
        else: print('\r\n El contacto no se encuentra en la base de datos\r\n')


    # Elimina un contacto por su nombre
    def deleteContact(self):
        nameArchive, exist, name = self.__existContact('Dígite el nombre o el número del contacto a eliminar:\r\n')
        if exist:
            self.__showDeleteOption(nameArchive)
            print('\r\n Contacto eliminado correctamente!\r\n')
        else: print('\r\n El contacto a eliminar no existe\r\n')


    # Guarda los datos dependiendo del método, sea crear o editar
    def __saveDatArchive(self, method='create'):
        messageMethod, messageTag, messagePhone, messageCategory, option = self.__validateInputMethod(method)
        if option != 0:
            nameArchive, exist, name = self.__existContact(messageMethod)
            if (not exist and method == 'create') or (exist and method == 'edit'):
                if method == 'edit': self.__showEditOption(nameArchive)
                if option == 1 and method == 'create':
                    questionPhone = 0
                    listPhone = []
                    while (questionPhone <= 1):
                        tag = Console.read(f'Dígite {messageTag} del número: \r\n', "")
                        phoneContact = self.__addPhone(messagePhone)
                        questionPhone = 0
                        while (questionPhone < 1 or questionPhone > 2):
                            messageQuestion = '¿Desea agregar otro número?\n1. Si\n2. No\n'
                            questionPhone = input(messageQuestion)
                            questionPhone = Console.validateQuestions(questionPhone)
                        phone = Phone(tag, phoneContact)
                        listPhone.append(phone)
                    category = Console.read(f'Dígite {messageCategory} del contacto: \r\n', "")
                    self.__createContactInArchive(name, category, listPhone, nameArchive)
                    print(f'\r\n Contacto creado correctamente!\r\n')
            elif (exist and method == 'create'): print('\r\n El contacto ya existe para crearlo\r\n')
            elif (not exist and method == 'edit'): print('\r\n El contacto para editar no existe \r\n')


    def __showEditOption(self, nameArchive):
        title = "Menu Editar Contacto"
        options = [
            'Desea editar el nombre', 
            'Desea editar una etiqueta',
            'Desea editar una categoria', 
            'Desea editar un número', 
            'Desea agregar un nuevo número'
        ]
        MenuEdit(title, options, self.__editData, nameArchive)


    def __editData(self, nameArchive, optionProperty):
        contact, option, counter = self.__showDataAvalaible(nameArchive, optionProperty)
        match optionProperty:
            case "name":
                nameContact = input(f"Digite el nuevo nombre del contacto \"{contact.getName()}\" (si quiere dejar el mismo solo de enter): \n")
                if nameContact.strip() != "":
                    contact.setName(nameContact)
                    nameArchiveOld = nameArchive
                    nameArchive = self.archive.getNameArchive(nameContact.strip())
                    self.archive.renameArchive(nameArchiveOld, nameArchive)

            case "tag":
                tagContact = input(f"Digite la nueva etiqueta, la anterior es {contact.getPhones()[option - 1].getTag()} (si quiere dejar la etiqueta por defecto, debe dar enter):\n")
                if tagContact.strip() != "": contact.getPhones()[option - 1].setTag(tagContact)

            case "category":
                categoryContact = input(f"Digite la nueva categoria, la anterior es \"{contact.getCategory()}\" (si quiere dejar el por defecto de enter): \n")
                contact.setCategory(contact.getCategory() if categoryContact.strip() == "" else categoryContact)

            case "number":
                numberEdit = self.__addPhone('el nuevo teléfono')
                contact.getPhones()[option - 1].setNumber(numberEdit)

            case "phone":
                newTag = Console.read('Digite la nueva etiqueta para el nuevo numero: \n', "")
                newPhone = self.__addPhone('el nuevo teléfono')
                newPhoneContact = Phone(newTag, newPhone)
                contact.getPhones().append(newPhoneContact)

        self.__writeInArchive(nameArchive, contact)
        if (contact.getName() != nameArchive): self.archive.renameArchive(nameArchive, self.archive.getNameArchive(contact.getName()))
        print(f'\r\n Contacto editado correctamente!\r\n')


    def __showDataAvalaible(self, nameArchive, nameProperty, method="edit"):
        contact = Contact()
        listContact = []
        propertys = {
            "number": "Los números",
            "tag": "Las etiquetas",
            "edit": "editar", 
            "delete": "eliminar",
        }
        option = 0
        method = propertys[method]
        archive = 0
        counter = 0
        counterPhone = 1
        while option < 1 or option > counter:
            option = 0
            counter = 0
            archive = self.archive.getArchive(nameArchive)
            if not nameProperty in ("name", "category", "phone"):
                nameMessages = propertys[nameProperty]
                print(f'{nameMessages} a {method} son: ')
            for line in archive:
                line = line.rstrip().split(':')
                if len(line) > 1:
                    data = line[1].strip()
                    listContact.append(data)
                    if data.isnumeric() and nameProperty == "number":
                        print(f'{counter + 1}) {data}')
                        counter += 1
                    elif nameProperty == "tag" and line[0].count("Etiqueta") > 0:
                        print(f'{counter + 1} {data}')
                        counter += 1
                    elif data.isnumeric() and nameProperty == "phone":
                        counter += 1
                        counterPhone = 0
            if counter == 0 or counterPhone == 0:
                break
            option = input('Elija una opción: ')
            option = Console.validateQuestions(option)
        archive.close()
        if len(listContact) > 0:
            contact = Contact(listContact[0], listContact[-1])
            for index, item in enumerate(listContact):
                if item.isnumeric():
                    contact.setPhones(Phone(listContact[index - 1], item))
        return contact, option, counter


    # Válida que el número se escriba correctamente
    def __addPhone(self, messagePhone):
        phoneContact = ''
        while not phoneContact.isdigit() or len(phoneContact) < 10:
            if phoneContact == '': phoneContact = input(f'Dígite {messagePhone} del contacto: \r\n')
            elif (len(phoneContact) < 10): phoneContact = input(f'Dígite {messagePhone} del contacto correctamente (No se permite menos de 10 digitos): \r\n')
            else: phoneContact = input(f'Dígite {messagePhone} del contacto correctamente\n(No se pemite letras): \r\n')
            phoneContact = phoneContact.strip()
        return phoneContact


    def __createContactInArchive(self, name, category, listPhone, nameArchive):
        contact = Contact(name, category)
        for phone in listPhone: contact.setPhones(phone)
        self.__writeInArchive(nameArchive, contact)


    def __writeInArchive(self, nameArchive, contact):
        archive = self.archive.getArchive(nameArchive, 'w')
        archive.write('Nombre: '+contact.getName()+'\r\n')
        for i, phone in enumerate(contact.getPhones(), 1):
            archive.write(f'Etiqueta del telefono {i}: '+phone.getTag()+'\r\n')
            archive.write(f'Telefono {i}: '+phone.getNumber()+'\r\n')
        archive.write('Categoria: '+contact.getCategory()+'\r\n')
        archive.close()


    def __validateInputMethod(self, method):
        option = 1
        if method == 'create':
            messageMethod = 'Dígite el nombre del contacto nuevo: \r\n'
            messageTag = 'la etiqueta'
            messagePhone = 'el teléfono'
            messageCategory = 'la categoría'
        elif method == 'edit':
            messageMethod = 'Dígite el nombre o el número del contacto que desea editar: \r\n'
            messageTag = 'la nueva etiqueta'
            messagePhone = 'el nuevo teléfono'
            messageCategory = 'la nueva categoría'
        else:
            print('No existe el metodo, por favor revise la ruta')
            option = 0
        return messageMethod, messageTag, messagePhone, messageCategory, option


    def __existContact(self, messageInput):
        name = input(messageInput)
        nameArchive = self.__validateContent(name.strip())
        exist = self.archive.existArchive(nameArchive)
        return nameArchive, exist, name


    def __showDeleteOption(self, nameArchive):
        option = 0
        while option < 1 or option > 2:
            option = self.__showMenuDelete()
            option = Console.validateQuestions(option)
        self.__questionDelete(nameArchive, option)


    def __showMenuDelete(self):
        print('1. Desea eliminar todo el contacto')
        print('2. Desea eliminar un número')
        option = input('Elija una opción: ')
        return option.strip()


    def __questionDelete(self, nameArchive, option):
        if option == 1: self.archive.deleteArchive(nameArchive)
        else: self.__deleteNumber(nameArchive)


    def __deleteNumber(self, nameArchive):
        contact, option, counter = self.__showDataAvalaible(nameArchive, 'number', 'delete')
        if counter < 2: self.archive.deleteArchive(nameArchive)
        else:
            contact.getPhones().pop(option - 1)
            self.__writeInArchive(nameArchive, contact)


    # Válida el nombre del contacto y agrega directorio preestablecido
    def __validateContent(self, content):
        if content.isdigit(): nameArchive = self.archive.searchContent(content)
        else: nameArchive = self.archive.getNameArchive(content)
        return nameArchive

