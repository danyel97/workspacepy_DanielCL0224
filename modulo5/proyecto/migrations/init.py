import os 
import zipfile


def getPath():
    ruta="data"
    dir_actual = os.getcwd()
    ruta_absoluta=os.path.join(dir_actual,ruta)
    return ruta_absoluta

def getPathWithFileOrDir(file):
    ruta=f"data/{file}"
    dir_actual = os.getcwd()
    ruta_absoluta=os.path.join(dir_actual,ruta)
    return ruta_absoluta


def quitar_extension(nombre_archivo):
    nombre_base, _ = os.path.splitext(nombre_archivo)
    return nombre_base

def exportZip():  
    msg=''
    ruta=getPath()
    files=os.listdir(ruta)
    print(files)
    for file in files:
        try:
            dir=quitar_extension(file)
            if not os.path.isdir(f'./data/{dir}'):
                print("creando carpeta para extraer zipeados")
                os.mkdir(f'./data/{dir}')
                msg='Proceso de descompresión exitoso'
            else:
                msg='carpeta ya existe'
                print("carpeta ya existe")
            file_absoluto=getPathWithFileOrDir(file)
            with zipfile.ZipFile(file_absoluto,'r') as zip:
                zip.extractall(path=f'./data/{dir}')
        except Exception as e:
            msg='ocurrio un error'
            print('Ocurrio un error export zip',e)

    return msg


