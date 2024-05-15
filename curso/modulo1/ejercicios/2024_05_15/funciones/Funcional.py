lista = [1, 2, 3, 4, 4, 5]
letras = ['a', 'b', 'c', 'd']


def foreach(coleccion, funcion):
    for g in coleccion:
        funcion(g)


def cuadrado(n):
    return n * n


foreach(letras, print)
mayusculas = map(lambda x: x.upper(), letras)
triples = map(lambda d: d * 3, lista)
print(list(mayusculas))
print(list(triples))
impares = filter(lambda m: m % 2 == 1, lista)
print(list(impares))

cuadrados = map(cuadrado, lista)
print(list(cuadrados))

from functools import reduce

rdo = reduce(lambda x, y: x + y, letras)
print(rdo)
