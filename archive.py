#Librería para el manejo de archivos y el sistema operativo en general
import os


# Clase que formatea y obtiene información de archivos
class Archive():
    def __init__(self):
        #Constante para la creación de una carpeta
        self.__folder = "contacts/"
        #Constante para la extensión de los archivos
        self.__extension = ".txt"


    #Crea un directorio o carpeta para guardar los contactos(si ya existe, no la crea)
    def create(self):
        if not os.path.exists(self.__folder): os.makedirs(self.__folder)


    #Método que obtiene un objeto de tipo archivo abierto para su escritura 
    #o por defecto (lectura) si no manda parámetro de acción
    def getArchive(self, nameArchive, action = 'r'): return open(nameArchive, action)


    #Método que válida si el contacto existe en los archivos 
    #obtiene el nombre del archivo con su extensión y su ruta
    def existArchive(self, nameArchive): return os.path.isfile(nameArchive)


    #Método que construye el nombre del archivo con su respectiva ruta y extensión (en este caso txt)
    def getNameArchive(self, name): return self.__folder + name + self.__extension


    #Método para renombrar un archivo existente
    def renameArchive(self, namePrevious, nameNew): os.rename(namePrevious, nameNew)


    #Método para eliminar un archivo existente:
    def deleteArchive(self, nameDelete): os.remove(nameDelete)


    #Método para obtener los archivos que contiene una carpeta y filtrados por la extension
    def getFiles(self):
        listFiles = os.listdir(self.__folder)
        files = [file for file in listFiles if file.endswith(self.__extension)]
        return files


    #Método para buscar dentro de un archivo
    def searchContent(self, content):
        files = self.getFiles()
        size = len(files)
        if size > 0:
            for file in files:
                nameFile = self.__folder + file
                contact = self.getArchive(nameFile)
                for line in contact:
                    if line.find(content) != -1:
                        return nameFile
        return ''


    #Método para mostrar lo que contiene un directorio(abre sus archivos contenidos)
    def showDirectorys(self):
        files = self.getFiles()
        size = len(files)
        if size > 0:
            print('\r\n Información de los contactos \r\n')
            for archive in files:
                contact = self.getArchive(self.__folder + archive)
                for line in contact:
                    if len(line) > 1:
                        #imprime los contenidos
                        print(f'\r {line.rstrip()}')
                #Imprime un separador de contactos
                print('\r\n')
        else:
            print('\r\n No hay contactos para mostrar\r\n')

