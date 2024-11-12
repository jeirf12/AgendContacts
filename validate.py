import importlib.util

def exists_module_getch():
    valid = importlib.util.find_spec('getch')
    if not valid:
        print("Debe instalar py-getch con el siguiente comando:\n\n\tpython -m pip install py-getch")
        return False

    return valid


