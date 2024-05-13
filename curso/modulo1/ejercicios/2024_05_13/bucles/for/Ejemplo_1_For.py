# Mostrar en pantalla los primeros 'n' números impares
n = int(input('Números '))
i = 1
for b in range(n):
    print(i)
    i += 2

# Funcionalidad de range
# esta función devuelve una serie o lista o colección de valores
# tiene 3 formatos disponibles:

# - range(8)            --> 0, 1, 2, 3, 4, 5, 6, 7
# - range(87, 93)       --> 87, 88, 89, 90, 91, 92
# - range(87, 93, 2)    --> 87, 89, 91

# - range(start, finish, interval)