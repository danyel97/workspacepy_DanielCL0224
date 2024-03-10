from lib.file2 import getValuesRandom
import os 

os.getcwd()
def saludar():
    print("Hola, te estoy saludando desde la función saludar() " \
            "del módulo saludos")
    


class Alumno:
    def __init__(self,nombre) -> None:
        self.nombre=nombre

print(__file__)
print(__name__)


a=getValuesRandom(1000)
print("esto es otro lib",a)
