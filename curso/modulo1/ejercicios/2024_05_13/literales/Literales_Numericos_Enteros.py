# Tipos de literales numéricos enteros
# - En base decimal:     16
# - En base binario:     0bx1111
# - En base octal:       0o17
# - En base hexadecimal: 0xf

b = 0b1111
o = 0o17
h = 0xf

print(b)
print(h)
print(o)

a = 20
b = 71
c = 105

ab = bin(a) # Convertir a binario
ao = oct(b) # Convertir a octal
ah = hex(a) # Convertir a hexadecimal

print(ab)
print(ao)
print(ah)

# Tipos de literales de tipo caracter
# - En base ASCII:          "L"
# - En base Unicode 16-bit  "\u0394"
# - En base Unicode 32-bit  "\u00000394"

c = "\u0394"
print(type(c))
print(ord(c))

g = chr(12345)
print(g)

palabra = "mañana"
nueva = palabra.encode(encoding="utf-8")
print(nueva)

palabra = nueva.decode(encoding="utf-8")
print(palabra)
