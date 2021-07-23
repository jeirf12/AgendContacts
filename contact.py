#Clase contacto que sirve para darle formato a los datos
class Contact:

    #Constructor parametrizado
    def __init__(self, name, tag, phone, category):
        self.__name = name
        self.__tag = tag
        self.__phone = phone
        self.__category = category

    #Getter and Setter de cada atributo
    def setName(self, name):
        self.__name = name

    def setTag(self, tag):
        self.__tag = tag

    def setPhone(self, phone):
        self.__phone = phone

    def setCategory(self, category):
        self.__category = category

    def getName(self):
        return self.__name

    def getTag(self):
        return self.__tag

    def getPhone(self):
        return self.__phone

    def getCategory(self):
        return self.__category
