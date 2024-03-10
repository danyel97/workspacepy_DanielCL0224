#Registar datos de un Alumno
import os
from clases.alumno import Alumno


ruta_relativa='modulo4/ejercicios/archivos_relativos/alumnos.txt'
ruta_absoluta=os.path.abspath(ruta_relativa)

def getInfo():
    nombre=input("Ingrese el valor de nombre:")
    dni=input("Ingrese el valor de dni:")
    nivel=input("Ingrese el valor de nivel:")
    especialidad=input("Ingrese el valor de especialidad:")
    A1=Alumno(nombre,dni,nivel,especialidad)
    return str(A1)

def inscribirAlmuno():
    try:
        with open(ruta_absoluta,mode='+a') as file:
            a=getInfo()
            file.write(a)
            file.close()

    except Exception as e:
        print(e)

def getAll():
    try:
        with open(ruta_absoluta,mode='r') as file:
            data=file.readlines()
            print(data)
    except Exception as e:
        print(e)     

while True:
    print("Ingrese su opcion")
    print("1.Inscribir Alumno")
    print("2.Obtener lista de alumnos")
    print("3.Salir")
    opcion=int(input("Ingrese su opcion:"))
    
    if opcion==1:
        inscribirAlmuno()
    elif opcion==2:
        getAll()
    elif opcion==3:
        break    
    else:
        print("Opcion no valida")





