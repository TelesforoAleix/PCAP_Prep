# Pedir por teclado valores de dos listas
# Se introducen valores hasta que tecleemos el 0

# Valores de la primera lista, se agregan valores hasta introducir el '0'

'''

lista1 = []

n1 = int(input('Dínos un número entero: '))

while n1 != 0:
    lista1.append(n1)
    n1 = int(input('Dínos un número entero: '))


# Valores de la segunda lista, se agregan valores hasta introducir el '0'

lista2 = []

print("Let's go to the next list!")

n2 = int(input('Dínos un número entero: '))

while n2 != 0:
    lista2.append(n2)
    n2 = int(input('Dínos un número entero: '))

# Realizar la suma de los elementos y mostrar en pantalla

elementos_L1 = len(lista1)
elementos_L2 = len(lista2)

elementos_t = elementos_L1 + elementos_L2

print("La lista 1 es: ", lista1, " con el número de elementos: ", elementos_L1)
print("La lista 2 es: ", lista2, " con el número de elementos: ", elementos_L2)

print('El número total de elementos es: ', elementos_t)

# Solution
print('-' * 80)

def getLista():
    lista = list()
    x = -1
    while x != 0:
        x = int(input('Número: '))
        lista.append(x)
    return lista

def suma_listas(p,s):
    items = len(p) if len(p) < len(s) else len(s)
    rdo = []
    for x in range(items):
        rdo.append(p[x] + s[x])
    return rdo


def print_lista(a, b, c):
    sums = len(c)
    print('a   +   b  -->  c')
    for x in range(sums):
        print(a[x],'   +   ', b[x],'  -->  ',c[x])
    return

primera = getLista()
segunda = getLista()

tercera = suma_listas(primera, segunda)
print(print_lista(primera, segunda, tercera))

'''

# Solution
print('-' * 80)

def getLista():
    lista = list()
    x = -1
    while x != 0:
        x = int(input('Número: '))
        lista.append(x)
    return lista

def suma_listas(*listas):
    if len(listas) < 1:
        return []
    minimo = len(listas[0])
    for g in listas:
        if len(g) < minimo:
            minimo = len(g)
    rdo = []
    for x in range(minimo):
        suma = 0
        for num in range(len(listas)):
            suma += listas[num][x]
        rdo.append(suma)
    return rdo

r1 = [2, 3]
r2 = [1, 1]
r3 = [1, 2, 3]
r4 = suma_listas(r1, r2, r3)
print(r4)


'''
def print_lista(*listas):
    sums = len(c)
    print('a   +   b  -->  c')
    for x in range(sums):
        print(a[x],'   +   ', b[x],'  -->  ',c[x])
    return

primera = getLista()
segunda = getLista()
tercera = getLista()
cuarta = getLista()

suma = suma_listas(primera, segunda, tercera, cuarta)
print(suma)

'''