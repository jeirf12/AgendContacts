#Importa del modulo contacto todos los metodos
from contact import *

#Importa del modulo archivo todos los metodos
from archive import *

#Guarda los datos dependiendo del metodo, sea crear o editar 
def saveDatArchive(metod = 'create'):
    if metod == 'create':
        messageMetod = 'Dígite el nombre del contacto: \r\n'
        messagePhone = 'el telefono'
        messageCategory = 'la categoria'
    elif metod == 'edit':
        messageMetod = 'Nombre del contacto que desea editar: \r\n'
        messagePhone = 'el nuevo telefono'
        messageCategory = 'la nueva categoria'
    else:
        print('No existe el metodo, por favor revise la ruta')
        return 0

    name = input(messageMetod)

    #crea el contacto con directorio preestablecido
    nameArchive = getNameArchive(name)

    #valida si existe un contacto
    exist = existArchive(nameArchive)
    if (not exist and metod == 'create') or (exist and metod == 'edit'):
        if metod == 'edit':
            name = input('Dígite el nuevo nombre del contacto: \r\n')
            #crea el nuevo nombre del contacto con directorio preestablecido
            nameArchiveNew = getNameArchive(name)
        phoneContact = ''
        while(not phoneContact.isdigit() or len(phoneContact)<10):
            if phoneContact == '':
                phoneContact = input(f'Dígite {messagePhone} del contacto: \r\n')
            elif(len(phoneContact)<10):
                phoneContact = input(f'Dígite {messagePhone} del contacto correctamente (No se permite menos de 10 digitos): \r\n')
            else:
                phoneContact = input(f'Dígite {messagePhone} del contacto correctamente\n(No se pemite letras): \r\n')

        category = input(f'Dígite {messageCategory} del contacto: \r\n')

        contact = Contact(name, phoneContact, category)

        #obtiene el archivo con el nombre de la carpeta y el archivo con su extension 
        archive = getArchive(nameArchive,'w')

        #Crea un contacto
        contact = Contact(name, phoneContact, category)

        #Escribe en el archivo
        archive.write('Nombre: '+contact.getName()+'\r\n')
        archive.write('Telefono: '+contact.getPhone()+'\r\n')
        archive.write('Categoria: '+contact.getCategory()+'\r\n')

        #Cierra el archivo
        archive.close()

        if metod == 'create':
            print('\r\n Contacto creado correctamente\r\n ')
        elif metod == 'edit':
            #renombra el nuevo archivo con el anterior (si cambia el nombre del contacto)
            renameArchive(nameArchive, nameArchiveNew)
            print('\r\n Contacto editado correctamente!\r\n')

    elif (exist and metod == 'create'):
        print('\r\n El contacto ya existe para crearlo\r\n')
    elif (not exist and metod == 'edit'):
        print('\r\n El contacto para editar no existe \r\n')

#Crea un contacto en la carpeta con su respectiva información
def createContact():
    print('Escribe los datos para agregar el nuevo contacto')
    saveDatArchive()

#Edita un contacto creado dentro de la carpeta
def editContact():
    print('Escribe los datos del contacto a editar')
    saveDatArchive('edit')

#Muestra todos los contactos que hay en la carpeta, y abre solo archivos con extension .txt 
def showContacts():
   showDirectorys()
#Busca un contacto por su nombre
def seekContact():
    nameSearch = input('Dígite el nombre del contacto a buscar:\r\n')

    #crea el nombre del contacto con directorio preestablecido
    nameArchive = getNameArchive(nameSearch)

    exist = existArchive(nameArchive)

    if exist:
        contact = getArchive(nameArchive)
        print('\r\n Información del Contacto: \r\n')
        for line in contact:
            print(line.rstrip())
        print('\r\n')
    else:
        print('\r\n El contacto no se encuentra en la base de datos\r\n')

#Elimina un contacto por su nombre
def deleteContact():
    nameDelete = input('Dígite el nombre del contacto a eliminar:\r\n')

    #crea el nombre del contacto con directorio preestablecido
    nameArchive = getNameArchive(nameDelete)

    exist = existArchive(nameArchive)

    if exist:
        deleteArchive(nameArchive)
        print('\r\n Contacto eliminado correctamente!\r\n')
    else:
        print('\r\n El contacto a eliminar no existe\r\n')

