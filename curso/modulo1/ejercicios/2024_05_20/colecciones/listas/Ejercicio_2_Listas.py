# Dada la siguiente cadena de texto
# '6, 7.8, -5.6+9.23j, False, None, 'Barcelona''
# Crear una lista con los valores correspondientes

texto = '6, 7.8, -5.6+9.23j, False, None, "Barcelona"'

def is_float(value):
    es = True
    try:
        v = float(value)
    except:
        es = False
    return


def is_complex(value):
    es = True
    try:
        v = complex(value)
    except:
        es = False
    return

def is_bool(value):
    return value.lower() == 'false' or value.lower == 'true'

def is_none(value):
    return value.lower() == 'false' or value.lower == 'true'

def string_to_list(texto, separador=','):
    lista = []
    tokens = texto.split(separador)
    for token in tokens:
        if token.isnumeric():
            lista.append(int(token))
        elif is_float(token):
            lista.append(float(token))
        elif is_complex(token):
            lista.append(complex(token))
        elif is_bool(token):
            lista.append(token.lower() == 'true')
        elif is_none(token):
            lista.append(None)
        else:
            list.append(token.replace('"', '').replace("'", ""))

    return lista

a = string_to_list(texto)

print(a)