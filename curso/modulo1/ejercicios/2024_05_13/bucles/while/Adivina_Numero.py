import random

# Número entre 1 y 1000
# 600
# Número entre 600 y 1000
# 900
# Número entre 600 y 900
# 700
# Número entre 700 y 900
# 800
# Has acertado, numero de intentor X

min = 1
max = 10000

aleatorio = random.randint(min, max)

intento = 0
number = 0
print('Vamos a jugar a adivinar un numero entre 1 y 10000')
while number != aleatorio:
    print('Número entre ', min, ' y ', max)
    number = int(input('Introduzca su número: '))
    intento += 1
    if number > max:
        print('The number is too big')
    else:
        if number > aleatorio:
            max = number
        elif number < aleatorio:
            min = number
else:
    print('Has acertado, número de intentos: ', intento)
