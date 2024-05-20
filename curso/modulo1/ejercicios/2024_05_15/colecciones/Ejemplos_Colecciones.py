# Tipos de colecciones en Python
# - Listas
# - Conjuntos
# - Tuplas
# - Diccionarios

# Ejemplo de lista
numeros = [2, 2, 3, 4, 5]
diferentes = [2.8, False, 'text', 4, 23, None]

vacia = []

lista = list()
lista.append(2)
lista.append('Lola')
lista.append(4.5)
print(lista, type(lista))

nums = [n for n in range(5)] # For comprension
print(nums)

una = [1, 2, 3]
dos = [4, 5, 6]
tres = una + dos
print(tres)

cuatro = una    # - Ambas apuntan al mismo objeto (colección)
cuatro.append(13)
print(una)


# Ejemplo de conjuntos
conju = {3, 4, 5, 6, 5, 6} # set()
print(conju) #{3, 4, 5, 6} // No admiten valores repetidos

# Ejemplos de Tuplas
tupla = (3, 4, 5, 6, 7, 78, 7) # tuple()
# Son valores inmutables

# Ejemplos de Diccionarios
dic = {"a":24, "b":31} # dict()


