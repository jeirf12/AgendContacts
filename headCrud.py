#Importa del módulo contacto todos los métodos
from model import *

#Importa módulos que no tiene nada que ver con el modelo
from console import Console

#Importa del módulo archivo todos los métodos
from archive import Archive

Archive = Archive()

def validateInputMethod(method):
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

#Guarda los datos dependiendo del método, sea crear o editar 
def saveDatArchive(method = 'create'):
    messageMethod, messageTag, messagePhone, messageCategory, option = validateInputMethod(method)
    if option != 0:
        nameArchive, exist, name = existContent(messageMethod)
        if (not exist and method == 'create') or (exist and method == 'edit'):
            if method == 'edit':
                contact = showEditOption(nameArchive)
                nameArchiveNew = nameArchive
                if not contact.getName() == name:
                    #crea el nuevo nombre del contacto con directorio preestablecido
                    nameArchiveNew = Archive.getNameArchive(contact.getName())
            if option == 1 and method == 'create':
                questionPhone = 0
                listPhone = []
                while(questionPhone <= 1):
                    tag = input(f'Dígite {messageTag} del número: \r\n')
                    phoneContact = addPhone(messagePhone)
                    questionPhone = 0
                    while (questionPhone < 1 or questionPhone > 2):
                        messageQuestion = '¿Desea agregar otro número?\n1. Si\n2. No\n'
                        questionPhone = input(messageQuestion)
                        questionPhone = Console.validateQuestions(questionPhone)
                    phone = Phone(tag, phoneContact)
                    listPhone.append(phone)
                category = input(f'Dígite {messageCategory} del contacto: \r\n')
                createContactInArchive(name, category, listPhone, nameArchive)
            if method == 'create':
                nameMethod = 'creado'
            elif method == 'edit':
                #renombra el nuevo archivo con el anterior (si cambia el nombre del contacto)
                Archive.renameArchive(nameArchive, nameArchiveNew)
                nameMethod = 'editado'
            print(f'\r\n Contacto {nameMethod} correctamente!\r\n')
        elif (exist and method == 'create'):
            print('\r\n El contacto ya existe para crearlo\r\n')
        elif (not exist and method == 'edit'):
            print('\r\n El contacto para editar no existe \r\n')

def showMenuEdit():
    print('1. Desea editar el nombre')
    print('2. Desea editar una etiqueta')
    print('3. Desea editar una categoria')
    print('4. Desea editar un número')
    print('5. Desea agregar un nuevo número')
    option = input('Elija una opción: ')
    return option.strip()

def questionEdit(nameArchive, option):
    match option:
        case 1: return editData(nameArchive, "name")
        case 2: return editData(nameArchive, "tag")
        case 3: return editData(nameArchive, "category")
        case 4: return editData(nameArchive, "number")
        case 5: return editData(nameArchive, "phone")

def insertFullContact(listContact):
    contact = Contact(listContact[0], listContact[len(listContact) - 1])
    for index,item in enumerate(listContact):
        if item.isnumeric():
            contact.setPhones(Phone(listContact[index-1], item))
    return contact

def editData(nameArchive, optionProperty):
    listContact, option, counter = showDataAvalaible(nameArchive, optionProperty)
    contact = insertFullContact(listContact)
    counter2 = 1
    count = 1
    match optionProperty:
        case "name":
            nameContact = input(f"Digite el nuevo nombre del contacto \"{contact.getName()}\" (si quiere dejar el mismo solo de enter): ")
            contact.setName(contact.getName() if nameContact.strip() == "" else nameContact)
        case "tag":
            contact = Contact(contact.getName(), contact.getCategory())
            while count <= counter:
                if count == option:
                    tagContact = input(f"Digite la nueva etiqueta, la anterior es {listContact[counter2]} (si quiere dejar la etiqueta por defecto, debe dar enter):")
                    tagContact = listContact[counter2] if tagContact.strip() == "" else tagContact
                    phone = Phone(tagContact, listContact[counter2 + 1])
                else:
                    phone = Phone(listContact[counter2], listContact[counter2 + 1])
                contact.setPhones(phone)
                count += 1
                counter2 += 2
        case "category":
            categoryContact = input(f"Digite la nueva categoria, la anterior es \"{contact.getCategory()}\" (si quiere dejar el por defecto de enter): ")
            contact.setCategory(contact.getCategory() if categoryContact.strip() == "" else categoryContact)
        case "number":
            contact = Contact(contact.getName(), contact.getCategory())
            while count <= counter:
                if count == option:
                    phoneContact = addPhone('el nuevo teléfono')
                    phone = Phone(listContact[counter2], phoneContact)
                else:
                    phone = Phone(listContact[counter2], listContact[counter2 + 1])
                contact.setPhones(phone)
                count += 1
                counter2 += 2
        case "phone":
            contact = Contact(contact.getName(), contact.getCategory())
            newTag = input("Digite la nueva etiqueta para el nuevo numero: ")
            newContactPhone = addPhone('el nuevo teléfono')
            newPhone = Phone(newTag, newContactPhone)
            while count <= counter:
                phone = Phone(listContact[counter2], listContact[counter2 + 1])
                contact.setPhones(phone)
                count += 1
                counter2 += 2
            contact.setPhones(newPhone)
    writeInArchive(nameArchive, contact)
    return contact

