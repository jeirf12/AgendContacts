from validate import exists_module_getch

#Main principal de la aplicacion
if __name__ == '__main__' and exists_module_getch():
    #Importa del módulo el método run
    from menu import MenuMain

    title = 'Seleccione del Menú lo que desea hacer:'
    options = ["Agregar Nuevo Contacto", "Editar Contacto", "Ver Contactos", "Buscar Contacto", "Eliminar Contacto"]

    # Agend.archive.create()
    menuconf = MenuMain(title, options)


