import os
import re
#la ruta absoluta no es recomendable usar porque es variable segun la computadora
ruta_absoluta='/workspaces/workspacepy0224/modulo4/archivos/personas.txt'
ruta_relativa='modulo4/ejercicios/archivos_relativos/personas.txt'
directorio=os.getcwd()
#formas de obtener ruta abosulta de manera dinamica 
r=os.path.abspath(ruta_relativa)
rabsoluta=os.path.join(directorio,ruta_relativa)

try:
    with open(rabsoluta,mode='r') as archivo:
        data=archivo.readlines()
except Exception as e:
    print(e)

newList=[]
for i in data:
    patron=r'\n'
    informacion=i.split(';')
    print(informacion)
    dictPersonas={
        'name':informacion[1]+" "+informacion[2],
        'fecha_nacimiento':re.sub(patron,"",informacion[3])
    }
    newList.append(dictPersonas)

print(newList)

