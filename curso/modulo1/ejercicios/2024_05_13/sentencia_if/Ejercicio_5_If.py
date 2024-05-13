print('Introduzca edad')
edad = int(input())
print('Introduzca ingresos')
ingresos = int(input())
if edad > 16:
    if ingresos >= 1000:
        print('tributa')
    else:
        print('no tributa')
else:
    print('no tributa')
