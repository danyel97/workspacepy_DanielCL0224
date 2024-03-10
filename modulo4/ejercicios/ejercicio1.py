import sys 
import os
variable=input('data desde teclado')

lista=sys.argv
version=os.getppid()

print(variable)
print(sys.argv)
print(version)
