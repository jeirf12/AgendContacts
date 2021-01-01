#Importa toda la clase donde esta el crud de contactos
from HeadCrud import *

#Menu implementado 
def run():
    
    #Revisa si la carpeta existe o no (si no existe la crea)
    create()
    
    option = 0
    while option !=6:
        
        #Muestra el menu de opciones
        showMenu()

        #Pregunta al usuario la accion a realizar
        option = questionUsers() 

#Muestra el menu para mostrar al usuario por consola
def showMenu():
    print('Seleccione del Menu lo que desea hacer:')
    print('1) Agregar Nuevo Contacto')
    print('2) Editar Contacto')
    print('3) ver Contactos')
    print('4) Buscar Contacto')
    print('5) Eliminar Contacto')
    print('6) Salir')

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

