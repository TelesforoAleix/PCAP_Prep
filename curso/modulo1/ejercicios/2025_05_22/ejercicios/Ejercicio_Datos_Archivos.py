import os
import datetime as dt
import curso.api.Ficheros as File

def data_dir(dir, recursive=False):
    lista = []
    files = File.dir_files_tree(dir) if recursive else File.dir_files(dir)
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

