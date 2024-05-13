def multiplica(a, b=2):
    return a * b

print(multiplica(2, 4))
print(multiplica(2))
# If we define one of the variables on the formula
# It should be the last parameter
# Will use the predefined in case it hasn't been passed.

def suma(a=3, b=2):
    return a + b

print(suma())               # --> 5 (2+3)
print(suma(5))              # --> 7 (5+2)
print(suma(4,5))      # --> 9 (4+5)
print(suma(b=10, a=45))     # --> 55 (45+10)

