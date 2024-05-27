# dado el dataset, utilizar los siguientes archivos: 'nombres.data' y 'apellidos.data'
# definir una función que recibe dos parametros de entrada indicando el número de nombres
# masculinos y el número de nombres femeninos

# Devolver una lista con los nombres generados


import curso.api.Ficheros as Files
import random


def personas(hombres, mujeres):
    nombres = Files.list_file_text('C:\\Users\\34676\\Documents\\Code\\Python\\Course\\curso\\data\\nombres.data')[1:]
    # print(nombres)
    nombres_masculinos = [nombre.split(';')[0] for nombre in nombres if nombre.strip().endswith('h')]
    nombres_femeninos = [nombre.split(';')[0] for nombre in nombres if nombre.strip().endswith('m')]

    apellidos = Files.list_file_text('C:\\Users\\34676\\Documents\\Code\\Python\\Course\\curso\\data\\apellidos.data')[1:]
    # print(apellidos)
    personas = []
    for n in range(mujeres):
        aleatorio = random.randint(0,len(apellidos)-1)
        apellido1 = apellidos[aleatorio]
        aleatorio = random.randint(0,len(apellidos)-1)
        apellido2 = apellidos[aleatorio]
        aleatorio = random.randint(0, len(nombres_femeninos)-1)
        nombre = nombres_femeninos[aleatorio]
        personas.append(nombre+' '+apellido1.strip()+' '+apellido2.strip())

    for n in range(hombres):
        aleatorio = random.randint(0,len(apellidos)-1)
        apellido1 = apellidos[aleatorio]
        aleatorio = random.randint(0,len(apellidos)-1)
        apellido2 = apellidos[aleatorio]
        aleatorio = random.randint(0, len(nombres_masculinos)-1)
        nombre = nombres_masculinos[aleatorio]
        personas.append(nombre+' '+apellido1.strip()+' '+apellido2.strip())
    random.shuffle(personas)
    return personas


nombres = personas(5,5)
print(nombres)