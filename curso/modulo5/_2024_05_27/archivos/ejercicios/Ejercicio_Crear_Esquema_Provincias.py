# dado el dataset leer el arcguvi 'provincias.data', definir una función que devuelva
# una lista con el formato indicado por el esquema del archivo

import curso.api.Ficheros as File


def data_record(filename):
    records = []
    lineas = File.list_file_text(filename)
    for linea in lineas:
        datos = linea.split(';')
        data = {}
        data['id'] = int(datos[0])
        data['provincia'] = datos[1]
        data['id_ccaa'] = int(datos[2])
        records.append(data)
    return records




data = data_record('C:\\Users\\34676\\Documents\\Code\\Python\\Course\\curso\\data\\provincias.data')
for d in data:
    print(d)