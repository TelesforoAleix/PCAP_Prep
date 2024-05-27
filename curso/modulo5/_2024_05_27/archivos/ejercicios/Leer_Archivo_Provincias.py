# Dado el dataset, abrir el archivo 'provincias.data', leer contenido
# y mostrar unicamente el nombre de la provincia

import curso.api.Ficheros as File

datos = File.list_file_text('C:\\Users\\34676\\Documents\\Code\\Python\\Course\\curso\\data\\provincias.data')[1:]
for provincia in datos:
    print(provincia.split(';')[1])