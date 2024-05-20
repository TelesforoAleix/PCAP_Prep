# definir una función que devuelva una cadena de texto rellenada
# por la izquierda con un determinado caracter

def pad_left(text, width, character='0'):
    if len(text) > width:
        return text
    return (character * (width - len(text))) + text


s = pad_left('something', 32, 'x')
print(s)

def pad2_left(text, width, character='0'):
    return (character * (width - len(text))) + text if len(text) > width else text