def showEditOption(nameArchive):
    option = 0
    while option < 1 or option > 5:
        option = showMenuEdit()
        option = Console.validateQuestions(option)
    return questionEdit(nameArchive, option)

#Válida que el número se escriba correctamente
def addPhone(messagePhone):
    phoneContact = ''
    while(not phoneContact.isdigit() or len(phoneContact) < 10):
        if phoneContact == '':
            phoneContact = input(f'Dígite {messagePhone} del contacto: \r\n')
        elif(len(phoneContact) < 10):
            phoneContact = input(f'Dígite {messagePhone} del contacto correctamente (No se permite menos de 10 digitos): \r\n')
        else:
            phoneContact = input(f'Dígite {messagePhone} del contacto correctamente\n(No se pemite letras): \r\n')
        phoneContact = phoneContact.strip()
    return phoneContact

#Crea un contacto en la carpeta con su respectiva información
def createContact():
    print('Escribe los datos para agregar el nuevo contacto')
    saveDatArchive()

#Edita un contacto creado dentro de la carpeta
def editContact():
    print('Escribe los datos del contacto a editar')
    saveDatArchive('edit')

#Muestra todos los contactos que hay en la carpeta, y abre solo archivos con extensión .txt 
def showContacts():
   Archive.showDirectorys()

#Busca un contacto por su nombre o número
def seekContact():
    nameArchive, exist, name = existContent('Dígite el nombre o número del contacto a buscar:\r\n')
    if exist:
        contact = Archive.getArchive(nameArchive)
        print('\r\n Información del Contacto: \r\n')
        for line in contact:
            if len(line) > 1:
                print(f'\r {line.rstrip()}')
        print('\r\n')
    else:
        print('\r\n El contacto no se encuentra en la base de datos\r\n')

#Elimina un contacto por su nombre
def deleteContact():
    nameArchive, exist, name = existContent('Dígite el nombre o el número del contacto a eliminar:\r\n')
    if exist:
        showDeleteOption(nameArchive)
        print('\r\n Contacto eliminado correctamente!\r\n')
    else:
        print('\r\n El contacto a eliminar no existe\r\n')

def showMenuDelete():
    print('1. Desea eliminar todo el contacto')
    print('2. Desea eliminar un número')
    option = input('Elija una opción: ')
    return option.strip()

def questionDelete(nameArchive, option):
    if option == 1:
        Archive.deleteArchive(nameArchive)
    else:
        deleteNumber(nameArchive)

def showDataAvalaible(nameArchive, nameProperty, method="edit"):
    listContact = []
    propertys = { "number": "Los números", "tag": "Las etiquetas", "edit": "editar", "delete": "eliminar"}
    option = 0
    method = propertys[method]
    archive = 0
    counter = 0
    counterPhone = 1
    while option < 1 or option > counter:
        option = 0
        counter = 0
        archive = Archive.getArchive(nameArchive)
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
        if counter == 0 or counterPhone == 0: break;
        option = input('Elija una opción: ')
        option = Console.validateQuestions(option)
    archive.close()
    return listContact, option, counter

def deleteNumber(nameArchive):
    listContact, option, counter = showDataAvalaible(nameArchive, 'number', 'delete')
    if counter < 2:
        Archive.deleteArchive(nameArchive)
    else:
        contact = Contact()
        contact.setName(listContact[0])
        counter2 = 1
        count = 1
        while count <= counter:
            if count != option:
                phone = Phone(listContact[counter2], listContact[counter2 + 1])
                contact.setPhones(phone)
            count += 1
            counter2 += 2
        contact.setCategory(listContact[counter2])
        writeInArchive(nameArchive, contact)

def showDeleteOption(nameArchive):
    option = 0
    while option < 1 or option > 2:
        option = showMenuDelete()
        option = Console.validateQuestions(option)
    questionDelete(nameArchive, option)

#Válida el nombre del contacto y agrega directorio preestablecido
def validateContent(content):
    if content.isdigit():
        nameArchive = Archive.searchContent(content)
    else:
        nameArchive = Archive.getNameArchive(content)
    return nameArchive

def createContactInArchive(name, category, listPhone, nameArchive):
    contact = Contact(name, category)
    for phone in listPhone:
        contact.setPhones(phone)
    writeInArchive(nameArchive, contact)

def writeInArchive(nameArchive, contact):
    archive = Archive.getArchive(nameArchive, 'w')
    archive.write('Nombre: '+contact.getName()+'\r\n')
    for i, phone in enumerate(contact.getPhones(), 1):
        archive.write(f'Etiqueta del telefono {i}: '+phone.getTag()+'\r\n')
        archive.write(f'Telefono {i}: '+phone.getNumber()+'\r\n')
    archive.write('Categoria: '+contact.getCategory()+'\r\n')
    archive.close()

def existContent(messageInput):
    name = input(messageInput)
    nameArchive = validateContent(name.strip())
    exist = Archive.existArchive(nameArchive)
    return nameArchive, exist, name
