# Funciones recursivas
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print('Factorial =>', factorial(6))

def factorial2(n):
    return 1 if n == 1 else n*factorial(n-1)
print('Factorial2 => ', factorial2(6))

print('-' * 80)

def fibonacci(n):
    return n if n < 2 else fibonacci(n - 1) + fibonacci(n - 2)


print("Fibonacci =>", fibonacci(22))

print('-' * 80)


def sumas(n):
    if n == 1:
        return 1
    else:
        return n + sumas(n - 1)


print('Sumas : ', sumas(5))


def ocurrencias(texto, palabra, palabras=[]):
    posicion = texto.lower().find(palabra.lower())
    if posicion == -1:
        return palabras
    else:
        word = texto[posicion:]
        word = word[:word.find(' ')] if word.find(' ') != -1 else word
        palabras.append(word)
        texto = texto[posicion + len(palabra):]
        return ocurrencias(texto, palabra, palabras)

texto = 'NUeva frase frase nuEVa Nueva'

print(ocurrencias(texto, 'nueva'))
