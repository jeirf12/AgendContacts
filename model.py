#Clase contacto que sirve para darle formato a los datos
class Contact:
    #Constructor parametrizado
    def __init__(self, name, category):
        self.__name = name
        self.__phones = []
        self.__category = category

    #Getter and Setter de cada atributo
    def setName(self, name): self.__name = name

    def setPhones(self, phone): self.__phones.append(phone)

    def setCategory(self, category): self.__category = category

    def getName(self): return self.__name

    def getPhones(self): return self.__phones

    def getCategory(self): return self.__category

#Clase telefono que sirve para darle formato
class Phone:
    #Constructor parametrizado
    def __init__(self, tag, number):
        self.__tag = tag
        self.__number = number

    #Getter and Setter de cada atributo
    def setTag(self, tag): self.__tag = tag

    def setNumber(self, number): self.__number = number

    def getTag(self): return self.__tag

    def getNumber(self): return self.__number
