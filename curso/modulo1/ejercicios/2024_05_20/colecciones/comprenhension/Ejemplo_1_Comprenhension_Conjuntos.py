impares = { numero for numero in range(1, 100, 2)}
print(impares)

lista = [1,12,1,1,1,1,2,2,3,3,3,2,3,3,2,2,2,4,4,5,5,5,4,4]
valores = {b for b in lista}
print(valores)

valores = set(lista)
print(valores)
