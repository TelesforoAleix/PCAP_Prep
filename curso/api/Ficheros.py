import os
import datetime as dt
def dir_files(dir):
    return [os.path.join(dir, file) for file in os.listdir(dir) if os.path.isfile(os.path.join(dir, file))]


def dir_files_tree(dir):
    lista = []
    for (d, subdir, files) in os.walk(dir):
        for file in files:
            lista.append(os.path.join(d, file))
    return lista


def dir_dir(dir):
    return [os.path.join(dir, file) for file in os.listdir(dir) if os.path.isdir(os.path.join(dir, file))]

def dir_dirs_tree(dir):
    lista = []
    for (d, _, _) in os.walk(dir):
        lista.append(d)
    return lista


def data_dir(dir, recursive=False):
    lista = []
    files = dir_files_tree(dir) if recursive else dir_files(dir)
    for file in files:
        registro = {}
        registro['path'] = dir
        registro['name'] = file
        registro['file'] = os.path.join(dir, file)
        registro['size'] = os.path.getsize(file)
        registro['access'] = dt.datetime.fromtimestamp(os.path.getatime(registro['file']))
        registro['last'] = dt.datetime.fromtimestamp(os.path.getmtime(registro['file']))
        registro['create'] = dt.datetime.fromtimestamp(os.path.getctime(registro['file']))
        lista.append(registro)
    return lista

def list_file_text(filename, encoding='utf-8'):
    try:
        with open(filename, 'r', encoding=encoding) as fichero:
            lista = fichero.readlines()
        return lista
    except:
        lista = []
    return lista


def file_text(filename, encoding='utf-8'):
    try:
        with open(filename, 'r', encoding=encoding) as fichero:
            texto = fichero.readlines()
        return texto
    except:
        texto = ''
    return texto