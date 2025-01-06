#Librería para el manejo de archivos y el sistema operativo en general
import os


# Librería para el manejo de la consola como proxy
from console import Console


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


    #Método que válida si el contacto existe en los archivos 
    #obtiene el nombre del archivo con su extensión y su ruta
    def existArchive(self, nameArchive): return os.path.isfile(nameArchive)


    #Método que construye el nombre del archivo con su respectiva ruta y extensión (en este caso txt)
    def getNameArchive(self, name): return self.__folder + name + self.__extension


    #Método para renombrar un archivo existente
    def renameArchive(self, namePrevious, nameNew): os.rename(namePrevious, nameNew)


    #Método para eliminar un archivo existente:
    def deleteArchive(self, nameDelete): os.remove(nameDelete)


    #Método para buscar dentro de un archivo
    def searchContent(self, content):
        files = self.getFiles()
        fileFound = next(filter(lambda file: any(content in line for line in self.__getArchive(file)), files), '')
        return fileFound


    def searchContentAllFiles(self, content):
        files = self.getFiles()
        filesFound = list(filter(lambda file: any(content in line for line in self.__getArchive(file)), files))
        return filesFound


    #Método para obtener los archivos que contiene una carpeta y filtrados por la extension
    def getFiles(self):
        listFiles = os.listdir(self.__folder)
        files = [self.__folder + file for file in listFiles if file.endswith(self.__extension)]
        return files


    def showFile(self, nameFile):
        with self.__getArchive(nameFile) as file:
            for line in file:
                if len(line) > 1:
                    Console.writeJumpLine(f'\r {line.rstrip()}')
            Console.writeJumpLine('\r\n')


    def writeFile(self, nameFile, content):
        with self.__getArchive(nameFile, 'w') as file:
            file.write(content)


    def getContentFile(self, nameFile):
        contents = []
        with self.__getArchive(nameFile) as file:
            contents = [
                line.rstrip().split(':')[1].strip()
                for line in file
                if ':' in line and len(line.rstrip().split(':')) == 2
            ]
        return contents


    #Método que obtiene un objeto de tipo archivo abierto para su escritura 
    #o por defecto (lectura) si no manda parámetro de acción
    def __getArchive(self, nameArchive, action = 'r'): return open(nameArchive, action)


