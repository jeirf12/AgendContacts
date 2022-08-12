#válida cadenas numericas
def validateQuestions(value):
    value = value.strip()
    return int(value) if value.isdigit() else 0
