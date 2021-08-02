#Importa del módulo contacto todos los métodos
from model import *

#Importa módulos que no tiene nada que ver con el modelo
from utilities import validateQuestions

#Importa del módulo archivo todos los métodos
from archive import *

#Guarda los datos dependiendo del método, sea crear o editar 
def saveDatArchive(method = 'create'):
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
        return 0
    name = input(messageMethod)
    #crea el contacto con directorio preestablecido
    nameArchive = validateContent(name.strip())
    #válida si existe un contacto
    exist = existArchive(nameArchive)
    if (not exist and method == 'create') or (exist and method == 'edit'):
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
        #obtiene el archivo con el nombre de la carpeta y el archivo con su extensión 
        archive = getArchive(nameArchive,'w')
        #Crea un contacto
        contact = Contact(name, category)
        for phone in listPhone:
            #Agrega teléfonos al contacto
            contact.setPhones(phone)
        #Escribe en el archivo
        archive.write('Nombre: '+contact.getName()+'\r\n')
        for i, ph in enumerate(contact.getPhones(), 1):
            archive.write(f'Etiqueta del telefono {i}: '+ph.getTag()+'\r\n')
            archive.write(f'Telefono {i}: '+ph.getNumber()+'\r\n')
        archive.write('Categoria: '+contact.getCategory()+'\r\n')
        #Cierra el archivo
        archive.close()
        if method == 'create':
            print('\r\n Contacto creado correctamente\r\n ')
        elif method == 'edit':
            #renombra el nuevo archivo con el anterior (si cambia el nombre del contacto)
            renameArchive(nameArchive, nameArchiveNew)
            print('\r\n Contacto editado correctamente!\r\n')
    elif (exist and method == 'create'):
        print('\r\n El contacto ya existe para crearlo\r\n')
    elif (not exist and method == 'edit'):
        print('\r\n El contacto para editar no existe \r\n')

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
    nameSearch = input('Dígite el nombre o número del contacto a buscar:\r\n')
    #crea el nombre del contacto con directorio preestablecido
    nameArchive = validateContent(nameSearch.strip())
    exist = existArchive(nameArchive)
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
    nameDelete = input('Dígite el nombre o el número del contacto a eliminar:\r\n')
    #crea el nombre del contacto con directorio preestablecido
    nameArchive = validateContent(nameDelete.strip())
    exist = existArchive(nameArchive)
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

def deleteNumber(nameArchive):
    listContact = []
    option = 0
    while option < 1 or option > counter:
        archive = getArchive(nameArchive)
        counter = 0
        print('Los números a eliminar son: ')
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
    if counter < 2:
        archive.close()
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
        archive = getArchive(nameArchive, 'w')
        archive.write('Nombre: '+contact.getName()+'\r\n')
        for i, ph in enumerate(contact.getPhones(), 1):
            archive.write(f'Etiqueta del telefono {i}: '+ph.getTag()+'\r\n')
            archive.write(f'Telefono {i}: '+ph.getNumber()+'\r\n')
        archive.write('Categoria: '+contact.getCategory()+'\r\n')
        #Cierra el archivo
        archive.close()

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
