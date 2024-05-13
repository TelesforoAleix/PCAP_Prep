# Send 3 number and analyse which is higher and if they are equal or not

print('Introduzca 3 numeros:')
a = int(input())
b = int(input())
c = int(input())

if a == b == c:
    print('All numbers are equal')
else:
    if a == b and a != c:
        if a > c:
            print ('a and b are the biggest numbers, but equal')
        else:
            print('c is the biggest number, a and b are equal')
    elif a == c and a != b:
        if a > b:
            print ('a and c are the biggest numbers, but equal')
        else:
            print('b is the biggest number, a and c are equal')
    elif b == c and b != a:
        if b > a:
            print ('b and c are the biggest numbers, but equal')
        else:
            print('a is the biggest number, a and c are equal')
    else:
        if a > b:
            if a > c:
                print('A is the biggest number')
            else:
                pass
        else:
            if b > c:
                print('B is the biggest number')
            else:
                print('C is the biggest number')