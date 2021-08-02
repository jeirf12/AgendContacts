#Importa del módulo contacto todos los métodos
from model import *

#Importa módulos que no tiene nada que ver con el modelo
from utilities import validateQuestions

#Importa del módulo archivo todos los métodos
from archive import *

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
                option = showEditOption(nameArchive)
                nameArchiveNew = nameArchive
            if option == 1:
                if method == 'edit':
                    name = input('Dígite el nuevo nombre del contacto: \r\n')
                    #crea el nuevo nombre del contacto con directorio preestablecido
                    nameArchiveNew = getNameArchive(name)
                questionPhone = 0
                listPhone = []
                while(questionPhone <= 1):
                    tag = input(f'Dígite {messageTag} del número: \r\n')
                    phoneContact = addPhone(messagePhone)
                    questionPhone = 0
                    while (questionPhone < 1 or questionPhone > 2):
                        messageQuestion = '¿Desea agregar otro número?\n1. Si\n2. No\n'
                        questionPhone = input(messageQuestion)
                        questionPhone = validateQuestions(questionPhone)
                    phone = Phone(tag, phoneContact)
                    listPhone.append(phone)
                category = input(f'Dígite {messageCategory} del contacto: \r\n')
                createContactInArchive(name, category, listPhone, nameArchive)
            if method == 'create':
                nameMethod = 'creado'
            elif method == 'edit':
                #renombra el nuevo archivo con el anterior (si cambia el nombre del contacto)
                renameArchive(nameArchive, nameArchiveNew)
                nameMethod = 'editado'
            print(f'\r\n Contacto {nameMethod} correctamente!\r\n')
        elif (exist and method == 'create'):
            print('\r\n El contacto ya existe para crearlo\r\n')
        elif (not exist and method == 'edit'):
            print('\r\n El contacto para editar no existe \r\n')

def showMenuEdit():
    print('1. Desea editar todo el contacto')
    print('2. Desea editar un número')
    option = input('Elija una opción: ')
    return option.strip()

def questionEdit(nameArchive, option):
    if option == 2:
        editNumber(nameArchive)

def editNumber(nameArchive):
    listContact, option, counter = showNumberAvalaible(nameArchive)
    contact = Contact()
    contact.setName(listContact[0])
    counter2 = 1
    count = 1
    while count <= counter:
        if count == option:
            phoneContact = addPhone('el nuevo teléfono')
            phone = Phone(listContact[counter2], phoneContact)
        else:
            phone = Phone(listContact[counter2], listContact[counter2 + 1])
        contact.setPhones(phone)
        count += 1
        counter2 += 2
    contact.setCategory(listContact[counter2])
    writeInArchive(nameArchive, contact)

def showEditOption(nameArchive):
    option = 0
    while option < 1 or option > 2:
        option = showMenuEdit()
        option = validateQuestions(option)
    questionEdit(nameArchive, option)
    return option

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
   showDirectorys()

#Busca un contacto por su nombre o número
def seekContact():
    nameArchive, exist, name = existContent('Dígite el nombre o número del contacto a buscar:\r\n')
    if exist:
        contact = getArchive(nameArchive)
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
        deleteArchive(nameArchive)
    else:
        deleteNumber(nameArchive)

def showNumberAvalaible(nameArchive, method="edit"):
    listContact = []
    option = 0
    if method == "edit":
        method = "editar"
    elif method == "delete":
        method = "eliminar"
    while option < 1 or option > counter:
        archive = getArchive(nameArchive)
        counter = 0
        print(f'Los números a {method} son: ')
        for line in archive:
            line = line.rstrip().split(':')
            if len(line) > 1:
                data = line[1].strip()
                listContact.append(data)
                if data.isnumeric():
                    print(f'{counter + 1}) {data}')
                    counter += 1
        option = input('Elija una opción: ')
        option = validateQuestions(option)
        archive.close()
    return listContact, option, counter

def deleteNumber(nameArchive):
    listContact, option, counter = showNumberAvalaible(nameArchive, 'delete')
    if counter < 2:
        deleteArchive(nameArchive)
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
        option = validateQuestions(option)
    questionDelete(nameArchive, option)

#Válida el nombre del contacto y agrega directorio preestablecido
def validateContent(content):
    if content.isdigit():
        nameArchive = searchContent(content)
    else:
        nameArchive = getNameArchive(content)
    return nameArchive

def createContactInArchive(name, category, listPhone, nameArchive):
    contact = Contact(name, category)
    for phone in listPhone:
        contact.setPhones(phone)
    writeInArchive(nameArchive, contact)

def writeInArchive(nameArchive, contact):
    archive = getArchive(nameArchive, 'w')
    archive.write('Nombre: '+contact.getName()+'\r\n')
    for i, phone in enumerate(contact.getPhones(), 1):
        archive.write(f'Etiqueta del telefono {i}: '+phone.getTag()+'\r\n')
        archive.write(f'Telefono {i}: '+phone.getNumber()+'\r\n')
    archive.write('Categoria: '+contact.getCategory()+'\r\n')
    archive.close()

def existContent(messageInput):
    name = input(messageInput)
    nameArchive = validateContent(name.strip())
    exist = existArchive(nameArchive)
    return nameArchive, exist, name
