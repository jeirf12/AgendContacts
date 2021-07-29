#Librería para el manejo de archivos y el sistema operativo en general
import os

#Constante para la creación de una carpeta
FOLDER = 'contacts/'

#Constante para la extensión de los archivos
EXTENSION = '.txt'

#Crea un directorio o carpeta para guardar los contactos(si ya existe, no la crea)
def create():
    #Valida si la carpeta ya ha sido creada
    if not os.path.exists(FOLDER):
        #crear la carpeta
        os.makedirs(FOLDER)

#Método que obtiene un objeto de tipo archivo abierto para su escritura 
#o por defecto (lectura) si no manda parametro de acción
def getArchive(nameArchive, action = 'r'):
    return open(nameArchive, action)

#Método que válida si el contacto existe en los archivos
def existArchive(nameArchive):
    #obtiene el nombre del archivo con su extensión y su ruta
    return os.path.isfile(nameArchive)

#Método que arma el archivo con su respectiva ruta y extensión (en este caso txt)
def getNameArchive(name):
    return FOLDER + name + EXTENSION

#Método para renombrar un archivo existente
def renameArchive(namePrevious, nameNew):
    os.rename(namePrevious, nameNew)

#Método para eliminar un archivo existente:
def deleteArchive(nameDelete):
    os.remove(nameDelete)

#Método para obtener los archivos que contiene una carpeta
def getFiles():
    return os.listdir(FOLDER)

#Método para buscar dentro de un archivo
def searchContent(content):
    listFiles = getFiles()
    files = [i for i in listFiles if i.endswith(EXTENSION)]
    size = len(files)
    if size > 0:
        for file in files:
            nameFile = FOLDER + file
            contact = getArchive(nameFile)
            for line in contact:
                if line.find(content) != -1:
                    return nameFile
    return ''

#Método para mostrar lo que contiene un directorio(abre sus archivos contenidos)
def showDirectorys():
    #Obtiene los archivos dentro de un directorio
    archiveList = getFiles()
    #Válida que la extensión del archivo sea .txt
    archiveTxt = [i for i in archiveList if i.endswith(EXTENSION)]
    size = len(archiveTxt)
    if size > 0:
        print('\r\n Información de los contactos \r\n')
        for archive in archiveTxt:
            contact = getArchive(FOLDER + archive)
            for line in contact:
                if len(line) > 1:
                    #imprime los contenidos
                    print(f'\r {line.rstrip()}')
            #Imprime un separador de contactos
            print('\r\n')
    else:
        print('\r\n No hay contactos para mostrar\r\n')
