#def suma(a, b)


# De forma recursive
def sumatorio3(*numeros):
    return sum(numeros)


def pow2(exponente):
    return (1 << exponente) if exponente > 0 else 0


s = pow2(4)
print(s)
