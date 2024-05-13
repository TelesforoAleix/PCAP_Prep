def sumatorio(*numeros):
    suma = 0
    for n in numeros:
        suma += n
    return suma

s = sumatorio(1, 2, 3, 4, 543, 5436, 234)
# - Todos los números que entremos serán sumados.
# La lista se debe escribir después de la función.

print(s)

def sum(n, b=5, *h):
    suma = 0
    for n in h:
        suma += n
    return n + b + suma

print(suma(1,2,4,5,6,7,8,5,4,23,2))
# n = 1
# b = 2
# h = 4,5,6,7,8,5,4,23,2