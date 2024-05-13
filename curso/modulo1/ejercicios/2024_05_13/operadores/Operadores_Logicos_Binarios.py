# Operadores a nivel de bit
# |     -> or
# &     -> and
# ~     -> not
# ^     -> xor
# >>    -> desplazamiento de bits a la derecha
# <<    -> desplazamiento de bits a la izquierda

# Operador or
n1 = 14
n2 = 9
r1 = n1 | n2
print(r1)
print(bin(n1))
print(bin(n2))
print(bin(r1))

print('-' * 70)

# Operador and
n1 = 14
n2 = 9
r1 = n1 & n2
print(r1)
print(bin(n1))
print(bin(n2))
print(bin(r1))

print('-' * 70)

# Operador xor
n1 = 14
n2 = 9
r1 = n1 ^ n2
print(r1)
print(bin(n1))
print(bin(n2))
print(bin(r1))

print('-' * 70)

# Operador not o negación
n1 = 14
r1 = ~n1
print(r1)
print(bin(n1))
print(bin(r1))

print('-' * 70)

# Operador desplazamiento a la izquierda
n1 = 1
n2 = 3

r1 = n1 << n2
r2 = 2 ** 3

print(r1)
print(bin(n1))
print(bin(r1))

print('-' * 70)

# Operador desplazamiento a la derecha
n1 = 254
n2 = 3
r1 = n1 >> n2
print(r1)
print(bin(n1))
print(bin(r1))
