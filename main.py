#Importa del módulo el método run
from menu import MenuMain
from headCrud import Archive

#Main principal de la aplicacion
if __name__ == '__main__':
    title = 'Seleccione del Menú lo que desea hacer:'
    options = ["Agregar Nuevo Contacto", "Editar Contacto", "Ver Contactos", "Buscar Contacto", "Eliminar Contacto"]

    Archive.create()
    menuconf = MenuMain(title, options)
