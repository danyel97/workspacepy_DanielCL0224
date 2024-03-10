from lib.file1 import saludar
import lib.file2 as fx
from lib.file1 import *
saludar()

#lib.file2.getValuesRandom(100) no recomendada (x)
print(fx.getValuesRandom(100))


alumno1=Alumno('gian')

print(__file__)
print(__name__)


#######
if __name__=="__main__":
    print("es el archivo principal a ejecutar")

#####