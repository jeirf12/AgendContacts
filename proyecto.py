#libreria para el manejo de archivos
import os

#constante para la creacion de una carpeta
FOLDER = 'contacts/'

#Constante para la extension de los archivos
EXTENSION = '.txt'

class Contact:
    
    def __init__(self, name, phone,category):
        self.name = name
        self.phone = phone
        self.category = category 

def app():
    
    #Revisa si la carpeta existe o no
    createDirectory()
    option = 0
    while option !=6:
        
        #Muestra el menu de opciones
        showMenu()

        #Pregunta al usuario la accion a realizar
        option = questionUsers()    

def questionUsers():
    option = input('Selecione una opcion: \r\n')
    option = int(option)
    #Ejecutar las opciones
    if option == 1:
        createContact()
    elif option == 2:
        editContact()
    elif option == 3:
        showContacts()
    elif option == 4:
        seekContact()
    elif option == 5:
        deleteContact()
    elif option == 6:
        print('Gracias por utilizar el programa!')
    else:
        print('Opción no válida, intente de nuevo')
    return option

def existContact(name):
    return os.path.isfile(name)

def getNameArchive(name):
    return FOLDER + name + EXTENSION

def getArchive(nameArchive, form = 'r'):
    return open(nameArchive, form)

def createContact():
    print('Escribe los datos para agregar el nuevo contacto') 
    
    name = input('Dígite el nombre del contacto: \r\n')

    #obtiene el nombre del archivo con su extension y su ruta
    nameArchive = getNameArchive(name)
    
    #valida si existe un contacto
    existe = existContact(nameArchive)
    if not existe:
        phoneContact = input('Dígite el numero del telefono: \r\n')
        category = input('Dígite la categoria del contacto: \r\n')

        #obtiene el archivo con el nombre de la carpeta y el archivo con su extension 
        archive = getArchive(nameArchive,'w')
        
        #Crea un contacto
        contact = Contact(name, phoneContact, category)

        archive.write('Nombre: '+contact.name+'\r\n')
        archive.write('Telefono: '+contact.phone+'\r\n')
        archive.write('Categoria: '+contact.category+'\r\n')
        
        archive.close()

        print('\r\n Contacto creado correctamente\r\n ')
    else:
        print('Ese contacto ya existe')

def editContact():
    print('Escribe el nombre del contacto a editar')
    namePrevious = input('Nombre del contacto que desea editar: \r\n')

    #obtiene el nombre del archivo con su extension y su ruta
    nameArchivePrevious = getNameArchive(namePrevious)
    
    #valida si existe un contacto
    exist = existContact(nameArchivePrevious)
    if exist:
        nameNew = input('Dígite el nuevo nombre del contacto: \r\n')
        phoneNew = input('Dígite el nuevo telefono del contacto: \r\n')
        categoryNew = input('Dígite la nueva categoria del contacto: \r\n')
        
        #crea un contacto
        contact = Contact(nameNew, phoneNew, categoryNew)
        
        #Obtiene un archivo
        archive = getArchive(nameArchivePrevious, 'w')

        archive.write('Nombre: '+contact.name+'\r\n')
        archive.write('Telefono: '+contact.phone+'\r\n')
        archive.write('Categoria: '+contact.category+'\r\n')
        
        archive.close()

        #crea un nueva ruta con el nombre nuevo del contacto
        nameArchiveNew = getNameArchive(nameNew)
        
        #renombra el nuevo archivo con el anterior
        os.rename(nameArchivePrevious, nameArchiveNew)

        print('\r\n Contacto editado correctamente!\r\n')

    else:
        print('el contacto no existe')

def showContacts():
    #Obtiene los archivos dentro de un directorio
    archiveList = os.listdir(FOLDER)

    #Valida que la extension del archivo sea .txt
    archiveTxt = [i for i in archiveList if i.endswith(EXTENSION)]

    for archive in archiveTxt:
        contact = getArchive(FOLDER + archive)
        for line in contact:
            #imprime los contenidos
            print(line.rstrip())
        #Imprime un separador de contactos
        print('\r\n')

def seekContact():
    nameSearch = input('Dígite el nombre del contacto a buscar:\r\n')

    nameArchive = getNameArchive(nameSearch)
    
    exist = existContact(nameArchive)

    if exist:
        contact = getArchive(nameArchive)
        print('\r\n Información del Contacto: \r\n')
        for line in contact:
            print(line.rstrip())
        print('\r\n')
    else:
        print('El contacto no se encuentra en la base de datos')

def deleteContact():
    nameDelete = input('Dígite el nombre del contacto a eliminar:\r\n')
    
    nameArchive = getNameArchive(nameDelete)

    exist = existContact(nameArchive)
    
    if exist:
        os.remove(nameArchive)
        print('Contacto eliminado correctamente!')
    else:
        print('El contacto a eliminar no existe')

def showMenu():
    print('Seleccione del Menu lo que desea hacer:')
    print('1) Agregar Nuevo Contacto')
    print('2) Editar Contacto')
    print('3) ver Contactos')
    print('4) Buscar Contacto')
    print('5) Eliminar Contacto')
    print('6) Salir')

def createDirectory():
    if not os.path.exists(FOLDER):
        #crear la carpeta
        os.makedirs(FOLDER)

#main principal o ejecutor de la aplicación
app()
