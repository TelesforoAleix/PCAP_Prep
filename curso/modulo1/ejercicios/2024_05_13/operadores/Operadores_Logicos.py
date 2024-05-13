rdo = 3 > 4
bool2 = 5 <= 6 == 6 < 9
#print(bool2)
# Utilizando el operador OR

bool3 = 5 == 6 or 6 != 6 or 7 != 8
#print(bool3)

bool4 = 5 <= 6 and 6 == 6 and 7 < 8
#print(bool4)

bool5 = (5 <= 6 or 6 < 9) and 8 > 10
print(bool5)

print("not =>", not 5 <= 6)
print("not =>", not False)

n = 1000
if n > 100 and n < 2000:
    print('Se cumple')
else:
    print('No se cumple')

if n < 10 or n > 1000:
    print('Se cumple')
else:
    print('No se cumple')

