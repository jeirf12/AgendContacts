#Libreria para el manejo de archivos
import os

#Constante para la creacion de una carpeta
FOLDER = 'contacts/'

#Constante para la extension de los archivos
EXTENSION = '.txt'

#Clase contacto que sirve como api y darle formato a los datos
class Contact:
    
    #Constructor parametrizado
    def __init__(self, name, phone,category):
        self.__name = name
        self.__phone = phone
        self.__category = category 
    
    #Getter and Setter de cada atributo
    def setName(self, name):
        self.__name = name

    def setPhone(self, phone):
        self.__phone = phone

    def setCategory(self, category):
        self.__category = category

    def getName(self):
        return self.__name

    def getPhone(self):
        return self.__phone

    def getCategory(self):
        return self.__category

#Main principal - implementacion
def app():
    
    #Revisa si la carpeta existe o no
    createDirectory()
    
    option = 0
    while option !=6:
        
        #Muestra el menu de opciones
        showMenu()

        #Pregunta al usuario la accion a realizar
        option = questionUsers()    

#Implementacion donde se decide la accion a realizar
def questionUsers():
    option = input('Selecione una opcion: \r\n')
    if option.isdigit():
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
            print('\r\n Opción no válida, intente de nuevo\r\n')
    else:
        print('\r\n Por favor dígite numeros\r\n')
        option = 0

    return option

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

    #obtiene el nombre del archivo con su extension y su ruta
    nameArchive = getNameArchive(name)
    
    
    #valida si existe un contacto
    exist = existContact(nameArchive)
    if (not exist and metod == 'create') or (exist and metod == 'edit'):
        if metod == 'edit': 
            name = input('Dígite el nuevo nombre del contacto: \r\n')
            #obtiene el nombre del archivo con su extension y su ruta
            nameArchiveNew = getNameArchive(name)
        phoneContact = ''
        while(not phoneContact.isdigit()):
            if phoneContact == '':
                phoneContact = input(f'Dígite {messagePhone} del contacto: \r\n')
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
            #renombra el nuevo archivo con el anterior
            os.rename(nameArchive, nameArchiveNew)
            
            print('\r\n Contacto editado correctamente!\r\n')

    elif (exist and metod == 'create'):
        print('\r\n El contacto ya existe para crearlo\r\n')
    elif (not exist and metod == 'edit'):
        print('\r\n El contacto para editar no existe \r\n')

#Metodo que valida si el contacto existe en los archivos
def existContact(name):
    return os.path.isfile(name)

#Metodo que arma el archivo con su respectiva ruta y extension (en este caso txt)
def getNameArchive(name):
    return FOLDER + name + EXTENSION

#Metodo que obtiene un objeto de tipo archivo abierto para su escritura 
#o por defecto (lectura) si no manda parametro de acción
def getArchive(nameArchive, action = 'r'):
    return open(nameArchive, action)

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
    #Obtiene los archivos dentro de un directorio
    archiveList = os.listdir(FOLDER)

    #Valida que la extension del archivo sea .txt
    archiveTxt = [i for i in archiveList if i.endswith(EXTENSION)]
    size = len(archiveTxt)
    if size > 0:
        for archive in archiveTxt:
            contact = getArchive(FOLDER + archive)
            for line in contact:
                #imprime los contenidos
                print(line.rstrip())
            #Imprime un separador de contactos
            print('\r\n')
    else:
        print('\r\n No hay contactos para mostrar\r\n')
#Busca un contacto por su nombre
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
        print('\r\n El contacto no se encuentra en la base de datos\r\n')

#Elimina un contacto por su nombre
def deleteContact():
    nameDelete = input('Dígite el nombre del contacto a eliminar:\r\n')
    
    nameArchive = getNameArchive(nameDelete)

    exist = existContact(nameArchive)
    
    if exist:
        os.remove(nameArchive)
        print('\r\n Contacto eliminado correctamente!\r\n')
    else:
        print('\r\n El contacto a eliminar no existe\r\n')

#Muestra el menu para mostrar al usuario por consola
def showMenu():
    print('Seleccione del Menu lo que desea hacer:')
    print('1) Agregar Nuevo Contacto')
    print('2) Editar Contacto')
    print('3) ver Contactos')
    print('4) Buscar Contacto')
    print('5) Eliminar Contacto')
    print('6) Salir')

#Crea un directorio o carpeta para guardar los contactos(si ya existe, no la crea)
def createDirectory():
    #Valida si la carpeta ya ha sido creada
    if not os.path.exists(FOLDER):
        #crear la carpeta
        os.makedirs(FOLDER)

#main principal o ejecutor de la aplicación
app()
